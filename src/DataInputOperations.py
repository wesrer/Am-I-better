from pathlib import Path

import json

from typing import List, Dict

# Type Hints for Type Checking
StringList = List[str]
StringDict = Dict[str, str]


class DataInputOperations:
    def __init__(self, resolve_path_object):

        self.resolvePathsObject = resolve_path_object
        self.dataDirectory = self.resolvePathsObject.data_directory_path()
        self.uniqueIDsFile = self.resolvePathsObject.unique_ids_path()
        self.defaultValuesFile = self.resolvePathsObject.default_values_path()

        self.uniqueIDs = self.read_unique_ids()
        self.defaultValues = self.read_default_values()

    # FUNCTION PURPOSE:
    #   reads the JSON file '< task_type >.json' from directory < task_status >
    #   inside the data directory and returns it
    #
    # FUNCTION PARAMETERS:
    #   - taskStatus: "active" or "completed"
    #   - taskType:   "oneTimeTasks" or "habits" or "longTermProjects"

    def get_tasks(self,
                  task_status: str,
                  task_type: str,
                  child_task_type: str = "None",
                  parent_task_id: int = -1) -> StringDict:

        path_address = self.dataDirectory / task_status / (task_type + '.json')

        with path_address.open() as f:
            data = json.load(f)

        if child_task_type != "None":
            data = data[parent_task_id][child_task_type]

        return data
    # FUNCTION PURPOSE:
    #   returns a new ID for the task being created
    #
    # FUNCTION PARAMETERS:
    #   - task_type:    "oneTimeTasks" or "habits" or "longTermProjects"
    #   - parent_id:    The ID of the task if it has sub-tasks
    #   - has_children: indicates whether the task type can have sub-tasks

    def get_new_unique_id_for_task(self,
                                   task_type: str,
                                   parent_id: int = -1,
                                   has_children: bool = False) -> int:

        # The dictionary has ID content at differing depths,
        # based on whether the taskType can have Children or not

        # NOTE: Current case only handles depth of 0 and 1
        #       Will need to be reimplemented if any other depths
        #       are present in the data structure
        if has_children:
            parent_dictionary = self.uniqueIDs[task_type][parent_id]
        else:
            parent_dictionary = self.uniqueIDs[task_type]

        # send the next available ID, which is either an old ID that can
        # be recycled, or a newly generated ID
        if len(self.uniqueIDs[task_type]["available"]) == 0:
            new_unique_id = parent_dictionary["next"]

            parent_dictionary["next"] = str(int(new_unique_id) + 1)
        else:
            new_unique_id = parent_dictionary["available"].pop(0)

        return int(new_unique_id)

    # FUNCTION PURPOSE:
    #   Recycles old IDs
    #
    # FUNCTION PARAMETERS:
    #   - task_type:               "oneTimeTasks" or "habits" or "longTermProjects"
    #   - parent_id:               only applies when the taskType can have sub-tasks("longTermProjects")
    #                              in which case the task has to be identified with an id
    #   - id_to_mark_as_available: the ID to recycle
    #   - has_children:            can the task type have sub-tasks

    def mark_id_as_available(self,
                             task_type: str,
                             parent_id: int = -1,
                             id_to_mark_as_available: int = -1,
                             list_of_ids_to_mark_as_available: List[int] = [],
                             has_children: bool = False, ) -> None:

        # The dictionary has ID content at differing depths,
        # based on whether the taskType can have Children or not

        if has_children:
            parent_id = self.uniqueIDs[task_type][parent_id]
        else:
            parent_id = self.uniqueIDs[task_type]

        if len(list_of_ids_to_mark_as_available) != 0:
            [parent_id["available"].append(str(x)) for x in list_of_ids_to_mark_as_available]
        else:
            parent_id["available"].append(str(id_to_mark_as_available))

        # FIXME: hacky shit
        parent_id["available"] = sorted([int(x) for x in parent_id["available"]])
        parent_id["available"] = [str(x) for x in parent_id["available"]]

    def mark_id_as_unavailable(self,
                               task_type: str,
                               parent_id: int = -1,
                               id_to_mark_as_unavailable: int = -1,
                               list_of_ids_to_mark_as_unavailable: List[int] = [],
                               has_children: bool = False, ) -> None:

        # The dictionary has ID content at differing depths,
        # based on whether the taskType can have Children or not

        if has_children:
            parent_id = self.uniqueIDs[task_type][parent_id]
        else:
            parent_id = self.uniqueIDs[task_type]

        if len(list_of_ids_to_mark_as_unavailable) != 0:
            for x in list_of_ids_to_mark_as_unavailable:
                del parent_id["available"][x]
        else:
            del parent_id["available"][id_to_mark_as_unavailable]

        parent_id["available"].sort()

    # FUNCTION PURPOSE:
    #   Sets up the data structure for tasks and sub-tasks that need their own
    #   independent ID scheme
    #
    # FUNCTION PARAMETERS:
    #   - task_id:    the id which has to be initialized
    #   - task_type:  usually just "longTermProjects"
    #
    # NOTE:
    #   This function is only meant to be called when the task type can have sub-tasks

    def initialize_new_id_slots(self,
                                task_id: int,
                                task_type: str) -> None:

        self.uniqueIDs[task_type][task_id] = {
            "available": [],
            "next": 0
        }

    # FUNCTION PURPOSE:
    #   Reads the default values dictionary from a json file

    def read_default_values(self) -> StringDict:
        with self.defaultValuesFile.open() as f:
            data = json.load(f)

        return data

    # FUNCTION PARAMETERS:
    #   None
    #
    # FUNCTION PURPOSE:
    #   Writes the default values dictionary to a json file

    def write_default_values(self) -> None:

        with open(self.defaultValuesFile, 'w') as idfile:
            data_to_write = json.dumps(self.defaultValues, sort_keys=True, indent=4, ensure_ascii=False)

            idfile.write(data_to_write)
            idfile.close()

    def get_default_values(self,
                           defualt_value_type: str,
                           default_identifier_string: str) -> str:
        return self.defaultValues[defualt_value_type][default_identifier_string]

    def reset_ids(self,
                  task_type: str,
                  reset_available: bool,
                  reset_next: bool):
        if reset_available:
            self.uniqueIDs[task_type]["available"] = []

        if reset_next:
            self.uniqueIDs[task_type]["next"] = 0

    # FUNCTION PARAMETERS:
    #   None
    #
    # FUNCTION PURPOSE:
    #   Reads the ID dictionary from a json file

    def read_unique_ids(self) -> StringDict:
        with self.uniqueIDsFile.open() as f:
            data = json.load(f)
        return data

    # FUNCTION PARAMETERS:
    #   None
    #
    # FUNCTION PURPOSE:
    #   Writes the ID dictionary to a json file

    def write_unique_ids(self) -> None:

        with open(self.uniqueIDsFile, 'w') as idfile:
            data_to_write = json.dumps(self.uniqueIDs, sort_keys=True, indent=4, ensure_ascii=False)

            idfile.write(data_to_write)
            idfile.close()




