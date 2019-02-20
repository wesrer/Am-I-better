from src import one_time_tasks
from src import data_input_operations
from src import data_output_operations
from src import task_functions
from pathlib import Path


class TestOneTimeTasks:
    def read_test_data(self,
                       filename: str,
                       directory: Path):
        pass

    def initialize_one_time_task_object(self):
        data_input_operations_object = data_input_operations.DataInputOperations()
        data_output_operations_object = data_output_operations.DataOutputOperations()
        task_functions_object = task_functions.TaskFunctions(data_input_operations_object)

        return one_time_tasks.OneTimeTasks(data_input_operations_object=data_input_operations_object,
                                           task_functions_object=task_functions_object,
                                           active_one_time_tasks={},
                                           completed_one_time_tasks={})

    def sample_tasks(self, one_time_tasks_object):
        one_time_tasks_object.add_one_time_task("Fix This Shit Bug",
                                                priority=8)
        one_time_tasks_object.add_one_time_task("Code for 4 hours",
                                                priority=4)
        one_time_tasks_object.add_one_time_task("Study Japanese for 2 hours",
                                                priority=4)
        one_time_tasks_object.add_one_time_task("Drink some Honey Tea",
                                                priority=0)
        one_time_tasks_object.add_one_time_task("Drink some Hot Chocolate",
                                                priority=0)

        return one_time_tasks_object

    # FIXME
    def test_adding_one_time_tasks(self):
        # initialize one time tasks object
        # create sample tasks
        # assert that the dictionary returned is as expected
        sample_one_time_task_object = self.sample_tasks(self.initialize_one_time_task_object())
        assert "something" == "something"

    # FIXME
    def test_marking_tasks_as_completed(self):
        # self.oneTimeTasksObject.mark_task_as_completed()
        assert "something" == "something"

    def test_delete_task(self):
        assert "something" == "something"
