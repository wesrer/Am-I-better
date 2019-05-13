from src import OneTimeTasks
from src import DataInputOperations
from src import DataOutputOperations
from src import TaskFunctions
from src import DictionaryOperations
from src import ResolvePaths

import os
import json
import src
from pathlib import Path

dictionary_operations_object = DictionaryOperations.DictionaryOperations()

test_data_path = Path(os.path.dirname(os.path.abspath(src.__file__))) / '..' / 'tests' / 'test_data'


class TestOneTimeTasks:
    def __init__(self):
        self.check_equality_of_dict_of_task_dicts = dictionary_operations_object.check_equality_of_dicts_of_task_dicts

    @staticmethod
    def read_test_data(path_val: Path):
        with path_val.open() as f:
            data = json.load(f)

        return data

    @staticmethod
    def initialize_one_time_task_object():
        source_path = os.path.dirname(os.path.abspath(__file__))

        resolve_paths_object = ResolvePaths.ResolvePaths(module_path=source_path,
                                                         execution_type="test")

        data_input_operations_object = DataInputOperations.DataInputOperations(resolve_path_object=resolve_paths_object)

        # data_output_operations_object = \
        #     data_output_operations.DataOutputOperations(dictionary_operations.DictionaryOperations())

        task_functions_object = TaskFunctions.TaskFunctions(data_input_operations_object)

        one_time_tasks_object = OneTimeTasks.OneTimeTasks(data_input_operations_object=data_input_operations_object,
                                                          task_functions_object=task_functions_object,
                                                          active_one_time_tasks={},
                                                          completed_one_time_tasks={})

        return one_time_tasks_object, data_input_operations_object

    @staticmethod
    def sample_tasks_1(one_time_tasks_object):
        one_time_tasks_object.add_one_time_task("Fix This Shit Bug", priority=8, weight=3)
        one_time_tasks_object.add_one_time_task("Code for 4 hours", priority=4, weight=3)
        one_time_tasks_object.add_one_time_task("Study Japanese for 2 hours", priority=4, weight=3)
        one_time_tasks_object.add_one_time_task("Drink some Honey Tea", priority=0, weight=3)
        one_time_tasks_object.add_one_time_task("Drink some Hot Chocolate", priority=0, weight=3)

        return one_time_tasks_object

    # TODO: Figure out why this [0] is here
    def test_adding_one_time_tasks(self):
        sample_one_time_task_object = self.sample_tasks_1(self.initialize_one_time_task_object()[0])

        returned_output = sample_one_time_task_object.get_active_one_time_tasks()
        expected_output = self.read_test_data(test_data_path / 'active' / 'oneTimeTasks_simple_addition.json')

        assert self.check_equality_of_dict_of_task_dicts(returned_output,
                                                         expected_output)

    def test_adding_duplicate_one_time_tasks(self):
        initialized_one_time_tasks_object = self.initialize_one_time_task_object()[0]

        initialized_one_time_tasks_object.add_one_time_task("Fix This Shit Bug", priority=8, weight=3)
        initialized_one_time_tasks_object.add_one_time_task("Fix This Shit Bug", priority=8, weight=3)

        returned_output = initialized_one_time_tasks_object.get_active_one_time_tasks()
        expected_output = self.read_test_data(test_data_path / 'active' / 'oneTimeTasks_simple_duplicates.json')

        assert dictionary_operations_object.check_equality_of_dicts_of_task_dicts(returned_output, expected_output)

    def test_reusing_ids_marked_as_completed(self):
        sample_one_time_task_object = \
            self.sample_tasks_1(self.initialize_one_time_task_object()[0])

        sample_one_time_task_object.mark_task_as_completed('1')
        sample_one_time_task_object.add_one_time_task(task_string="Test All the existing code",
                                                      priority=4,
                                                      weight=3)

        returned_active_output = sample_one_time_task_object.get_active_one_time_tasks()
        returned_completed_output = sample_one_time_task_object.get_completed_one_time_tasks()

        expected_active_output = self.read_test_data(
            test_data_path / 'active' / 'oneTimeTasks_simple_mark_as_complete.json')

        expected_completed_output = self.read_test_data(
            test_data_path / 'completed' / 'oneTimeTasks_simple_mark_as_complete.json')

        condition1 = self.check_equality_of_dicts_of_task_dicts(expected_active_output,
                                                                returned_active_output)
        condition2 = self.check_equality_of_dicts_of_task_dicts(expected_completed_output,
                                                                returned_completed_output)

        assert condition1 and condition2

    def test_id_dictionary_after_simple_addition(self):
        initialized_one_time_object, initialized_data_input_operations_object = self.initialize_one_time_task_object()

        initialized_one_time_object.add_one_time_task(task_string="test1", priority=4, weight=3)
        initialized_one_time_object.add_one_time_task(task_string="test2", priority=4, weight=3)

        assert 2 == initialized_data_input_operations_object.get_new_unique_id_for_task(task_type='oneTimeTasks')

    def test_id_dictionary_after_marking_a_task_as_complete(self):
        initialized_one_time_object, initialized_data_input_operations_object = self.initialize_one_time_task_object()

        sample_one_time_task_object = self.sample_tasks_1(initialized_one_time_object)

        sample_one_time_task_object.mark_task_as_completed('1')

        next_id = initialized_data_input_operations_object.get_new_unique_id_for_task(task_type='oneTimeTasks')

        assert next_id == 1

    def test_delete_task(self):
        initialized_one_time_object, initialized_data_input_operations_object = self.initialize_one_time_task_object()

        sample_one_time_task_object = self.sample_tasks_1(initialized_one_time_object)

        sample_one_time_task_object.delete_task(id_to_delete='1')
        returned_active_output = sample_one_time_task_object.get_active_one_time_tasks()

        expected_active_output = self.read_test_data(
            test_data_path / 'active' / 'oneTimeTasks_simple_deletion.json')

        next_id = initialized_data_input_operations_object.get_new_unique_id_for_task(task_type='oneTimeTasks')

        assert next_id == 1 and \
            dictionary_operations_object.check_equality_of_dicts_of_task_dicts(returned_active_output,
                                                                               expected_active_output)




