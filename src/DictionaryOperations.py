# General dictionary functions that I use for this program
# but can be used anywhere really

from typing import Dict, List
from operator import itemgetter


def list_to_dictionary(key_list: List,
                       value_list: List) -> Dict:
    return_dictionary = {}
    for key, value in list(zip(key_list, value_list)):
        return_dictionary[key] = value

    return return_dictionary


def dictionary_to_list(initial_dictionary: Dict,
                       preserve_keys: bool = True,
                       key_string: str = "identifier") -> List:
    return_list = []
    for key, value in initial_dictionary:
        if preserve_keys:
            value[key_string] = key

        return_list.append(value)

        return return_list


def sort_list_of_dictionaries_by_key(list_of_dict: List[Dict],
                                     sort_key):
    return sorted(list_of_dict,
                  key=itemgetter(sort_key))

