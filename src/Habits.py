from typing import List, Dict

# Custom Type Hints for Type Checking
StringList = List[str]
StringDict = Dict[str, str]


# TODO: figure out how to refresh tasks
class Habits:
    def __init__(self,
                 data_io_operations_object,
                 task_functions_object):

        self.DataIOOperationsObject = data_io_operations_object;
        self.TaskFunctionsObject = task_functions_object

        self.activeHabits = \
            self.DataIOOperationsObject.getTasks(taskStatus='active',
                                                 taskType='habits')
        self.inactiveHabits = \
            self.DataIOOperationsObject.getTasks(taskStatus='inactive',
                                                 taskType='habits')

    def add_habit(self,
                  habit_string: str,
                  priority: int = 0,
                  refresh_rate: int = 1) -> None:

        unqiueID = self.DataIOOperationsObject.getNewUniqueIDForTask(taskType='habits')

        self.activeHabits[str(unqiueID)] = \
            self.TaskFunctionsObject.add_tasks(task_string=habit_string,
                                               task_type="habits",
                                               priority=priority,
                                               refresh_rate=refresh_rate)

    def deleteHabit(self,
                    idToDelete: int) -> None:
        self.activeHabits = \
            self.TaskFunctionsObject.delete_task(id_to_delete=idToDelete,
                                                 active_dictionary=self.activeHabits,
                                                 task_type="habits")

    def markHabitAsInactive(self,
                            idToMarkAsInactive: int) -> None:
        self.activeHabits, self.inactiveHabits = \
            self.TaskFunctionsObject.mark_task_as_completed(id_to_mark_as_completed=idToMarkAsInactive,
                                                            active_dictionary=self.activeHabits,
                                                            completed_dictionary=self.inactiveHabits,
                                                            task_type="habits",
                                                            completed_task_type="inactiveHabits")

    def saveActiveHabits(self) -> None:
        self.DataIOOperationsObject.saveAsFile(taskStatus='active',
                                               taskType='habits',
                                               dictionaryToSave=self.activeHabits)

    def saveInactiveHabits(self) -> None:
        self.DataIOOperationsObject.saveAsFile(taskStatus='inactive',
                                               taskType='habits',
                                               dictionaryToSave=self.inactiveHabits)

    # GET operations

    def getActiveHabits(self) -> StringDict:
        return self.activeHabits

    def getInactiveHabits(self) -> StringDict:
        return self.inactiveHabits
