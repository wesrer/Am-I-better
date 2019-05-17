from src import DictionaryOperations
from copy import deepcopy

dictionary_operations = DictionaryOperations.DictionaryOperations()

template_dict = {
    "randVal": 1,
    "anotherRandVal": "thisString",
    "yetAnotherOne": False,

}


class TestDictionaryOperations:
    def test_task_equality_when_complete_by_is_unmatched(self):
        dict1 = deepcopy(template_dict)
        dict2 = deepcopy(template_dict)

        dict1["completeBy"] = "unMatchedAndWrecked"
        dict2["completeBy"] = "thisWillNotMatch"

        assert dictionary_operations.check_task_dictionary_equality(dict1, dict2)

    def test_task_equality_when_complete_by_and_assigned_on_is_unmatched(self):
        dict1 = deepcopy(template_dict)
        dict2 = deepcopy(template_dict)

        dict1["completeBy"] = "unMatchedAndWrecked"
        dict1["assignedOn"] = "thisIsAlsoUnmatched"
        dict2["completeBy"] = "thisWillNotMatch"
        dict2["assignedOn"] = "flySoloFam"

        assert dictionary_operations.check_task_dictionary_equality(dict1, dict2)

    def test_task_equality_unmatched_values_negative_case(self):
        dict1 = deepcopy(template_dict)
        dict2 = deepcopy(template_dict)
        dict1["garbage"] = "4"
        dict1["kingGarbageTheSecond"] = "56473"

        dict2["garbage"] = "6"
        dict2["kingGarbageTheSecond"] = "56474"

        assert not dictionary_operations.check_task_dictionary_equality(dict1, dict2)

    def test_task_equality_unequal_length(self):
        dict1 = deepcopy(template_dict)
        dict1["thisWillBreakLengthEquality"] = "thisValueDoesNotMatter"

        assert not dictionary_operations.check_task_dictionary_equality(dict1, template_dict)

    def test_dictionary_to_list_without_preserving_keys(self):
        dict1 = deepcopy(template_dict)
        dict2 = deepcopy(template_dict)
        parameter_dictionary = {
            "0": dict1,
            "1": dict2
        }

        returned_list = dictionary_operations.dict_of_dicts_to_list_of_dicts(initial_dictionary=parameter_dictionary,
                                                                             preserve_keys=False)

        condition1 = dictionary_operations.check_task_dictionary_equality(returned_list[0], dict1, skip_time_values=False)
        condition2 = dictionary_operations.check_task_dictionary_equality(returned_list[1], dict2, skip_time_values=False)

        assert condition2 and condition1

    def test_dictionary_to_list_preserving_keys(self):
        dict1 = deepcopy(template_dict)
        dict2 = deepcopy(template_dict)

        parameter_dictionary = {"0": dict1,
                                "1": dict2}

        returned_list = dictionary_operations.dict_of_dicts_to_list_of_dicts(parameter_dictionary,
                                                                             preserve_keys=True)

        dict1["identifier"] = "0"
        dict2["identifier"] = "1"

        condition1 = dictionary_operations.check_task_dictionary_equality(returned_list[0], dict1, skip_time_values=False)
        condition2 = dictionary_operations.check_task_dictionary_equality(returned_list[1], dict2, skip_time_values=False)

        assert condition1 == condition2

    def test_adding_outer_key_without_preserving_inner_keys(self):
        dict1 = deepcopy(template_dict)
        dict1["identifier"] = "0"

        returned_dict = dictionary_operations.add_outer_dictionary(dict1,
                                                                   preserve_inner_key=False,
                                                                   key_to_use_as_outer_key="identifier")

        assert dictionary_operations.check_equality_of_dicts_with_nested_task_dicts({"0": template_dict}, returned_dict)

    def test_adding_outer_key_preserving_inner_keys(self):
        dict1 = deepcopy(template_dict)
        dict1["identifier"] = "0"

        returned_dict = dictionary_operations.add_outer_dictionary(dict1,
                                                                   preserve_inner_key=True,
                                                                   key_to_use_as_outer_key="identifier")
        assert dictionary_operations.check_equality_of_dicts_with_nested_task_dicts({"0": dict1}, returned_dict)

    def test_list_to_dictionary_depth_1(self):
        key_list = ["randVal", "anotherRandVal", "yetAnotherOne"]
        value_list = [1, "thisString", False]
        returned_dictionary = dictionary_operations.key_and_value_lists_to_dict(key_list=key_list,
                                                                                value_list=value_list)

        assert dictionary_operations.check_task_dictionary_equality(dict1=returned_dictionary,
                                                                    dict2=template_dict)

    # TODO: implement this
    # def test_list_to_dictionary_depth_2(self):
    #     assert "something" == "something"


