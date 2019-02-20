from src import app_main

AppObject = app_main.App()


class TestInitializationsInAppMain:
    # helper methods
    def get_class_name(self, some_object):
        return some_object.__class__.__name__

    # test methods
    def test_one_time_task_object_initialization_in_app_main(self):
        initialized_one_time_task_object = AppObject.get_one_time_task_object()
        assert self.get_class_name(initialized_one_time_task_object) == "OneTimeTasks"

    def test_habit_object_initialization_in_app_main(self):
        initialized_one_time_task_object = AppObject.get_habit_object()
        assert self.get_class_name(initialized_one_time_task_object) == "Habits"

    # FIXME: write this after actually implementing it
    # def test_long_term_project_initialization_in_app_main(self):
    #     initialized_long_term_project_object = AppObject.


# def test_adding_one_time_tasks():
#     # FIXME
#     desired_return_value = "what"
#
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
