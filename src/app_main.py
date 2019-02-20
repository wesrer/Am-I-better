from src import dictionary_operations
from src import data_input_operations
from src import data_output_operations
from src import task_functions
from src import one_time_tasks
from src import habits
import src
import os


class App:
    def __init__(self):
        self.dailyTasks = []

        source_path = os.path.abspath(src.__file__)

        self.DictionaryOperationsObject = dictionary_operations.DictionaryOperations()

        self.DataInputOperationsObject = data_input_operations.DataInputOperations(source_path)

        self.DataOutputOperationsObject =\
            data_output_operations.DataOutputOperations(self.DictionaryOperationsObject)

        self.TaskFunctionsObject = \
            task_functions.TaskFunctions(self.DataInputOperationsObject)

        self.MainOneTimeTasksObject = self.initialize_main_one_time_tasks_object()

        self.HabitsObject = habits.Habits(self.DataInputOperationsObject,
                                          self.TaskFunctionsObject)

    def on_start_operations(self):
        pass

    # This is the Class Level Initialization of One Time Tasks
    # There can also be long term tasks level initialization of oneTimeTasks
    def initialize_main_one_time_tasks_object(self):
        completed_one_time_tasks = \
            self.DataInputOperationsObject.get_tasks(task_status='completed',
                                                     task_type='oneTimeTasks')
        active_one_time_tasks = \
            self.DataInputOperationsObject.get_tasks(task_status='active',
                                                     task_type='oneTimeTasks')

        return one_time_tasks.OneTimeTasks(self.DataInputOperationsObject,
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
        return self.MainOneTimeTasksObject

    def get_habit_object(self):
        return self.HabitsObject

    # FIXME: no initialized object lol
    def get_long_term_objects(self):
        pass



