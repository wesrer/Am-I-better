from src.operations.UserInputParser import UserInputParser
from src.operations.DictionaryOperations import DictionaryOperations

UserInputParser = UserInputParser()
DictionaryOperations = DictionaryOperations()


class TestUserInputParser:
    def test_parsing_ids_joined_with_commas_no_space_with_property_and_value_after(self):
        # this input mirrors the input when people are updating more than one value
        # ex: `aib habit update 0,6 weight:1`
        user_input = ((0, 6), 'weight:1')

        expected_output = ['0', '6']
        assert UserInputParser.generate_list_of_ids(user_input) == expected_output

    def test_parsing_ids_joined_with_commas_no_space_with_string_after(self):
        # this input mirrors the input when people are updating more than one value
        # ex: `aib habit update 0,6 weight:1`
        user_input = ((0, 6), 'this', 'is', 'a', 'new', 'string')

        expected_output = ['0', '6']
        assert UserInputParser.generate_list_of_ids(user_input) == expected_output

    def test_parsing_ids_joined_with_commas_and_space_with_property_and_value_after(self):
        # this input mirrors the input when people are updating more than one value
        # ex: `aib habit update 0, 6 weight:1`
        user_input = ((0,), 6, 'weight:1')

        expected_output = ['0', '6']
        assert UserInputParser.generate_list_of_ids(user_input) == expected_output

    def test_parsing_ids_joined_with_commas_and_space_with_string_after(self):
        # this input mirrors the input when people are updating more than one value
        # ex: `aib habit update 0, 6 weight:1`
        user_input = ((0,), 6, 'this', 'is', 'a', 'new', 'string')

        expected_output = ['0', '6']
        assert UserInputParser.generate_list_of_ids(user_input) == expected_output

    def test_parsing_ids_joined_with_space_with_property_and_value_after(self):
        # this input mirrors the input when people are updating more than one value
        # ex: `aib habit update 0 6 weight:1`
        user_input = (0, 6, 'weight:1')

        expected_output = ['0', '6']
        assert UserInputParser.generate_list_of_ids(user_input) == expected_output

    def test_parsing_ids_joined_with_space_with_string_after(self):
        # this input mirrors the input when people are updating more than one value
        # ex: `aib habit update 0 6 weight:1`
        user_input = (0, 6, 'this', 'is', 'a', 'new', 'string')

        expected_output = ['0', '6']
        assert UserInputParser.generate_list_of_ids(user_input) == expected_output

    def test_parsing_only_one_id_with_no_string_after(self):
        # this is the most common input type, used for almost every action
        user_input = (5,)

        expected_output = ['5']
        assert UserInputParser.generate_list_of_ids(user_input) == expected_output

    def test_parsing_only_one_id_with_property_and_value_after(self):
        user_input = (5, 'weight:1')

        expected_output = ['5']
        assert UserInputParser.generate_list_of_ids(user_input) == expected_output

    def test_parsing_only_one_id_with_task_string_after(self):
        user_input = (5, 'this', 'is', 'a', 'new', 'string')

        expected_output = ['5']
        assert UserInputParser.generate_list_of_ids(user_input) == expected_output

    def test_parsing_ids_joined_with_commas_no_space_with_string_with_replicated_number_after(self):
        # this input mirrors the input when people are updating more than one value
        # ex: `aib habit update 0,6 weight:1`
        user_input = ((0, 6), 'buy', 6, 'chocolates')

        expected_output = ['0', '6']
        assert UserInputParser.generate_list_of_ids(user_input) == expected_output

    def test_generating_task_string_with_numbers(self):
        user_input = (0, 'Drink', 2, 'litres', 'of', 'water')

        expected_output = 'Drink 2 litres of water'

        assert UserInputParser.generate_task_string(args=user_input) == expected_output

    def test_generating_task_string_with_numbers_and_properties(self):
        user_input = (0, 'Drink', 2, 'litres', 'of', 'water', 'priority:5')

        expected_output = 'Drink 2 litres of water'

        assert UserInputParser.generate_task_string(args=user_input) == expected_output

    def test_generating_properties_when_properties_after_string(self):
        user_input = (0, 'Drink', 2, 'litres', 'of', 'water', 'priority:5', 'weight:6')

        expected_output = {
            'priority': '5',
            'weight': '6'
        }

        returned_output = UserInputParser.find_properties(args=user_input)

        assert DictionaryOperations.check_task_dictionary_equality(returned_output, expected_output)

    def test_generating_properties_when_properties_before_and_after_string(self):
        user_input = (0, 'priority:5', 'Drink', 2, 'litres', 'of', 'water', 'weight:6')

        expected_output = {
            'priority': '5',
            'weight': '6'
        }

        returned_output = UserInputParser.find_properties(args=user_input)

        assert DictionaryOperations.check_task_dictionary_equality(returned_output, expected_output)

