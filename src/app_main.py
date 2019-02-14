from DataIOOperations import DataIOOperations
from TaskFunctions import TaskFunctions
from oneTimeTasks import OneTimeTasks
from habits import Habits


class App:
    def __init__(self):
        self.dailyTasks = []
        self.DataIOOperationsObject = DataIOOperations()
        self.TaskFunctionsObject = taskFunctions(self.DataIOOperationsObject)

        self.MainOneTimeTasksObject = self.initialize_main_one_time_tasks_object()
        self.HabitsObject = Habits(self.DataIOOperationsObject,
                                   self.TaskFunctionsObject)

    def on_start_operations(self):
        pass

    # This is the Class Level Initialization of One Time Tasks
    # There can also be long term tasks level initialization of oneTimeTasks
    def initialize_main_one_time_tasks_object(self):
        completed_one_time_tasks = \
            self.DataIOOperationsObject.get_tasks(task_status='completed',
                                                  task_type='oneTimeTasks')
        active_one_time_tasks = \
            self.DataIOOperationsObject.get_tasks(task_status='active',
                                                  task_type='oneTimeTasks')

        return OneTimeTasks(self.DataIOOperationsObject,
                            self.TaskFunctionsObject,
                            active_one_time_tasks,
                            completed_one_time_tasks)

    def on_close_operations(self):
        # TODO: have to do this for all the kinds of operations
        self.OneTimeTasksObject.save_active_one_time_tasks()
        self.OneTimeTasksObject.save_completed_one_time_tasks()

        self.DataIOOperationsObject.write_unique_ids()

    # GET operations
    def get_one_time_task_object(self):
        return self.OneTimeTasksObject



