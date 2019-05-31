from src import OneTimeTasks
from src import DataInputOperations, DataOutputOperations
from src.operations import DictionaryOperations, ResolvePaths, TaskFunctions

import os
import json
import src
from pathlib import Path

import pytest

dictionary_operations = DictionaryOperations.DictionaryOperations()

test_data_path = Path(os.path.dirname(os.path.abspath(src.__file__))) / '..' / 'tests' / 'test_data'


class TestOneTimeTasks:
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
        data_output_operations_object = DataOutputOperations.DataOutputOperations(resolve_paths=resolve_paths_object,
                                                                                  dictionary_operations=dictionary_operations)

        # data_output_operations_object = \
        #     data_output_operations.DataOutputOperations(dictionary_operations.DictionaryOperations())

        task_functions_object = TaskFunctions.TaskFunctions(data_input_operations_object)

        one_time_tasks_object = OneTimeTasks.OneTimeTasks(data_input_operations_object=data_input_operations_object,
                                                          data_output_operations_object=data_output_operations_object,
                                                          task_functions_object=task_functions_object,
                                                          active_one_time_tasks={},
                                                          completed_one_time_tasks={})

        return one_time_tasks_object, data_input_operations_object

    @staticmethod
    def sample_tasks_1(one_time_tasks_object):
        one_time_tasks_object.add("Fix This Shit Bug", priority=8, weight=3)
        one_time_tasks_object.add("Code for 4 hours", priority=4, weight=3)
        one_time_tasks_object.add("Study Japanese for 2 hours", priority=4, weight=3)
        one_time_tasks_object.add("Drink some Honey Tea", priority=0, weight=3)
        one_time_tasks_object.add("Drink some Hot Chocolate", priority=0, weight=3)

        return one_time_tasks_object

    def test_adding_one_time_tasks(self):
        sample_one_time_task_object = self.sample_tasks_1(self.initialize_one_time_task_object()[0])

        returned_output = sample_one_time_task_object.get_active_one_time_tasks()
        expected_output = self.read_test_data(test_data_path / 'active' / 'oneTimeTasks_simple_addition.json')

        assert dictionary_operations.check_equality_of_dicts_with_nested_task_dicts(returned_output,
                                                                                    expected_output)

    def test_adding_duplicate_one_time_tasks(self):
        initialized_one_time_tasks_object = self.initialize_one_time_task_object()[0]

        initialized_one_time_tasks_object.add("Fix This Shit Bug", priority=8, weight=3)
        initialized_one_time_tasks_object.add("Fix This Shit Bug", priority=8, weight=3)

        returned_output = initialized_one_time_tasks_object.get_active_one_time_tasks()
        expected_output = self.read_test_data(test_data_path / 'active' / 'oneTimeTasks_simple_duplicates.json')

        assert dictionary_operations.check_equality_of_dicts_with_nested_task_dicts(returned_output,
                                                                                    expected_output)

    def test_reusing_ids_marked_as_completed(self):
        sample_one_time_task_object = \
            self.sample_tasks_1(self.initialize_one_time_task_object()[0])

        sample_one_time_task_object.mark_as_completed(1)
        sample_one_time_task_object.add(task_string="Test All the existing code",
                                        priority=4,
                                        weight=3)

        returned_active_output = sample_one_time_task_object.get_active_one_time_tasks()
        returned_completed_output = sample_one_time_task_object.get_completed_one_time_tasks()

        expected_active_output = self.read_test_data(
            test_data_path / 'active' / 'oneTimeTasks_simple_mark_as_complete.json')

        expected_completed_output = self.read_test_data(
            test_data_path / 'completed' / 'oneTimeTasks_simple_mark_as_complete.json')

        assert dictionary_operations.check_equality_of_dicts_with_nested_task_dicts(expected_active_output,
                                                                                    returned_active_output)
        assert dictionary_operations.check_equality_of_dicts_with_nested_task_dicts(
            dict1=expected_completed_output,
            dict2=returned_completed_output)

    def test_id_dictionary_after_simple_addition(self):
        initialized_one_time_object, initialized_data_input_operations_object = self.initialize_one_time_task_object()

        initialized_one_time_object.add(task_string="test1", priority=4, weight=3)
        initialized_one_time_object.add(task_string="test2", priority=4, weight=3)

        assert 2 == initialized_data_input_operations_object.get_new_unique_id_for_task(task_type='oneTimeTasks')

    def test_id_dictionary_after_marking_a_task_as_complete(self):
        initialized_one_time_object, initialized_data_input_operations_object = self.initialize_one_time_task_object()

        sample_one_time_task_object = self.sample_tasks_1(initialized_one_time_object)

        sample_one_time_task_object.mark_as_completed(1)

        next_id = initialized_data_input_operations_object.get_new_unique_id_for_task(task_type='oneTimeTasks')

        assert next_id == 1

    def test_marking_multiple_tasks_as_completed(self):
        initialized_one_time_object, initialized_data_input_operations_object = self.initialize_one_time_task_object()

        sample_one_time_task_object = self.sample_tasks_1(initialized_one_time_object)

        sample_one_time_task_object.mark_as_completed(list_of_ids_to_mark_as_completed=[0, 1])

        returned_active_output = sample_one_time_task_object.get_active_one_time_tasks()
        returned_completed_output = sample_one_time_task_object.get_completed_one_time_tasks()

        expected_active_output = self.read_test_data(
            test_data_path / 'active' / 'oneTimeTasks_marking_multiple_as_complete.json')

        expected_completed_output = self.read_test_data(
            test_data_path / 'completed' / 'oneTimeTasks_marking_multiple_as_complete.json')

        assert dictionary_operations.check_equality_of_dicts_with_nested_task_dicts(expected_active_output,
                                                                                    returned_active_output)
        assert dictionary_operations.check_equality_of_dicts_with_nested_task_dicts(expected_completed_output,
                                                                                    returned_completed_output)

        for x in [0, 1]:
            assert x == initialized_data_input_operations_object.get_new_unique_id_for_task(task_type="oneTimeTasks")

        assert 5 == initialized_data_input_operations_object.get_new_unique_id_for_task(task_type="oneTimeTasks")
        assert 2 == initialized_data_input_operations_object.get_new_unique_id_for_task(
            task_type="completedOneTimeTasks")

    def test_delete_active_tasks_task(self):
        initialized_one_time_object, initialized_data_input_operations_object = self.initialize_one_time_task_object()

        sample_one_time_task_object = self.sample_tasks_1(initialized_one_time_object)

        sample_one_time_task_object.delete_active_tasks(id_to_delete='1')
        returned_active_output = sample_one_time_task_object.get_active_one_time_tasks()

        expected_active_output = self.read_test_data(
            test_data_path / 'active' / 'oneTimeTasks_simple_deletion.json')

        next_id = initialized_data_input_operations_object.get_new_unique_id_for_task(task_type='oneTimeTasks')

        assert next_id == 1 and dictionary_operations.check_equality_of_dicts_with_nested_task_dicts(
            dict1=returned_active_output,
            dict2=expected_active_output)

    def test_unmarking_a_completed_task(self):
        initialized_one_time_tasks_object, initialized_data_input_operations = self.initialize_one_time_task_object()
        sample_one_time_task_object = self.sample_tasks_1(initialized_one_time_tasks_object)

        sample_one_time_task_object.mark_as_completed(1)
        sample_one_time_task_object.unmark_completed(0)

        returned_active_output = sample_one_time_task_object.get_active_one_time_tasks()
        returned_completed_output = sample_one_time_task_object.get_completed_one_time_tasks()

        expected_active_output = self.read_test_data(
            test_data_path / 'active' / 'oneTimeTasks_simple_addition.json')

        length_of_expected_completed_output = 0

        assert dictionary_operations.check_equality_of_dicts_with_nested_task_dicts(expected_active_output,
                                                                                    returned_active_output)
        assert len(returned_completed_output) == length_of_expected_completed_output

        assert initialized_data_input_operations.get_new_unique_id_for_task(task_type="completedOneTimeTasks") == 0

        assert initialized_data_input_operations.get_new_unique_id_for_task(task_type="oneTimeTasks") == 5

    def test_unmarking_multiple_completed_tasks_in_reverse_order(self):
        initialized_one_time_tasks_object, initialized_data_input_operations = self.initialize_one_time_task_object()
        sample_one_time_task_object = self.sample_tasks_1(initialized_one_time_tasks_object)

        sample_one_time_task_object.mark_as_completed(1)
        sample_one_time_task_object.mark_as_completed(2)

        # unmarking tasks out of order, so that their position is reversed in the active tasks dictionary
        sample_one_time_task_object.unmark_completed(1)
        sample_one_time_task_object.unmark_completed(0)

        returned_active_output = sample_one_time_task_object.get_active_one_time_tasks()
        returned_completed_output = sample_one_time_task_object.get_completed_one_time_tasks()

        expected_active_output = \
            self.read_test_data(test_data_path / 'active' / 'oneTimeTasks_unmarking_out_of_order.json')

        assert dictionary_operations.check_equality_of_dicts_with_nested_task_dicts(expected_active_output,
                                                                                    returned_active_output)
        assert len(returned_completed_output) == 0

        assert 0 == initialized_data_input_operations.get_new_unique_id_for_task(task_type="completedOneTimeTasks")
        assert 5 == initialized_data_input_operations.get_new_unique_id_for_task(task_type="oneTimeTasks")

    def test_raise_exception_when_invalid_key_is_marked_as_completed(self):
        initialized_one_time_task_object = self.initialize_one_time_task_object()[0]

        with pytest.raises(KeyError):
            initialized_one_time_task_object.mark_as_completed(0)

    def test_raise_exception_when_invalid_key_is_unmarked(self):
        initialized_one_time_task_object = self.initialize_one_time_task_object()[0]

        with pytest.raises(KeyError):
            initialized_one_time_task_object.unmark_completed(0)

    def test_raise_exception_when_deleting_unavailable_task_key(self):
        initialized_one_time_task_object = self.initialize_one_time_task_object()[0]

        with pytest.raises(KeyError):
            initialized_one_time_task_object.delete_active_tasks(0)

    def test_clearing_all_completed_tasks(self):
        initialized_one_time_object, initialized_data_input_operations_object = self.initialize_one_time_task_object()
        sample_one_time_task_object = self.sample_tasks_1(initialized_one_time_object)

        sample_one_time_task_object.mark_as_completed(list_of_ids_to_mark_as_completed=[0, 1])

        sample_one_time_task_object.delete_all_completed_tasks()

        assert initialized_data_input_operations_object.get_new_unique_id_for_task("completedOneTimeTasks") == 0
        assert len(sample_one_time_task_object.get_completed_one_time_tasks()) == 0

    # TODO: implement deleting completed tasks
    # TODO: implement requesting more than one unqiue ids
