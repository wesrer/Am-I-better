from pathlib import Path
import json

from typing import List, Dict

# Type Hints for Type Checking
StringList = List[str]
StringDict = Dict[str, str]
ListStringDict = List[StringDict]


class DataInputOperations:
    def __init__(self):
        pass

    # FUNCTION PARAMETERS:
    #   - dictionary_to_display - the task type dictionary
    def display_type_tasks_based_on_priority(self,
                                             dictionary_to_display: StringDict,
                                             sort_descending: bool = True):
        pass

    def combine_dictionaries(self,
                             list_of_dictionaries: ListStringDict):
        pass
