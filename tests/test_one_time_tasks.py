from src import one_time_tasks
from src import data_input_operations
from src import data_output_operations
from src import task_functions
from src import dictionary_operations
from src import resolve_paths

import os
import json
import src
from pathlib import Path

dictionary_operations_object = dictionary_operations.DictionaryOperations()

test_data_path = Path(os.path.dirname(os.path.abspath(src.__file__))) / '..' / 'tests' / 'test_data'


class TestOneTimeTasks:
    def read_test_data(self,
                       path_val: Path):
        with path_val.open() as f:
            data = json.load(f)

        return data

    def initialize_one_time_task_object(self):
        source_path = os.path.dirname(os.path.abspath(__file__))

        resolve_paths_object = resolve_paths.ResolvePaths(module_path=source_path,
                                                          execution_type="test")

        data_input_operations_object = \
            data_input_operations.DataInputOperations(resolve_path_object=resolve_paths_object)
        # data_output_operations_object = \
        #     data_output_operations.DataOutputOperations(dictionary_operations.DictionaryOperations())
        task_functions_object = task_functions.TaskFunctions(data_input_operations_object)

        return one_time_tasks.OneTimeTasks(data_input_operations_object=data_input_operations_object,
                                           task_functions_object=task_functions_object,
                                           active_one_time_tasks={},
                                           completed_one_time_tasks={})

    def sample_tasks_1(self, one_time_tasks_object):
        one_time_tasks_object.add_one_time_task("Fix This Shit Bug",
                                                priority=8,
                                                weight=3)
        one_time_tasks_object.add_one_time_task("Code for 4 hours",
                                                priority=4,
                                                weight=3)
        one_time_tasks_object.add_one_time_task("Study Japanese for 2 hours",
                                                priority=4,
                                                weight=3)
        one_time_tasks_object.add_one_time_task("Drink some Honey Tea",
                                                priority=0,
                                                weight=3)
        one_time_tasks_object.add_one_time_task("Drink some Hot Chocolate",
                                                priority=0,
                                                weight=3)

        return one_time_tasks_object

    def test_adding_one_time_tasks(self):
        sample_one_time_task_object = \
            self.sample_tasks_1(self.initialize_one_time_task_object())

        returned_output = sample_one_time_task_object.get_active_one_time_tasks()
        expected_output = self.read_test_data(test_data_path / 'active' / 'oneTimeTasks_simple_addition.json')

        assert dictionary_operations_object.task_dictionary_equality(returned_output,
                                                                     expected_output)

    def test_marking_tasks_as_completed(self):
        sample_one_time_task_object = \
            self.sample_tasks_1(self.initialize_one_time_task_object())

        sample_one_time_task_object.mark_task_as_completed('1')
        sample_one_time_task_object.add_one_time_task(task_string="Test All the existing code",
                                                      priority=4,
                                                      weight=3)

        returned_active_output = sample_one_time_task_object.get_active_one_time_tasks()
        returned_completed_output = sample_one_time_task_object.get_completed_one_time_tasks()

        expected_active_output = \
            self.read_test_data(test_data_path / 'active' / 'oneTimeTasks_simple_mark_as_complete.json')

        expected_completed_output = \
            self.read_test_data(test_data_path / 'completed' / 'oneTimeTasks_simple_mark_as_complete.json')

        condition1 = \
            dictionary_operations_object.task_dictionary_equality(expected_active_output, returned_active_output)
        condition2 = \
            dictionary_operations_object.task_dictionary_equality(expected_completed_output, returned_completed_output)

        assert condition1 and condition2

    # def test_reusing_ids_marked_as_completed(self):
    #     sample_one_time_task_object = self.sample_tasks(self.initialize_one_time_task_object())
    #
    #     sample_one_time_task_object.mark_task_as_completed(1)
    #     sample_one_time_task_object.add_one_time_task("Test the new feature",
    #                                                   priority=0)
    #
    #     assert "something" == "something"

    # def test_delete_task(self):
    #     sample_one_time_task_object = self.sample_tasks(self.initialize_one_time_task_object())
    #
    #     sample_one_time_task_object.mark_task_as_completed(id_to_mark_as_completed=1)
    #     sample_one_time_task_object.add_one_time_task("Test the new feature",
    #                                                   priority=0)
    #
    #     assert "something" == "something"



