import os

from src.operations.DictionaryOperations import DictionaryOperations
from src.operations.ResolvePaths import ResolvePaths
from src.operations.TaskFunctions import TaskFunctions
from src.operations.TimeOperations import TimeOperations

from src.DataOutputOperations import DataOutputOperations
from src.DataInputOperations import DataInputOperations
from src.OneTimeTasks import OneTimeTasks
from src.Habits import Habits

from src.Experimental.PandasTest import PandasTest


class App:
    def __init__(self, execution_type: str = "dev"):

        # self.dailyTasks = []

        source_path = os.path.dirname(os.path.abspath(__file__))

        # UTILITY MODULES

        self.DictionaryOperations = DictionaryOperations()
        self.ResolvePaths = ResolvePaths(source_path, execution_type=execution_type)

        # I/O MODULES

        self.DataInputOperations = DataInputOperations(resolve_path_object=self.ResolvePaths)
        self.DataOutputOperations = DataOutputOperations(resolve_paths=self.ResolvePaths,
                                                         dictionary_operations=self.DictionaryOperations)

        # COMMON METHODS MODULE
        self.TaskFunctions = TaskFunctions(data_input_operations_object=self.DataInputOperations)
        self.TimeOperations = TimeOperations()

        # TASK MODULES

        self.MainOneTimeTasks = self.initialize_main_one_time_tasks_object()

        self.Habits = Habits(data_input_operations_object=self.DataInputOperations,
                             data_output_operations_object=self.DataOutputOperations,
                             task_functions_object=self.TaskFunctions,
                             time_operations_object=self.TimeOperations)

        # FIXME: testing module - delete later
        self.PandasTest = PandasTest(one_time_tasks_object=self.MainOneTimeTasks)

    def on_start_operations(self):
        self.Habits.refresh_habits()

    # NOTE: This is the Class Level Initialization of oneTimeTasks
    #       There can also be long term tasks level initialization of oneTimeTasks
    def initialize_main_one_time_tasks_object(self):
        completed_one_time_tasks = self.DataInputOperations.get_tasks(task_status='completed',
                                                                      task_type='oneTimeTasks')
        active_one_time_tasks = self.DataInputOperations.get_tasks(task_status='active',
                                                                   task_type='oneTimeTasks')

        return OneTimeTasks(data_input_operations_object=self.DataInputOperations,
                            data_output_operations_object=self.DataOutputOperations,
                            task_functions_object=self.TaskFunctions,
                            active_one_time_tasks=active_one_time_tasks,
                            completed_one_time_tasks=completed_one_time_tasks)

    def on_close_operations(self):
        # TODO: have to do this for all the kinds of operations
        self.MainOneTimeTasks.save_active_one_time_tasks()
        self.MainOneTimeTasks.save_completed_one_time_tasks()

        self.Habits.save_active_habits()
        self.Habits.save_inactive_habits()
        self.Habits.save_completed_habits()

        self.DataInputOperations.write_unique_ids()

    # GET operations
    def get_one_time_task_object(self):
        return self.MainOneTimeTasks

    def get_habit_object(self):
        return self.Habits

    # FIXME: delete later
    def get_pandas(self):
        return self.PandasTest

    # FIXME: no initialized object lol
    def get_long_term_objects(self):
        pass



