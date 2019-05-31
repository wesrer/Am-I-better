from typing import List, Dict

# Custom Type Hints for Type Checking
StringList = List[str]
StringDict = Dict[str, str]


# TODO: figure out how to refresh tasks
class Habits:
    def __init__(self,
                 data_input_operations_object,
                 task_functions_object):

        self.DataInputOperationsObject = data_input_operations_object;
        self.TaskFunctionsObject = task_functions_object

        self.activeHabits = \
            self.DataInputOperationsObject.get_tasks(task_status='active',
                                                     task_type='habits')
        self.inactiveHabits = \
            self.DataInputOperationsObject.get_tasks(task_status='inactive',
                                                     task_type='habits')

    # FIXME: add the custom default values implementation
    def add(self,
            habit_string: str,
            priority: int = 0,
            refresh_rate: int = 1) -> None:

        unqiue_id = self.DataInputOperationsObject.get_new_unique_id_for_task(task_type='habits')

        self.activeHabits[str(unqiue_id)] = \
            self.TaskFunctionsObject.add_tasks(task_string=habit_string,
                                               task_type="habits",
                                               priority=priority,
                                               refresh_rate=refresh_rate)

    def delete(self,
               id_to_delete: int) -> None:
        self.activeHabits = \
            self.TaskFunctionsObject.delete(id_to_delete=id_to_delete,
                                            active_dictionary=self.activeHabits,
                                            task_type="habits")

    def mark_as_inactive(self,
                         id_to_mark_as_inactive: int) -> None:
        self.activeHabits, self.inactiveHabits = \
            self.TaskFunctionsObject.mark_task_as_completed(id_to_mark_as_completed=id_to_mark_as_inactive,
                                                            active_dictionary=self.activeHabits,
                                                            completed_dictionary=self.inactiveHabits,
                                                            task_type="habits",
                                                            completed_task_type="inactiveHabits")

    # TODO: implement this
    def unmark_inactive(self,
                        id_to_unmark: int):
        pass

    def save_active_habits(self) -> None:
        self.DataInputOperationsObject.save_as_file(task_status='active',
                                                    task_type='habits',
                                                    dictionary_to_save=self.activeHabits)

    def save_inactive_habits(self) -> None:
        self.DataInputOperationsObject.save_as_file(task_status='inactive',
                                                    task_type='habits',
                                                    dictionary_to_save=self.inactiveHabits)

    # GET operations

    def get_active_habits(self) -> StringDict:
        return self.activeHabits

    def get_inactive_habits(self) -> StringDict:
        return self.inactiveHabits
