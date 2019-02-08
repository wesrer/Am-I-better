from typing import List, Dict

# Custom Type Hints for Type Checking
StringList = List[str]
StringDict = Dict[str, str]


# TODO: figure out how to refresh tasks
class Habits:
    def __init__(self,
                 dataIOOperationsObject,
                 taskFunctionsObject):

        self.DataIOOperationsObject = dataIOOperationsObject;
        self.TaskFunctionsObject = taskFunctionsObject

        self.activeHabits = \
            self.DataIOOperationsObject.getTasks(taskStatus='active',
                                                 taskType='habits')
        self.inactiveHabits = \
            self.DataIOOperationsObject.getTasks(taskStatus='inactive',
                                                 taskType='habits')

    def addHabit(self,
                 habitString: str,
                 priority: int = 0,
                 refreshRate: int = 1) -> None:

        unqiueID = self.DataIOOperationsObject.getNewUniqueIDForTask('habits')

        self.activeHabits[str(unqiueID)] = \
            self.TaskFunctionsObject.addTasks(taskString=habitString,
                                              taskType="habits",
                                              priority=priority,
                                              refreshRate=refreshRate)

    def deleteHabit(self,
                    idToDelete: int) -> None:
        self.activeHabits = \
            self.TaskFunctionsObject.deleteTask(idToDelete=idToDelete,
                                                activeDictionary=self.activeHabits,
                                                taskType="habits")

    def markHabitAsInactive(self,
                            idToMarkAsInactive: int) -> None:
        self.activeHabits, self.inactiveHabits = \
            self.TaskFunctionsObject.markTaskAsCompleted(idToMarkAsCompleted=idToMarkAsInactive,
                                                         activeDictionary=self.activeHabits,
                                                         completedDictionary=self.inactiveHabits,
                                                         taskType="habits",
                                                         completedTaskType="inactiveHabits")

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
