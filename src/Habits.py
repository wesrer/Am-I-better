class Habits:
    def __init__(self, dataIOOperationsObject, taskFunctionsObject):
        self.DataIOOperationsObject = dataIOOperationsObject;
        self.taskFunctions = taskFunctionsObject

        self.activeHabits = self.DataIOOperationsObject.getTasks('active', 'habits')
        self.inactiveHabits = self.DataIOOperationsObject.getTasks('inactive', 'habits')

        self.lastActiveUniqueID = int(self.DataIOOperationsObject.getUniqueIDs('habits'))
        self.lastInactiveUniqueID = int(self.DataIOOperationsObject.getUniqueIDs('inactiveHabits'))

    def addHabit(self, habitString, priority=0):
        pass

    # FIXME: reuse the
    def markHabitAsInactive(self, idToMarkAsInactive):
        uniqueID =

        self.inactiveHabits[str(self.lastInactiveUniqueID)] = self.activeHabits[str(idToMarkAsInactive)]

        del self.activeHabits[str(idToMarkAsInactive)]

    def deleteHabit(self, idToDelete):
        del


    def markHabitAs