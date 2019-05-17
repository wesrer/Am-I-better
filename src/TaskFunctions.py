import datetime
from . import DictionaryOperations

from typing import List, Dict

# Custom Type Hints for Type Checking
StringList = List[str]
StringDict = Dict[str, str]


# TODO: implement complete_by parameters
class TaskFunctions:
    # TODO: figure out how to Type Cast Custom Objects
    def __init__(self, data_input_operations_object):
        self.DataInputOperations = data_input_operations_object
        self.DictionaryOperations = DictionaryOperations.DictionaryOperations()

    # FIXME: implement this
    def convert_time_string_to_dictionary(self,
                                          time_string: str) -> StringDict:
        pass

    # FUNCTION PURPOSE:
    #   Add tasks to the three primary categories of active tasks
    #
    # FUNCTION PARAMETERS:
    #   - task_String: The actual task that the user wants to do
    #   - task_type: "oneTimeTasks" or "habits" or "longTermProjects"
    #   - priority: Adds variable priorities to different tasks
    #   - complete_by: A specific deadline for the particular task (doesn't apply to habits)
    #   - refresh_rate: The rate at which

    # TODO: add the custom default values implementation
    # TODO: figure out how the refresh rate works
    @staticmethod
    def add_tasks(task_string: str,
                  task_type: str,
                  priority: int = 0,
                  weight: int = 3,
                  complete_by: str = "N/A",
                  refresh_rate: int = 1) -> StringDict:

        # By default, all tasks need to be completed by 24 hours of initializing them
        if task_type == "oneTimeTasks":
            complete_by = datetime.datetime.now() + datetime.timedelta(hours=24)

            # formatting the string
            complete_by = complete_by.strftime("%c")

        elif task_type == "longTermProjects":
            complete_by = datetime.datetime.now() + datetime.timedelta(years=1)

        # make a JSON object to append to the existing list
        data_dict = {
            "taskString": task_string,
            "weight": str(weight),
            "assignedOn": (datetime.datetime.now()).strftime("%c"),
            "priority": str(priority),
        }

        if task_type == 'oneTimeTasks':
            data_dict["completeBy"] = complete_by
        elif task_type == 'habits':
            data_dict["refreshRate"] = str(refresh_rate)

        return data_dict

    # FUNCTION PARAMETERS:
    #   - task_dictionary: The already existing dictionary of the parent task
    #                      to which the task will be added
    #   - sub_task_string: The task which is going to be added
    # FUNCTION PURPOSE

    # TODO
    def add_sub_tasks(self,
                      task_dictionary: StringDict,
                      sub_task_string: str,
                      priority: int = 0,
                      complete_by: bool = False) -> StringDict:
        pass

    # Moves Task From Active Dictionary to Completed Dictionary
    # and adjusts ids to reflect this task

    # FIXME: implement parent-child relationships, because they are clearly
    #        not working
    # TODO: allow multiple tasks to be marked as completed in one function call
    def mark_task_as_completed(self,
                               id_to_mark_as_completed: int,
                               active_dictionary: StringDict,
                               completed_dictionary: StringDict,
                               task_type: str,
                               completed_task_type: str,
                               parent_id: int = -1,
                               has_children: bool = False) -> [StringDict, StringDict]:

        unique_id = self.DataInputOperations.get_new_unique_id_for_task(task_type=completed_task_type,
                                                                        parent_id=parent_id,
                                                                        has_children=has_children)

        completed_dictionary[str(unique_id)] = active_dictionary[str(id_to_mark_as_completed)]

        self.DataInputOperations.mark_id_as_available(task_type=task_type,
                                                      parent_id=parent_id,
                                                      has_children=has_children,
                                                      id_to_mark_as_available=id_to_mark_as_completed)

        del active_dictionary[str(id_to_mark_as_completed)]

        return active_dictionary, completed_dictionary

    # TODO: implement parent_id and has_children functionalities
    # TODO: allow multiple ids to be unmarked in one call
    def unmark_a_completed_task(self,
                                id_to_unmark: int,
                                active_dictionary: StringDict,
                                completed_dictionary: StringDict,
                                task_type: str,
                                completed_task_type: str,
                                parent_id: int = -1,
                                has_children: bool = False):
        unique_id = self.DataInputOperations.get_new_unique_id_for_task(task_type=task_type,
                                                                        parent_id=parent_id,
                                                                        has_children=has_children)

        # pushing the string to the active_dictionary under a next available id
        active_dictionary[str(unique_id)] = completed_dictionary[str(id_to_unmark)]

        self.DataInputOperations.mark_id_as_available(task_type=completed_task_type,
                                                      parent_id=parent_id,
                                                      has_children=has_children,
                                                      id_to_mark_as_available=id_to_unmark)

        del completed_dictionary[str(id_to_unmark)]

        return active_dictionary, completed_dictionary

    # FIXME: Okay, this is not a primary concern, but it sucks that you have
    #        to send all of this excess data just because you are calling the
    #        markIDAsAvailable function
    def delete_task(self,
                    id_to_delete: int,
                    active_dictionary: StringDict,
                    task_type: str,
                    parent_id: int = -1,
                    has_children: bool = False) -> StringDict:

        del active_dictionary[str(id_to_delete)]

        self.DataInputOperations.mark_id_as_available(task_type=task_type,
                                                      id_to_mark_as_available=id_to_delete,
                                                      has_children=has_children,
                                                      parent_id=parent_id)

        return active_dictionary

    # TODO: implement this
    def sort_by_priority(self,
                         active_dictionary: StringDict) -> StringDict:
        self.DictionaryOperations.dict_of_dicts_to_list_of_dicts()
        self.DictionaryOperations.sort_list_of_dictionaries_by_key()