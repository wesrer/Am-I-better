# General dictionary functions that I use for this program
# but can be used anywhere really

from typing import Dict, List
from operator import itemgetter


class DictionaryOperations:
    def __init__(self):
        pass

    def list_to_dictionary(self,
                           key_list: List,
                           value_list: List) -> Dict:
        return_dictionary = {}
        for key, value in list(zip(key_list, value_list)):
            return_dictionary[key] = value

        return return_dictionary

    def dictionary_to_list(self,
                           initial_dictionary: Dict,
                           preserve_keys: bool = True,
                           key_string: str = "identifier") -> List:
        return_list = []
        for key, value in initial_dictionary.items():
            if preserve_keys:
                value[key_string] = key

            return_list.append(value)

        return return_list

    def add_outer_dictionary(self,
                             initial_dictionary: Dict,
                             preserve_inner_key: bool = False,
                             key_to_use_as_outer_key: str = "identifier"):
        return_dictionary = dict()

        # FIXME: the name of the function variable is misleading because the
        # FIXME: the inner key is not being converted to the outer key, but
        # FIXME: rather the value associated with the inner key is being used.
        outer_key = initial_dictionary[key_to_use_as_outer_key]

        if not preserve_inner_key:
            del initial_dictionary[key_to_use_as_outer_key]

        # print({outer_key: initial_dictionary})

        return {outer_key: initial_dictionary}


    # FIXME: Implement descending sort
    def sort_list_of_dictionaries_by_key(self,
                                         list_of_dict: List[Dict],
                                         sort_key,
                                         sort_descending: bool = True):
        return sorted(list_of_dict,
                      key=itemgetter(sort_key))

    # TODO
    def task_dictionary_equality(self,
                                 dict1: Dict,
                                 dict2: Dict):

        for identifier, value in dict1.items():
            if not self.task_equality(value, dict2[identifier]):
                return False

        return True

    def task_equality(self,
                      dict1: Dict,
                      dict2: Dict):

        if not len(dict1) == len(dict2):
            return False

        for key, value in dict1.items():
            if key == "assignedOn" or key == "completeBy":
                continue
            elif dict2[key] != value:
                return False

        return True
