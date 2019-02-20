import datetime

from typing import List, Dict

# Custom Type Hints for Type Checking
StringList = List[str]
StringDict = Dict[str, str]

# TODO: implement complete_by parameters
class TaskFunctions:
    # TODO: figure out how to Type Cast Custom Objects
    def __init__(self, data_io_operations_object):
        self.DataIOOperationsObject = data_io_operations_object

    # FIXME: implement this
    def convert_time_string_to_dictionary(self,
                                               time_string: str) -> StringDict:
        pass

    # FUNCTION PARAMETERS:
    #   - task_String: The actual task that the user wants to do
    #   - task_type: "oneTimeTasks" or "habits" or "longTermProjects"
    #   - priority: Adds variable priorities to different tasks
    #   - complete_by: A specific deadline for the particular task (doesn't apply to habits)
    #   - refresh_rate: The rate at which
    #
    # FUNCTION PURPOSE: Add tasks to the three primary categories of active tasks

    # TODO: add the custom default values implementation
    # TODO: figure out how the refresh rate works
    def add_tasks(self,
                  task_string: str,
                  task_type: str,
                  priority: int = 0,
                  complete_by: str = "N/A",
                  refresh_rate: int = 1) -> StringDict:

        # By default, all tasks need to be completed by 24 hours of initializing them
        if task_type == "oneTimeTasks":
            complete_by = datetime.datetime.now() + datetime.timedelta(hours=24)

            # formatting the string
            complete_by = complete_by.strftime("%c")

        elif task_type == "longTermProjects":
            complete_by = datetime.datetime.now() + datetime.timedelta(years=1)

        # make a JSON object to append to the existing list
        data_dict = {
            "taskString": task_string,
            "assignedOn": (datetime.datetime.now()).strftime("%c"),
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
    def add_sub_tasks(self,
                      task_dictionary: StringDict,
                      sub_task_string: str,
                      priority: int = 0,
                      complete_by: bool = False) -> StringDict:
        pass

    # Moves Task From Active Dictionary to Completed Dictionary
    # and adjusts ids to reflect this task

    def mark_task_as_completed(self,
                               id_to_mark_as_completed: int,
                               active_dictionary: StringDict,
                               completed_dictionary: StringDict,
                               task_type: str,
                               completed_task_type: str,
                               parent_id: int,
                               has_children: bool = False) -> [StringDict, StringDict]:

        unique_id = self.DataIOOperationsObject.get_new_unique_id_for_task(task_type=completed_task_type,
                                                                           parent_id=parent_id,
                                                                           has_children=has_children)

        completed_dictionary[unique_id] = active_dictionary[str(id_to_mark_as_completed)]

        self.DataIOOperationsObject.mark_id_as_available(task_type=task_type,
                                                         parent_id=parent_id,
                                                         has_children=has_children,
                                                         idToMarkAsCompleted=id_to_mark_as_completed)

        del active_dictionary[str(id_to_mark_as_completed)]

        return active_dictionary, completed_dictionary

    # FIXME: Okay, this is not a primary concern, but it sucks that you have
    # FIXME: to send all of this excess data just because you are calling the
    # FIXME: markIDAsAvailable function
    def delete_task(self,
                    id_to_delete: int,
                    active_dictionary: StringDict,
                    task_type: str,
                    parent_id: int,
                    has_children: bool = False) -> StringDict:

        del active_dictionary[str(id_to_delete)]

        self.DataIOOperationsObject.mark_id_as_available(task_type=task_type,
                                                         id_to_mark_as_available=id_to_delete,
                                                         has_children=has_children,
                                                         parent_id=parent_id)

        return active_dictionary
