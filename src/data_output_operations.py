import json
from pathlib import Path
from typing import List, Dict

# Type Hints for Type Checking
StringList = List[str]
StringDict = Dict[str, str]
ListStringDict = List[StringDict]


class DataOutputOperations:
    def __init__(self,
                 resolve_paths_object,
                 dictionary_operations_object):

        self.resolvePathsObject = resolve_paths_object
        self.DictionaryOperationsObject = dictionary_operations_object

    # FUNCTION PARAMETERS:
    #   - dictionary_to_display - the task type dictionary

    # FIXME: implement descending sort
    # FIXME: find a better printing method, json dumping is tentative
    def display_type_tasks_based_on_priority(self,
                                             dictionary_to_display: StringDict,
                                             sort_descending: bool = True):
        list_dictionary = \
            self.DictionaryOperationsObject.dictionary_to_list(initial_dictionary=dictionary_to_display,
                                                               preserve_keys=True,
                                                               key_string="id")
        list_dictionary = \
            self.DictionaryOperationsObject.sort_list_of_dictionaries_by_key(list_of_dict=list_dictionary,
                                                                             sort_key="priority")
        print(json.dumps(list_dictionary,
                         sort_keys=True,
                         indent=4,
                         ensure_ascii=False))

    # TODO:
    def combine_dictionaries(self,
                             list_of_dictionaries: ListStringDict):
        pass

    # FUNCTION PARAMETERS:
    #   - taskStatus - "active" or "completed"
    #   - taskType - "oneTimeTasks" or "habits" or "longTermProjects"
    #   - dictionaryToSave - The python dictionary that is going to be converted
    #   to JSON and then saved
    #
    # FUNCTION PURPOSE:
    #   saves a python dictionary to a ' < taskType >.json' file in directory
    #   < taskStatus >

    def save_as_file(self,
                     task_status: str,
                     task_type: str,
                     directory_address: Path,
                     dictionary_to_save: StringDict) -> None:
        file_address = directory_address / task_status / (task_type + ".json")

        with open(file_address, 'w') as writefile:
            json.dump(dictionary_to_save,
                      writefile,
                      sort_keys=True,
                      indent=4,
                      ensure_ascii=False)
