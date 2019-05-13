# TODO:
#   The implementation of long term projects would be almost exactly the
#   same as oneTimeTasks, except tasks would be grouped together based on their
#   outer long term project association.

# FIXME: EVERYTHING!


class LongTermProjects:
    def __init__(self,
                 data_io_operations_object,
                 task_functions_object,
                 active_long_term_projects,
                 completed_long_term_projects):
        self.DataIOOperationsObject = data_io_operations_object
        self.TaskFunctionsObject = task_functions_object

        self.activeLongTermProjecs = active_long_term_projects
        self.completedLongTermProjects = completed_long_term_projects

    # Every long term project
    def add_long_term_project(self,
                              project_string,
                              priority: int = 0,
                              complete_by: bool = False):
        unique_id = self.DataIOOperationsObject.get_new_unique_id_for_task(task_type="longTermProjects")

        self.activeLongTermProjecs[str(unique_id)] = \
            self.taskFunctions


    def add_sub_task_to_long_term_project(self,
                                          long_term_project_id: int,
                                          task_string: str,
                                          ) -> None:
        pass

    # TODO: add a check that doesn't let a project with incomplete subtasks to be
    #       marked as completed
    def mark_long_term_project_as_completed(self, id_to_mark_as_completed: int) -> None:
        pass

    def delete_long_term_project(self, id_to_delete: int) -> None:
        pass

    def mark_sub_task_as_completed(self,
                                   long_term_project_id: int,
                                   sub_task_id: int) -> None:
        pass

    def delete_sub_task(self,
                        long_term_project_id: int,
                        sub_task_id: int) -> None:
        pass
