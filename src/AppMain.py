from . import DictionaryOperations
from . import DataInputOperations
from . import DataOutputOperations
from . import TaskFunctions
from . import ResolvePaths
from . import OneTimeTasks
from . import Habits
import os


class App:
    def __init__(self, execution_type):

        # self.dailyTasks = []

        source_path = os.path.dirname(os.path.abspath(__file__))

        # UTILITY MODULES

        self.DictionaryOperations = DictionaryOperations.DictionaryOperations()
        self.ResolvePaths = ResolvePaths.ResolvePaths(source_path, execution_type=execution_type)

        # I/O MODULES

        self.DataInputOperations = DataInputOperations.DataInputOperations(resolve_path_object=self.ResolvePaths)
        self.DataOutputOperations = \
            DataOutputOperations.DataOutputOperations(resolve_paths=self.ResolvePaths,
                                                      dictionary_operations=self.DictionaryOperations)

        # COMMON METHODS MODULE
        self.TaskFunctions = TaskFunctions.TaskFunctions(data_input_operations_object=self.DataInputOperations)

        # TASK MODULES

        self.MainOneTimeTasks = self.initialize_main_one_time_tasks_object()

        self.Habits = Habits.Habits(data_input_operations_object=self.DataInputOperations,
                                    task_functions_object=self.TaskFunctions)

    def on_start_operations(self):
        pass

    # NOTE: This is the Class Level Initialization of oneTimeTasks
    #       There can also be long term tasks level initialization of oneTimeTasks
    def initialize_main_one_time_tasks_object(self):
        completed_one_time_tasks = self.DataInputOperations.get_tasks(task_status='completed',
                                                                      task_type='oneTimeTasks')
        active_one_time_tasks = self.DataInputOperations.get_tasks(task_status='active',
                                                                   task_type='oneTimeTasks')

        return OneTimeTasks.OneTimeTasks(data_input_operations_object=self.DataInputOperations,
                                         task_functions_object=self.TaskFunctions,
                                         active_one_time_tasks=active_one_time_tasks,
                                         completed_one_time_tasks=completed_one_time_tasks)

    def on_close_operations(self):
        # TODO: have to do this for all the kinds of operations
        self.MainOneTimeTasks.save_active_one_time_tasks()
        self.MainOneTimeTasks.save_completed_one_time_tasks()

        self.DataInputOperations.write_unique_ids()

    # GET operations
    def get_one_time_task_object(self):
        return self.MainOneTimeTasks

    def get_habit_object(self):
        return self.Habits

    # FIXME: no initialized object lol
    def get_long_term_objects(self):
        pass



