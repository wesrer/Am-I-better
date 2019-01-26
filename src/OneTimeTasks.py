import DataIOOperations
import datetime
import taskFunctions

class OneTimeTasks:
    def __init__(self):
        self.DataIOOperationsObject = DataIOOperations.DataIOOperations()
        self.taskFunctionsObject = taskFunctions.taskFunctions()

        # FIXME: replace this with an actual file
        # self.activeOneTimeTasks = {}
        # self.completedOneTimeTasks = []
        self.completedOneTimeTasks = self.DataIOOperationsObject.getTasks('completed', 'oneTimeTasks')
        self.activeOneTimeTasks = self.DataIOOperationsObject.getTasks('active', 'oneTimeTasks')

        self.lastUniqueID = int(self.DataIOOperationsObject.getUniqueIDs('oneTimeTasks'))

    # FIXME: add more properties, because these are clearly not enough
    # FIXME: figure out how to take customized completeBy input
    def addOneTimeTask(self, taskString, priority=0, completeBy = False):
        self.lastUniqueID += 1

        self.activeOneTimeTasks[self.lastUniqueID] = self.taskFunctionsObject.addTasks(
                                                        taskString, "oneTimeTasks", priority, completeBy)

    # TODO: write this function
    def markTaskAsCompleted(self, idToMarkAsCompleted):
        self.completedOneTimeTasks.append(self.activeOneTimeTasks[idToMarkAsCompleted])
        del self.activeOneTimeTasks[idToMarkAsCompleted]

    def getActiveOneTimeTasks(self):
        return self.activeOneTimeTasks

    def getCompletedOneTimeTasks(self):
        return self.completedOneTimeTasks

    def saveActiveOneTimeTasks(self):
        print("saving active one time tasks")
        self.DataIOOperationsObject.updateUniqueIDs('oneTimeTasks', self.lastUniqueID)
        self.DataIOOperationsObject.saveAsFile('active', 'oneTimeTasks', self.activeOneTimeTasks)

    def saveCompletedOneTimeTasks(self):
        print("saving completed one time tasks")
        self.DataIOOperationsObject.saveAsFile('completed', 'oneTimeTasks', self.completedOneTimeTasks)

    def sortByPriority(self):
        # TODO
        sortedByPriority = 0
        return sortedByPriority
