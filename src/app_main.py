from . import dictionary_operations
from . import data_input_operations
from . import data_output_operations
from . import task_functions
from . import resolve_paths
from . import one_time_tasks
from . import habits
import os


class App:
    def __init__(self, execution_type):
        self.dailyTasks = []

        source_path = os.path.dirname(os.path.abspath(__file__))

        self.DictionaryOperationsObject = dictionary_operations.DictionaryOperations()

        self.ResolvePathsObject = resolve_paths.ResolvePaths(source_path,
                                                             execution_type=execution_type)

        self.DataInputOperationsObject = \
            data_input_operations.DataInputOperations(resolve_path_object=self.ResolvePathsObject)

        self.DataOutputOperationsObject =\
            data_output_operations.DataOutputOperations(dictionary_operations_object=self.DictionaryOperationsObject,
                                                        resolve_paths_object=self.ResolvePathsObject)

        self.TaskFunctionsObject = \
            task_functions.TaskFunctions(self.DataInputOperationsObject)

        self.MainOneTimeTasksObject = self.initialize_main_one_time_tasks_object()

        self.HabitsObject = habits.Habits(data_input_operations_object=self.DataInputOperationsObject,
                                          task_functions_object=self.TaskFunctionsObject)

    def on_start_operations(self):
        pass

    # This is the Class Level Initialization of One Time Tasks
    # There can also be long term tasks level initialization of oneTimeTasks
    def initialize_main_one_time_tasks_object(self):

        # self.dataDirectory / task_status / (task_type + ".json")

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
        self.MainOneTimeTasksObject.save_active_one_time_tasks()
        self.MainOneTimeTasksObject.save_completed_one_time_tasks()

        self.DataInputOperationsObject.write_unique_ids()

    # GET operations
    def get_one_time_task_object(self):
        return self.MainOneTimeTasksObject

    def get_habit_object(self):
        return self.HabitsObject

    # FIXME: no initialized object lol
    def get_long_term_objects(self):
        pass



