from typing import List, Dict
from datetime import datetime

import sys

# Custom Type Hints for Type Checking
StringList = List[str]
StringDict = Dict[str, str]


class Habits:
    def __init__(self,
                 data_input_operations_object,
                 data_output_operations_object,
                 task_functions_object,
                 time_operations_object):

        self.DataInputOperationsObject = data_input_operations_object
        self.DataOutputOperations = data_output_operations_object
        self.TaskFunctions = task_functions_object
        self.TimeOperations = time_operations_object

        self.activeHabits = self.DataInputOperationsObject.get_tasks(task_status='active',
                                                                     task_type='habits')

        self.completedHabits = self.DataInputOperationsObject.get_tasks(task_status='completed',
                                                                        task_type='habits')

        self.inactiveHabits = self.DataInputOperationsObject.get_tasks(task_status='inactive',
                                                                       task_type='habits')

    # FIXME: add the custom default values implementation
    def add(self,
            task_string: str,
            priority: int = 0,
            refresh_rate: int = 1) -> None:

        unqiue_id = self.DataInputOperationsObject.get_new_unique_id_for_task(task_type='habits')

        self.activeHabits[str(unqiue_id)] = \
            self.TaskFunctions.add_tasks(task_string=task_string,
                                         task_type="habits",
                                         priority=priority,
                                         refresh_rate=refresh_rate)

    def update(self,
               id_to_update: int,
               option_to_update: str,
               updated_value: str) -> None:
        option_to_update = option_to_update.lower()

        try:
            field_type = ""
            # the conditions are being checked against lists because in the future,
            # we might need to include synonyms for the same actions
            if option_to_update in ["task_string", "task string", "taskstring", "habitstring", "habit_string", "habit"]:
                field_type = "taskString"
            elif option_to_update in ["weight", "w", "wt"]:
                field_type = "weight"
            elif option_to_update in ["priority", "pri", "prio"]:
                field_type = "priority"
            elif option_to_update in ["scheduled_for", "scheduled", "due", "complete_by", "completeby", "by"]:
                # FIXME: implement this after implementing a general string to time conversion
                #        function in the time functions module
                raise NotImplementedError
            elif option_to_update in ["refresh_rate", "refreshrate"]:
                field_type = "refreshRate"
            else:
                raise ValueError

            self.activeHabits = self.TaskFunctions.update_values(id_to_edit=id_to_update,
                                                                 field_name=field_type,
                                                                 active_dictionary=self.activeHabits,
                                                                 updated_value=updated_value)
        except NotImplementedError as e:
            sys.exit("this feature hasn't been implemented yet")
        except ValueError as e:
            sys.exit(f"{option_to_update} is not a recognized property and cannot be updated")

    def delete_from_queue(self,
                          queue: str,
                          list_of_ids_to_delete: List[int]) -> None:
        try:
            if queue in ["active"]:
                queue_dict = self.activeHabits
            elif queue in ["inactive"]:
                queue_dict = self.inactiveHabits
            elif queue in ["completed"]:
                queue_dict = self.completedHabits
            else:
                raise ValueError

            queue_dict = self.TaskFunctions.delete_tasks(list_of_ids_to_delete=list_of_ids_to_delete,
                                                         active_dictionary=queue_dict,
                                                         task_type="habits")
        except ValueError as e:
            sys.exit(f"{queue} is not a recognized Habit queue")

    def mark_as_completed(self,
                          list_of_ids_to_mark_as_completed: List[int]) -> None:

        for x in list_of_ids_to_mark_as_completed:
            self.activeHabits[str(x)]["lastCompletedOn"] = datetime.now().strftime("%c")

        self.activeHabits, self.completedHabits = \
            self.TaskFunctions.mark_tasks(list_of_ids_to_mark=list_of_ids_to_mark_as_completed,
                                          active_dictionary=self.activeHabits,
                                          completed_dictionary=self.completedHabits,
                                          task_type="habits",
                                          completed_task_type="completedHabits")

    def mark_as_inactive(self,
                         list_of_ids_to_mark_as_inactive: List[int]) -> None:
        self.activeHabits, self.inactiveHabits = \
            self.TaskFunctions.mark_tasks(list_of_ids_to_mark=list_of_ids_to_mark_as_inactive,
                                          active_dictionary=self.activeHabits,
                                          completed_dictionary=self.inactiveHabits,
                                          task_type="habits",
                                          completed_task_type="inactiveHabits")

    def refresh_habits(self) -> None:
        habits_to_unmark = []
        for key, value in self.completedHabits.items():
            if not self.TimeOperations.is_still_valid(last_completed_on=value["lastCompletedOn"],
                                                      refresh_rate=int(value["refreshRate"])):
                habits_to_unmark.append(key)

        if len(habits_to_unmark) != 0:
            self.unmark(list_of_ids_to_unmark=habits_to_unmark,
                        unmark_to_queue="active",
                        unmark_from_queue="completed")

    def find_next_refresh_on(self) -> datetime:
        pass

    def unmark(self,
               list_of_ids_to_unmark: List[int],
               unmark_from_queue: str,
               unmark_to_queue: str = "active") -> None:

        try:
            if unmark_from_queue in ["active"]:
                raise KeyError

            unmark_from_queue = self.get_queue(queue=unmark_from_queue)
            unmark_to_queue = self.get_queue(queue=unmark_to_queue)


            unmark_to_queue, unmark_from_queue = \
                self.TaskFunctions.unmark(list_of_ids_to_unmark=list_of_ids_to_unmark,
                                          unmark_to=unmark_to_queue,
                                          unmark_from=unmark_from_queue,
                                          task_type="habits",
                                          completed_task_type="completedHabits")
        except KeyError as e:
            sys.exit(f"Cannot unmark from active queue.")

    def unmark_inactive(self,
                        list_of_ids_to_unmark: List[int]) -> None:
        self.unmark(list_of_ids_to_unmark=list_of_ids_to_unmark,
                    dictionary_to_unmark_from=self.inactiveHabits)

    def unmark_completed(self,
                         list_of_ids_to_unmark: List[int]) -> None:
        self.unmark(list_of_ids_to_unmark=list_of_ids_to_unmark,
                    dictionary_to_unmark_from=self.completedHabits)

    def clear_all_tasks_from_queue(self,
                                   queue: str):
        try:
            # TODO: issue a statment of warning about deleting all tasks
            if queue in ["completed"]:
                self.completedHabits = self.taskFunctions.clearing_all_tasks(task_type="completedHabits")
            elif queue in ["inactive"]:
                self.inactiveHabits = self.taskFunctions.clearing_all_tasks(task_type="inactiveHabits")
            elif queue in ["active"]:
                raise NotImplementedError
            else:
                raise ValueError

        except ValueError as e:
            sys.exit(f"{queue} is not a valid queue to delete")
        except NotImplementedError as e:
            sys.exit(f"Deleting all active habits hasn't been implemented yet, "
                     f"because recovery options haven't been implemented either.")

    def save_habit_queues(self) -> None:
        self.DataOutputOperations.save_as_file(task_status='active',
                                               task_type='habits',
                                               dictionary_to_save=self.activeHabits)

        self.DataOutputOperations.save_as_file(task_status='inactive',
                                               task_type='habits',
                                               dictionary_to_save=self.inactiveHabits)

        self.DataOutputOperations.save_as_file(task_status='completed',
                                               task_type='habits',
                                               dictionary_to_save=self.completedHabits)

    # GET operations

    def get_queue(self,
                  queue:str):
        try:
            if queue in ["active"]:
                return self.activeHabits
            elif queue in ["inactive"]:
                return self.inactiveHabits
            elif queue in ["completed"]:
                return self.completedHabits
            else:
                raise ValueError
        except ValueError as e:
            sys.exit(f"{queue} is not a recognized queue type for habits")
