from typing import List, Dict

# TODO: figure out how to Type Cast Custom Objects
# Custom Type Hints for Type Checking
StringList = List[str]
StringDict = Dict[str, str]


# FIXME: separate data_output_operations
class OneTimeTasks:

    def __init__(self,
                 data_input_operations_object,
                 task_functions_object,
                 active_one_time_tasks: StringDict,
                 completed_one_time_tasks: StringDict):

        self.DataInputOperationsObject = data_input_operations_object
        self.taskFunctionsObject = task_functions_object

        self.completedOneTimeTasks = completed_one_time_tasks
        self.activeOneTimeTasks = active_one_time_tasks

        self.defaultTimeValues = \
            self.DataInputOperationsObject.get_default_values("time", "oneTimeTasks")

    # FIXME: figure out how to take customized completeBy input
    def add_one_time_task(self,
                          task_string: str,
                          priority: int = 0,
                          complete_by: str = "defaultValue") -> None:

        unique_id = self.DataInputOperationsObject.get_new_unique_id_for_task('oneTimeTasks')

        if complete_by == "defaultValue":
            complete_by = self.defaultTimeValues
        else:
            complete_by = \
                self.taskFunctionsObject.convert_time_string_to_dictionary(complete_by)

        self.activeOneTimeTasks[str(unique_id)] = \
            self.taskFunctionsObject.add_tasks(task_string=task_string,
                                               task_type="oneTimeTasks",
                                               priority=priority,
                                               complete_by=complete_by)

    def mark_task_as_completed(self,
                               id_to_mark_as_completed: int) -> None:

        self.activeOneTimeTasks, self.completedOneTimeTasks = \
            self.taskFunctionsObject.mark_task_as_completed(id_to_mark_as_completed=id_to_mark_as_completed,
                                                            active_dictionary=self.activeOneTimeTasks,
                                                            completed_dictionary=self.completedOneTimeTasks,
                                                            task_type="oneTimeTasks",
                                                            completed_task_type="completedOneTimeTasks")

    def delete_task(self,
                    id_to_delete: int) -> None:

        self.activeOneTimeTasks = \
            self.taskFunctionsObject.delete_task(id_to_delete=id_to_delete,
                                                 active_dictionary=self.activeOneTimeTasks,
                                                 task_type='oneTimeTasks')

    def save_active_one_time_tasks(self) -> None:

        self.DataInputOperationsObject.save_as_file(task_status='active',
                                                    task_type='oneTimeTasks',
                                                    dictionary_to_save=self.activeOneTimeTasks)

    def save_completed_one_time_tasks(self) -> None:

        self.DataInputOperationsObject.save_as_file(task_status='completed',
                                                    task_type='oneTimeTasks',
                                                    dictionary_to_save=self.completedOneTimeTasks)

    # TODO: implement priorities
    def sort_by_priority(self) -> StringDict:

        sorted_by_priority= 0
        return sorted_by_priority

    # GET operations
    def get_active_one_time_tasks(self) -> StringDict:
        return self.activeOneTimeTasks

    def get_completed_one_time_tasks(self) -> StringDict:
        return self.completedOneTimeTasks
