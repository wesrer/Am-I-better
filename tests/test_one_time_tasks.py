from src import one_time_tasks
from pathlib import Path

class TestOneTimeTasks:
    def read_test_data(self,
                       filename: str,
                       directory: Path):
        pass

    def initialize_one_time_task_object(self):
        pass

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
        assert "something" == "something"

    # FIXME
    def test_marking_tasks_as_completed(self):
        # self.oneTimeTasksObject.mark_task_as_completed()
        assert "something" == "something"

    def test_delete_task(self):
        assert "something" == "something"
