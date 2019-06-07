from typing import List, Dict

# TODO: figure out how to Type Cast Custom Objects
# Custom Type Hints for Type Checking
StringList = List[str]
StringDict = Dict[str, str]


# FIXME: separate data_output_operations
class OneTimeTasks:

    def __init__(self,
                 data_input_operations_object,
                 data_output_operations_object,
                 task_functions_object,
                 active_one_time_tasks: StringDict,
                 completed_one_time_tasks: StringDict):

        self.DataInputOperations = data_input_operations_object
        self.DataOutputOperations = data_output_operations_object
        self.taskFunctions = task_functions_object

        self.completed_one_time_tasks = completed_one_time_tasks
        self.active_one_time_tasks = active_one_time_tasks

        self.default_time_values = self.DataInputOperations.get_default_values("time", "oneTimeTasks")

    # FIXME: figure out how to take customized completeBy input
    def add(self,
            task_string: str,
            priority: int = 0,
            weight: int = 3,
            complete_by: str = "defaultValue") -> None:

        unique_id = self.DataInputOperations.get_new_unique_id_for_task('oneTimeTasks')
        unique_id = str(unique_id)  # for easier JSON conversion

        if complete_by == "defaultValue":
            complete_by = self.default_time_values
        else:
            complete_by = self.taskFunctions.convert_time_string_to_dictionary(complete_by)

        self.active_one_time_tasks[unique_id] = self.taskFunctions.add_tasks(task_string=task_string,
                                                                             task_type="oneTimeTasks",
                                                                             priority=priority,
                                                                             weight=weight,
                                                                             complete_by=complete_by)

    def update(self,
               id_to_update: int,
               option_to_update: str,
               updated_value: str):
        option_to_update = option_to_update.lower()

        # the conditions are being checked against lists because in the future,
        # we might need to include synonyms for the same actions
        if option_to_update in ["task_string", "task string"]:
            field_type = "taskString"
        elif option_to_update in ["weight"]:
            field_type = "weight"
        elif option_to_update in ["priority"]:
            field_type = "priority"
        elif option_to_update in ["scheduled_for", "scheduled", "due", "complete_by", "completeby", "by"]:
            # FIXME: implement this after implementing a general string to time conversion
            #        function in the time functions module
            pass

        self.active_one_time_tasks = self.taskFunctions.update_values(id_to_edit=id_to_update,
                                                                      field_name=field_type,
                                                                      active_dictionary=self.active_one_time_tasks,
                                                                      updated_value=updated_value)

    def mark_as_completed(self,
                          id_to_mark_as_completed: int = -1,
                          list_of_ids_to_mark_as_completed: List[int] = []) -> None:

        if len(list_of_ids_to_mark_as_completed) != 0:
            self.active_one_time_tasks, self.completed_one_time_tasks = self.taskFunctions.mark_tasks_as_completed(
                list_of_ids_to_mark_as_completed=list_of_ids_to_mark_as_completed,
                active_dictionary=self.active_one_time_tasks,
                completed_dictionary=self.completed_one_time_tasks,
                task_type="oneTimeTasks",
                completed_task_type="completedOneTimeTasks")
        else:
            self.active_one_time_tasks, self.completed_one_time_tasks = \
                self.taskFunctions.mark_tasks_as_completed(id_to_mark_as_completed=id_to_mark_as_completed,
                                                           active_dictionary=self.active_one_time_tasks,
                                                           completed_dictionary=self.completed_one_time_tasks,
                                                           task_type="oneTimeTasks",
                                                           completed_task_type="completedOneTimeTasks")

    def unmark_completed(self, id_to_unmark: int) -> None:

        self.active_one_time_tasks, self.completed_one_time_tasks = \
            self.taskFunctions.unmark_a_completed_task(id_to_unmark=id_to_unmark,
                                                       active_dictionary=self.active_one_time_tasks,
                                                       completed_dictionary=self.completed_one_time_tasks,
                                                       task_type="oneTimeTasks",
                                                       completed_task_type="completedOneTimeTasks")

    def delete_active(self, list_of_ids_to_delete: List[int]) -> None:

        self.active_one_time_tasks = self.taskFunctions.delete_tasks(list_of_ids_to_delete=list_of_ids_to_delete,
                                                                     active_dictionary=self.active_one_time_tasks,
                                                                     task_type='oneTimeTasks')

    def delete_completed(self, list_of_ids_to_delete: List[int]) -> None:
        self.completed_one_time_tasks = self.taskFunctions.delete_tasks(ist_of_ids_to_delete=list_of_ids_to_delete,
                                                                        active_dictionary=self.completed_one_time_tasks,
                                                                        task_type='oneTimeTasks')

    def clear_all_completed_tasks(self) -> None:
        self.completed_one_time_tasks = self.taskFunctions.clearing_all_tasks(task_type="completedOneTimeTasks")

    def delete_all_completed_tasks(self) -> None:
        self.clear_all_completed_tasks()

    def save_active_one_time_tasks(self) -> None:

        self.DataOutputOperations.save_as_file(task_status='active',
                                               task_type='oneTimeTasks',
                                               dictionary_to_save=self.active_one_time_tasks)

    def save_completed_one_time_tasks(self) -> None:

        self.DataOutputOperations.save_as_file(task_status='completed',
                                               task_type='oneTimeTasks',
                                               dictionary_to_save=self.completed_one_time_tasks)

    # TODO: implement priorities
    def sort_by_priority(self) -> StringDict:
        pass
        # return sorted_by_priority

    # GET operations
    def get_active(self) -> StringDict:
        return self.active_one_time_tasks

    def get_completed(self) -> StringDict:
        return self.completed_one_time_tasks
