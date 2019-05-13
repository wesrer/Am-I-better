# General dictionary functions that I use for this program
# but can be used anywhere really

from typing import Dict, List
from operator import itemgetter


class DictionaryOperations:
    def __init__(self):
        pass

    @staticmethod
    def key_and_value_lists_to_dict(key_list: List,
                                    value_list: List) -> Dict:
        return_dictionary = {}

        for key, value in list(zip(key_list, value_list)):
            return_dictionary[key] = value

        return return_dictionary

    # NOTE: when the preserve key option is set to True, then the key associated with
    #       the dictionary is added to the dictionary as a value under the key_string key
    #       which by default is "identifier"
    @staticmethod
    def dict_of_dicts_to_list_of_dicts(initial_dictionary: Dict,
                                       preserve_keys: bool = True,
                                       key_string: str = "identifier") -> List:
        return_list = []
        for key, value in initial_dictionary.items():
            if preserve_keys:
                value[key_string] = key

            return_list.append(value)

        return return_list

    # Takes a value from the inner dictionary, and makes that the key of the outer
    # dictionary
    # NOTE: This is useful to reverse the effects of the previous method -
    #       `dict_of_dicts_to_list_of_dicts`
    @staticmethod
    def add_outer_dictionary(initial_dictionary: Dict,
                             preserve_inner_key: bool = False,
                             key_to_use_as_outer_key: str = "identifier"):

        # FIXME: the name of the function variable is misleading because the
        # FIXME: the inner key is not being converted to the outer key, but
        # FIXME: rather the value associated with the inner key is being used.
        outer_key = initial_dictionary[key_to_use_as_outer_key]

        if not preserve_inner_key:
            del initial_dictionary[key_to_use_as_outer_key]

        # print({outer_key: initial_dictionary})

        return {outer_key: initial_dictionary}

    # FIXME: Implement descending sort
    @staticmethod
    def sort_list_of_dictionaries_by_key(list_of_dict: List[Dict],
                                         sort_key,
                                         sort_descending: bool = True):
        return sorted(list_of_dict,
                      key=itemgetter(sort_key))

    def check_equality_of_dicts_of_task_dicts(self, dict1: Dict, dict2: Dict):

        for identifier, value in dict1.items():
            if not self.check_task_dictionary_equality(value, dict2[identifier]):
                return False

        return True

    @staticmethod
    def check_task_dictionary_equality(dict1: Dict,
                                       dict2: Dict,
                                       skip_time_values: bool = True):

        if not len(dict1) == len(dict2):
            return False

        for key, value in dict1.items():
            if skip_time_values and (key == "assignedOn" or key == "completeBy"):
                continue
            elif dict2[key] != value:
                return False

        return True
