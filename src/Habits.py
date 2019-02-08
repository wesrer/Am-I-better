
# TODO: figure out how to refresh tasks
class Habits:
    def __init__(self, dataIOOperationsObject, taskFunctionsObject):
        self.DataIOOperationsObject = dataIOOperationsObject;
        self.TaskFunctionsObject = taskFunctionsObject

        self.activeHabits = self.DataIOOperationsObject.getTasks('active', 'habits')
        self.inactiveHabits = self.DataIOOperationsObject.getTasks('inactive', 'habits')

    def addHabit(self, habitString, priority=0, refreshRate=1):
        unqiueID = self.DataIOOperationsObject.getNewUniqueIDForTask('habits')

        self.activeHabits[str(unqiueID)] = \
            self.TaskFunctionsObject.addTasks(taskString=habitString,
                                              taskType="habits",
                                              priority=priority,
                                              refreshRate=refreshRate)


    # FIXME: reuse the
    def markHabitAsInactive(self, idToMarkAsInactive):
        uniqueID = self.DataIOOperationsObject.getN

        self.inactiveHabits[str(self.lastInactiveUniqueID)] = self.activeHabits[str(idToMarkAsInactive)]

        del self.activeHabits[str(idToMarkAsInactive)]

    def deleteHabit(self, idToDelete):
        del


    def markHabitAsInactive(self, idToMarkAsInactive):
        self.activeHabits, self.inactiveHabits = \
            self.TaskFunctionsObject.markTaskAsCompleted(idToMarkAsCompleted=idToMarkAsInactive,
                                                         activeDictionary=self.activeHabits,
                                                         completedDictionary=self.inactiveHabits,
                                                         taskType="habits",
                                                         completedTaskType="inactiveHabits")