from typing import List, Dict
import sys

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
                 completed_one_time_tasks: StringDict,
                 inactive_one_time_tasks: StringDict):

        self.DataInputOperations = data_input_operations_object
        self.DataOutputOperations = data_output_operations_object
        self.taskFunctions = task_functions_object

        self.completed_tasks = completed_one_time_tasks
        self.active_tasks = active_one_time_tasks
        self.inactive_tasks = inactive_one_time_tasks

        self.default_time_values = self.DataInputOperations.get_default_values("time", "oneTimeTasks")

    # FIXME: figure out how to take customized completeBy input
    def add(self,
            task_string: str,
            priority: int = 0,
            weight: int = 3,
            complete_by: str = "defaultValue",
            queue: str = "active") -> None:

        if queue == "active":
            id_string = "oneTimeTasks"
            dedicated_dict = self.active_tasks

            if complete_by == "defaultValue":
                complete_by = self.default_time_values
            else:
                complete_by = self.taskFunctions.convert_time_string_to_dictionary(complete_by)

        elif queue == "inactive":
            id_string = "inactiveOneTimeTasks"
            complete_by = "N/A"
            dedicated_dict = self.inactive_tasks

        unique_id = self.DataInputOperations.get_new_unique_id_for_task('oneTimeTasks')
        unique_id = str(unique_id)  # for easier JSON conversion
        dedicated_dict[unique_id] = self.taskFunctions.add_tasks(task_string=task_string,
                                                                 task_type=id_string,
                                                                 priority=priority,
                                                                 weight=weight,
                                                                 complete_by=complete_by)

        print(f"Successfully added task {unique_id} to {queue} tasks.")

    def update(self,
               id_to_update: int,
               option_to_update: str,
               updated_value: str):
        option_to_update = option_to_update.lower()

        try:
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
                raise NotImplementedError
            else:
                raise ValueError

            self.active_tasks = self.taskFunctions.update_values(id_to_edit=id_to_update,
                                                                 field_name=field_type,
                                                                 active_dictionary=self.active_tasks,
                                                                 updated_value=updated_value)
        except NotImplementedError as e:
            sys.exit(f"{option_to_update} hasn't been implemented yet. Sorry!")
        except ValueError as e:
            sys.exit(f"{option_to_update} is not a recognized property and cannot be updated")

        print(f"Successfully updated task {id_to_update}")

    # TODO: refactor this to only deal with lists, because handling two cases doesn't make sense
    def mark_as_completed(self,
                          id_to_mark_as_completed: int = -1,  # for legacy support; depcrecate this
                          list_of_ids_to_mark_as_completed: List[int] = []) -> None:

        if len(list_of_ids_to_mark_as_completed) != 0:
            self.active_tasks, self.completed_tasks = self.taskFunctions.mark_tasks(
                list_of_ids_to_mark=list_of_ids_to_mark_as_completed,
                active_dictionary=self.active_tasks,
                completed_dictionary=self.completed_tasks,
                task_type="oneTimeTasks",
                completed_task_type="completedOneTimeTasks")

            id_string = ', '.join([str(x) for x in list_of_ids_to_mark_as_completed])
            print(f"Successfully marked tasks {id_string} as completed")
        else:
            self.active_tasks, self.completed_tasks = \
                self.taskFunctions.mark_tasks(id_to_mark=id_to_mark_as_completed,
                                              active_dictionary=self.active_tasks,
                                              completed_dictionary=self.completed_tasks,
                                              task_type="oneTimeTasks",
                                              completed_task_type="completedOneTimeTasks")

            print(f"Successfully marked task {id_to_mark_as_completed} as completed")

    def mark_as_inactive(self,
                         list_of_ids_to_mark_as_inactive: List[int]) -> None:

        self.active_tasks, self.inactive_tasks = \
            self.taskFunctions.mark_tasks(list_of_ids_to_mark=list_of_ids_to_mark_as_inactive,
                                          active_dictionary=self.active_tasks,
                                          completed_dictionary=self.inactive_tasks,
                                          task_type="oneTimeTasks",
                                          completed_task_type="inactiveOneTimeTasks")

    def unmark(self,
               list_of_ids_to_unmark: List[int],
               unmark_from_queue: str,
               unmark_to_queue: str = "active"):
        try:
            if unmark_from_queue in ["active"]:
                raise KeyError
            unmark_from_queue = self.get_queue(queue=unmark_from_queue)
            unmark_to_queue = self.get_queue(queue=unmark_to_queue)

            # FIXME: this can be simplified if we maintained a consistent naming scheme
            #        so for instance, "activeOneTimeTasks" instead of "oneTimeTasks"
            #        REFACTOR THIS LATER.
            unmark_to_task_type = ""
            if unmark_to_queue in ["active"]:
                unmark_to_task_type = "oneTimeTasks"
            else:
                unmark_to_task_type = f"{unmark_to_queue}OneTimeTasks"


            unmark_to_queue, unmark_from_queue = self.taskFunctions.unmark(list_of_ids_to_unmark=list_of_ids_to_unmark,
                                                                           unmark_to=unmark_to_queue,
                                                                           unmark_from=unmark_from_queue,
                                                                           task_type=unmark_to_task_type,
                                                                           completed_task_type=un)

        except KeyError as e:
            sys.exit("Cannot unmark from active queue.")

    def unmark_completed(self, list_of_ids_to_unmark: List[int]) -> None:

        self.active_tasks, self.completed_tasks = \
            self.taskFunctions.unmark(list_of_ids_to_unmark=list_of_ids_to_unmark,
                                      unmark_to=self.active_tasks,
                                      unmark_from=self.completed_tasks,
                                      task_type="oneTimeTasks",
                                      completed_task_type="completedOneTimeTasks")

    def delete_from_queue(self,
                          queue: str,
                          list_of_ids_to_delete: List[int]) -> None:
        try:
            if queue == "active":
                queue_dict = self.active_tasks

            elif queue == "inactive":
                queue_dict = self.inactive_tasks

            elif queue == "completed":
                queue_dict = self.completed_tasks
            else:
                raise ValueError

            queue_dict = self.taskFunctions.delete_tasks(list_of_ids_to_delete=list_of_ids_to_delete,
                                                         active_dictionary=queue_dict,
                                                         task_type='oneTimeTasks')

            id_string = ', '.join([str(x) for x in list_of_ids_to_delete])
            print(f"Successfully deleted {queue} tasks {id_string}")

        except ValueError as e:
            sys.exit(f"{queue} is not a valid task queue")

    def delete_active(self, list_of_ids_to_delete: List[int]) -> None:

        self.active_tasks = self.taskFunctions.delete_tasks(list_of_ids_to_delete=list_of_ids_to_delete,
                                                            active_dictionary=self.active_tasks,
                                                            task_type='oneTimeTasks')

        id_string = ', '.join([str(x) for x in list_of_ids_to_delete])
        print(f"Successfully deleted active tasks {id_string}")

    def delete_completed(self, list_of_ids_to_delete: List[int]) -> None:
        self.completed_tasks = self.taskFunctions.delete_tasks(list_of_ids_to_delete=list_of_ids_to_delete,
                                                               active_dictionary=self.completed_tasks,
                                                               task_type='oneTimeTasks')
        id_string = ', '.join([str(x) for x in list_of_ids_to_delete])
        print(f"Successfully deleted completed tasks {id_string}")

    def delete_inactive(self, list_of_ids_to_delete: List[int]) -> None:
        self.inactive_tasks = self.taskFunctions.delete_tasks(list_of_ids_to_delete=list_of_ids_to_delete,
                                                              active_dictionary=self.inactive_tasks,
                                                              task_type='oneTimeTasks')
        id_string = ', '.join([str(x) for x in list_of_ids_to_delete])
        print(f"Successfully deleted inactive tasks {id_string}")

    def clear_all_completed_tasks(self) -> None:
        self.completed_tasks = self.taskFunctions.clearing_all_tasks(task_type="completedOneTimeTasks")
        print(f"Successfully deleted all completed tasks")

    def clear_all_inactive_tasks(self) -> None:
        self.inactive_tasks = self.taskFunctions.clearing_all_tasks(task_type="inactiveOneTimeTasks")

    def clear_all_tasks_from_queue(self,
                                   queue: str):
        try:
            # TODO: issue a statment of warning about deleting all tasks
            if queue in ["completed"]:
                self.completed_tasks = self.taskFunctions.clearing_all_tasks(task_type="completedOneTimeTasks")
            elif queue in ["inactive"]:
                self.inactive_tasks = self.taskFunctions.clearing_all_tasks(task_type="inactiveOneTimeTasks")
            elif queue in ["active"]:
                raise NotImplementedError
            else:
                raise ValueError

        except ValueError as e:
            sys.exit(f"{queue} is not a valid queue to delete")
        except NotImplementedError as e:
            sys.exit(f"Deleting all active tasks hasn't been implemented yet, "
                     f"because recovery options haven't been implemented either.")

    def delete_all_tasks(self,
                         queue: str):
        self.clear_all_tasks_from_queue(queue=queue)

    def save_task_queues(self) -> None:
        self.DataOutputOperations.save_as_file(task_status='active',
                                               task_type='oneTimeTasks',
                                               dictionary_to_save=self.active_tasks)

        self.DataOutputOperations.save_as_file(task_status='completed',
                                               task_type='oneTimeTasks',
                                               dictionary_to_save=self.completed_tasks)

        self.DataOutputOperations.save_as_file(task_status='inactive',
                                               task_type='oneTimeTasks',
                                               dictionary_to_save=self.inactive_tasks)

    # TODO: implement priorities
    def sort_by_priority(self) -> StringDict:
        pass
        # return sorted_by_priority

    @staticmethod
    def get_task_type(queue: str):
        if queue in ["active"]:
            return "oneTimeTasks"
        elif queue in ["inactive", "completed"]:
            return f"{queue}OneTimeTasks"
        else:
            sys.exit(f"{queue} is not a recognized queue for tasks")

    def get_queue(self,
                  queue: str):
        queue = queue.lower()
        if queue in ["active"]:
            return self.active_tasks
        elif queue in ["completed"]:
            return self.completed_tasks
        elif queue in ["inactive"]:
            return self.inactive_tasks
