from src import dictionary_operations
from copy import deepcopy

dict1 = {
    "randVal": 1,
    "anotherRandVal": "thisString",
    "yetAnotherOne": False,

}
dict2 = {
    "randVal": 1,
    "anotherRandVal": "thisString",
    "yetAnotherOne": False,
}

dictionary_operations_object = dictionary_operations.DictionaryOperations()


class TestDictionaryOperations:
    def test_task_equality_when_complete_by_is_unmatched(self):
        dict1_copy = deepcopy(dict1)
        dict2_copy = deepcopy(dict2)
        dict1_copy["completeBy"] = "unMatchedAndWrecked"
        dict2_copy["completeBy"] = "thisWillNotMatch"

        assert dictionary_operations_object.task_equality(dict1=dict1_copy,
                                                          dict2=dict2_copy)

    def test_task_equality_when_complete_by_and_assigned_on_is_unmatched(self):
        dict1_copy = deepcopy(dict1)
        dict2_copy = deepcopy(dict2)
        dict1_copy["completeBy"] = "unMatchedAndWrecked"
        dict1_copy["assignedOn"] = "thisIsAlsoUnmatched"
        dict2_copy["completeBy"] = "thisWillNotMatch"
        dict2_copy["assignedOn"] = "flySoloFam"

        assert dictionary_operations_object.task_equality(dict1=dict1_copy,
                                                          dict2=dict2_copy)

    def test_task_equality_unmatched_values_negative_case(self):
        dict1_copy = deepcopy(dict1)
        dict2_copy = deepcopy(dict2)
        dict1_copy["garbage"] = "4"
        dict1_copy["kingGarbageTheSecond"] = "56473"
        dict2_copy["garbage"] = "6"
        dict2_copy["kingGarbageTheSecond"] = "56474"

        assert not dictionary_operations_object.task_equality(dict1=dict1_copy,
                                                              dict2=dict2_copy)

    def test_task_equality_unequal_length(self):
        dict1_copy = deepcopy(dict1)
        dict1_copy["thisWillBreakLengthEquality"] = "thisValueDoesNotMatter"

        assert not dictionary_operations_object.task_equality(dict1=dict1_copy,
                                                          dict2=dict2)

    def test_dictionary_to_list_without_preserving_keys(self):
        dict1_copy = deepcopy(dict1)
        dict2_copy = deepcopy(dict2)
        parameter_dictionary = {
            "0": dict1_copy,
            "1": dict2_copy
        }

        returned_list = dictionary_operations_object.dictionary_to_list(initial_dictionary=parameter_dictionary,
                                                                        preserve_keys=False)

        condition1 = dictionary_operations_object.task_equality(returned_list[0], dict1_copy)
        condition2 = dictionary_operations_object.task_equality(returned_list[1], dict2_copy)

        assert condition2 and condition1

    def test_dictionary_to_list_preserving_keys(self):
        dict1_copy = deepcopy(dict1)
        dict2_copy = deepcopy(dict2)

        returned_list = dictionary_operations_object.dictionary_to_list({"0": dict1_copy,
                                                                         "1": dict2_copy},
                                                                        preserve_keys=True)

        dict1_copy["identifier"] = "0"
        dict2_copy["identifier"] = "1"

        condition1 = dictionary_operations_object.task_equality(returned_list[0], dict1_copy)
        condition2 = dictionary_operations_object.task_equality(returned_list[1], dict2_copy)

        assert condition1 == condition2

    def test_adding_outer_key_without_preserving_inner_keys(self):
        dict1_copy = deepcopy(dict1)
        dict1_copy["identifier"] = "0"

        returned_dict = \
            dictionary_operations_object.add_outer_dictionary(dict1_copy, key_to_use_as_outer_key="identifier")

        assert dictionary_operations_object.task_dictionary_equality({"0": dict1}, returned_dict)

    def test_adding_outer_key_preserving_inner_keys(self):
        dict1_copy = deepcopy(dict1)
        dict1_copy["identifier"] = "0"

        returned_dict = \
            dictionary_operations_object.add_outer_dictionary(dict1_copy,
                                                              preserve_inner_key=True,
                                                              key_to_use_as_outer_key="identifier")
        print(returned_dict)
        print({"0": dict1_copy})
        assert dictionary_operations_object.task_dictionary_equality({"0": dict1_copy}, returned_dict)

    def test_list_to_dictionary_depth_1(self):
        key_list = ["randVal", "anotherRandVal", "yetAnotherOne"]
        value_list = [1, "thisString", False]
        returned_dictionary = \
            dictionary_operations_object.list_to_dictionary(key_list=key_list,
                                                            value_list=value_list)

        assert dictionary_operations_object.task_equality(dict1=returned_dictionary,
                                                          dict2=dict1)

    def test_list_to_dictionary_depth_2(self):
        assert "something" == "something"


