from src import dictionary_operations

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


class TestDictionaryOperations:
    def test_task_equality_when_complete_by_is_unmatched(self):
        dict1["completeBy"] = "unMatchedAndWrecked"
        dict2["completeBy"] = "thisWillNotMatch"

        dictionary_operations_object = dictionary_operations.DictionaryOperations()
        assert dictionary_operations_object.task_equality(dict1=dict1,
                                                          dict2=dict2)

    def test_task_equality_when_complete_by_and_assigned_on_is_unmatched(self):
        dict1["completeBy"] = "unMatchedAndWrecked"
        dict1["assignedOn"] = "thisIsAlsoUnmatched"
        dict2["completeBy"] = "thisWillNotMatch"
        dict2["completeBy"] = "flySoloFam"

        dictionary_operations_object = dictionary_operations.DictionaryOperations()
        assert dictionary_operations_object.task_equality(dict1=dict1,
                                                          dict2=dict2)


