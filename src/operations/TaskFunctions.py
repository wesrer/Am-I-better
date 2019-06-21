import datetime
import sys
from src.operations import DictionaryOperations

from typing import List, Dict

# Custom Type Hints for Type Checking
StringList = List[str]
StringDict = Dict[str, str]


# TODO: implement complete_by parameters
class TaskFunctions:
    # TODO: figure out how to Type Cast Custom Objects
    def __init__(self, data_input_operations_object):
        self.DataInputOperations = data_input_operations_object
        self.DictionaryOperations = DictionaryOperations.DictionaryOperations()
        self.today = datetime.datetime.now()

    # FIXME: implement this
    def convert_time_string_to_dictionary(self,
                                          time_string: str) -> StringDict:
        pass

    # FUNCTION PURPOSE:
    #   Add tasks to the three primary categories of active tasks
    #
    # FUNCTION PARAMETERS:
    #   - task_String: The actual task that the user wants to do
    #   - task_type: "oneTimeTasks" or "habits" or "longTermProjects"
    #   - priority: Adds variable priorities to different tasks
    #   - complete_by: A specific deadline for the particular task (doesn't apply to habits)
    #   - refresh_rate: The rate at which

    # TODO: add the custom default values implementation
    # TODO: figure out how the refresh rate works

    def add_tasks(self,
                  task_string: str,
                  task_type: str,
                  priority: int = 0,
                  weight: int = 3,
                  scheduled_start=False,  # TODO: add type casting
                  complete_by: str = "N/A",
                  refresh_rate: int = 1) -> StringDict:

        if not scheduled_start:
            scheduled_start = self.today

        # By default, all tasks need to be completed by 24 hours of their scheduled start
        if task_type == "oneTimeTasks":
            complete_by = scheduled_start + datetime.timedelta(hours=24)

            # formatting the string
            complete_by = complete_by.strftime("%c")

        elif task_type == "longTermProjects":
            complete_by = scheduled_start + datetime.timedelta(years=1)

        # make a JSON object to append to the existing list
        data_dict = {
            "taskString": task_string,
            "weight": str(weight),
            "assignedOn": self.today.strftime("%c"),
            "scheduledStart": scheduled_start.strftime("%c"),
            "priority": str(priority),
        }

        if task_type == 'oneTimeTasks':
            data_dict["completeBy"] = complete_by
        elif task_type == 'habits':
            data_dict["refreshRate"] = str(refresh_rate)

        return data_dict

    # FUNCTION PARAMETERS:
    #   - task_dictionary: The already existing dictionary of the parent task
    #                      to which the task will be added
    #   - sub_task_string: The task which is going to be added
    # FUNCTION PURPOSE

    # TODO
    def add_sub_tasks(self,
                      task_dictionary: StringDict,
                      sub_task_string: str,
                      priority: int = 0,
                      complete_by: bool = False) -> StringDict:
        pass

    # TODO: this is a really inefficient way of doing this. Needs refactoring to more efficiently handle lists
    def mark_tasks(self,
                   active_dictionary: StringDict,
                   completed_dictionary: StringDict,
                   task_type: str,
                   completed_task_type: str,
                   parent_id: int = -1,
                   has_children: bool = False,
                   id_to_mark: int = -1,
                   list_of_ids_to_mark: List[int] = [], ) -> [StringDict, StringDict]:

        if len(list_of_ids_to_mark) == 0:
            return self.mark_one_task(id_to_mark=id_to_mark,
                                      active_dictionary=active_dictionary,
                                      completed_dictionary=completed_dictionary,
                                      task_type=task_type,
                                      completed_task_type=completed_task_type,
                                      parent_id=parent_id,
                                      has_children=has_children)

        else:
            for x in list_of_ids_to_mark:
                active_dictionary, completed_dictionary = \
                    self.mark_one_task(id_to_mark=x,
                                       active_dictionary=active_dictionary,
                                       completed_dictionary=completed_dictionary,
                                       task_type=task_type,
                                       completed_task_type=completed_task_type,
                                       parent_id=parent_id,
                                       has_children=has_children)

            return active_dictionary, completed_dictionary

    # Moves Task From Active Dictionary to Completed Dictionary
    # and adjusts ids to reflect this task

    # FIXME: implement parent-child relationships, because they are clearly
    #        not working
    # TODO: allow multiple tasks to be marked as completed in one function call
    def mark_one_task(self,
                      active_dictionary: StringDict,
                      completed_dictionary: StringDict,
                      task_type: str,
                      completed_task_type: str,
                      id_to_mark: int = -1,
                      parent_id: int = -1,
                      has_children: bool = False) -> [StringDict, StringDict]:

        id_to_mark = str(id_to_mark)

        try:
            if id_to_mark not in active_dictionary:
                raise KeyError

            unique_id = self.DataInputOperations.get_new_unique_id_for_task(task_type=completed_task_type,
                                                                            parent_id=parent_id,
                                                                            has_children=has_children)

            completed_dictionary[str(unique_id)] = active_dictionary[id_to_mark]

            self.DataInputOperations.mark_id_as_available(task_type=task_type,
                                                          parent_id=parent_id,
                                                          has_children=has_children,
                                                          id_to_mark_as_available=id_to_mark)

            del active_dictionary[id_to_mark]
        except KeyError as e:
            sys.exit(f"{id_to_mark} for {task_type} does not exist")

        return active_dictionary, completed_dictionary

    # TODO: implement parent_id and has_children functionalities
    # TODO: allow multiple ids to be unmarked in one call
    def unmark_completed_tasks(self,
                               list_of_ids_to_unmark: List[int],
                               active_dictionary: StringDict,
                               completed_dictionary: StringDict,
                               task_type: str,
                               completed_task_type: str,
                               parent_id: int = -1,
                               has_children: bool = False):

        for id_to_unmark in list_of_ids_to_unmark:

            id_to_unmark = str(id_to_unmark)

            if id_to_unmark not in completed_dictionary:
                raise KeyError

            unique_id = self.DataInputOperations.get_new_unique_id_for_task(task_type=task_type,
                                                                            parent_id=parent_id,
                                                                            has_children=has_children)

            # pushing the string to the active_dictionary under a next available id
            active_dictionary[str(unique_id)] = completed_dictionary[id_to_unmark]

            self.DataInputOperations.mark_id_as_available(task_type=completed_task_type,
                                                          parent_id=parent_id,
                                                          has_children=has_children,
                                                          id_to_mark_as_available=id_to_unmark)

            del completed_dictionary[id_to_unmark]

        return active_dictionary, completed_dictionary

    def unmark_all_completed_habits(self,
                                    active_dictionary: StringDict,
                                    completed_dictionary: StringDict):

        for key, value in completed_dictionary.items():
            active_dictionary[key] = value
            self.DataInputOperations.mark_id_as_unavailable(task_type='habits',
                                                            id_to_mark_as_unavailable=key)
            del completed_dictionary[key]

        return active_dictionary, completed_dictionary

    # FIXME: Okay, this is not a primary concern, but it sucks that you have
    #        to send all of this excess data just because you are calling the
    #        markIDAsAvailable function
    def delete_tasks(self,
                     list_of_ids_to_delete: List[int],
                     active_dictionary: StringDict,
                     task_type: str,
                     parent_id: int = -1,
                     has_children: bool = False) -> StringDict:
        try:
            for id_to_delete in list_of_ids_to_delete:
                id_to_delete = str(id_to_delete)

                if id_to_delete not in active_dictionary:
                    raise KeyError

                del active_dictionary[id_to_delete]

                self.DataInputOperations.mark_id_as_available(task_type=task_type,
                                                              id_to_mark_as_available=id_to_delete,
                                                              has_children=has_children,
                                                              parent_id=parent_id)
        except KeyError as e:
            sys.exit(f"No {task_type} correspond to id {id_to_delete}")

        return active_dictionary

    @staticmethod
    def update_values(id_to_edit: int,
                      active_dictionary: StringDict,
                      updated_value: str,
                      field_name: str,
                      parent_id: int = -1,
                      has_children: bool = False):

        # TODO: figure out if we need parent_id and has_children
        active_dictionary[str(id_to_edit)][field_name] = updated_value
        return active_dictionary

    # TODO: implement this
    def sort_by_weight(self,
                       active_dictionary: StringDict) -> StringDict:
        self.DictionaryOperations.dict_of_dicts_to_list_of_dicts()
        self.DictionaryOperations.sort_list_of_dictionaries_by_key()

    # TODO: have some sort of warning before the actual execution of this, since this cannot be
    #       undone
    def clearing_all_tasks(self,
                           task_type: str):
        self.DataInputOperations.reset_ids(task_type=task_type,
                                           reset_available=True,
                                           reset_next=True)
        return {}  # this is the value the dictionary is going to be reset to
