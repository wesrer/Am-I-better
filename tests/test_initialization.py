from src import app_main
from pathlib import Path

AppObject = app_main.App()


class TestInitializationsInAppMain:
    def test_one_time_task_object_initialization_in_app_main(self):
        initialized_one_time_task_object = AppObject.get_one_time_task_object()
        assert initialized_one_time_task_object.__class__.__name__ == "OneTimeTasks"

    def test_habit_object_initialization_in_app_main(self):
        initialized_one_time_task_object = AppObject.get_habit_object()
        assert initialized_one_time_task_object.__class__.__name__ == "Habits"



# def test_adding_one_time_tasks():
#     # FIXME
#     desired_return_value = "what"
#     returned_value = oneTimeTaskObject.get_active_one_time_tasks()
#
#     oneTimeTaskObject.add_one_time_task("Fix This Shit Bug",
#                                         priority=8)
#     oneTimeTaskObject.add_one_time_task("Code for 4 hours",
#                                         priority=4)
#     oneTimeTaskObject.add_one_time_task("Study Japanese for 2 hours",
#                                         priority=4)
#     oneTimeTaskObject.add_one_time_task("Drink some Honey Tea",
#                                         priority=0)
#     oneTimeTaskObject.add_one_time_task("Drink some Hot Chocolate",
#                                         priority=0)
#
#     # TODO
#
#     assert desired_return_value == returned_value
#
# def test
#
# # TODO: LOL fix her bugs
# def test_hana():
#     pass
#
