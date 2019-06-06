from typing import List, Dict
import sys

# Custom Type Hints for Type Checking
StringList = List[str]
StringDict = Dict[str, str]


# TODO: figure out how to refresh tasks
class Habits:
    def __init__(self,
                 data_input_operations_object,
                 data_output_operations_object,
                 task_functions_object):

        self.DataInputOperationsObject = data_input_operations_object
        self.DataOutputOperations = data_output_operations_object
        self.TaskFunctionsObject = task_functions_object

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
            self.TaskFunctionsObject.add_tasks(task_string=task_string,
                                               task_type="habits",
                                               priority=priority,
                                               refresh_rate=refresh_rate)

    def update(self,
               id_to_update: int,
               option_to_update: str,
               updated_value: str):
        option_to_update = option_to_update.lower()

        try:
            # the conditions are being checked against lists because in the future,
            # we might need to include synonyms for the same actions
            if option_to_update in ["task_string", "task string", "taskstring", "habitstring", "habit_string", "habit"]:
                field_type = "taskString"
            elif option_to_update in ["weight"]:
                field_type = "weight"
            elif option_to_update in ["priority"]:
                field_type = "priority"
            elif option_to_update in ["scheduled_for", "scheduled", "due", "complete_by", "completeby", "by"]:
                # FIXME: implement this after implementing a general string to time conversion
                #        function in the time functions module
                raise NotImplementedError
            elif option_to_update in ["refresh_rate", "refreshrate"]:
                # FIXME: refresh rates hasn't been implemented yet properly
                raise NotImplementedError

            self.activeHabits = self.taskFunctions.update_values(id_to_edit=id_to_update,
                                                                 field_name=field_type,
                                                                 active_dictionary=self.active_one_time_tasks,
                                                                 updated_value=updated_value)
        except NotImplementedError as e:
            sys.exit("this feature hasn't been implemented yet")

    def delete_active(self,
                      id_to_delete: int) -> None:
        self.activeHabits = self.TaskFunctionsObject.delete_task(id_to_delete=id_to_delete,
                                                                 active_dictionary=self.activeHabits,
                                                                 task_type="habits")

    def delete_inactive(self,
                        id_to_delete: int) -> None:
        self.activeHabits = self.TaskFunctionsObject.delete_task(id_to_delete=id_to_delete,
                                                                 active_dictionary=self.inactiveHabits,
                                                                 task_type="habits")

    def mark_as_completed(self,
                          id_to_mark_as_completed: int) -> None:
        self.activeHabits, self.completedHabits = \
            self.TaskFunctionsObject.mark_tasks_as_completed(id_to_mark_as_completed=id_to_mark_as_completed,
                                                             active_dictionary=self.activeHabits,
                                                             completed_dictionary=self.completedHabits,
                                                             task_type="habits",
                                                             completed_task_type="")

    def mark_as_inactive(self,
                         id_to_mark_as_inactive: int) -> None:
        self.activeHabits, self.inactiveHabits = \
            self.TaskFunctionsObject.mark_tasks_as_completed(id_to_mark_as_completed=id_to_mark_as_inactive,
                                                             active_dictionary=self.activeHabits,
                                                             completed_dictionary=self.inactiveHabits,
                                                             task_type="habits",
                                                             completed_task_type="inactiveHabits")

    # TODO: implement this
    def unmark_inactive(self,
                        id_to_unmark: int):
        pass

    def save_active_habits(self) -> None:
        self.DataOutputOperations.save_as_file(task_status='active',
                                               task_type='habits',
                                               dictionary_to_save=self.activeHabits)

    def save_inactive_habits(self) -> None:
        self.DataOutputOperations.save_as_file(task_status='inactive',
                                               task_type='habits',
                                               dictionary_to_save=self.inactiveHabits)

    # GET operations

    def get_active(self) -> StringDict:
        return self.activeHabits

    def get_completed(self) -> StringDict:
        return self.completedHabits

    def get_inactive(self) -> StringDict:
        return self.inactiveHabits
