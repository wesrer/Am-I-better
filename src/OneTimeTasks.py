class OneTimeTasks:
    def __init__(self, dataIOOperationsObject, taskFunctionsObject):
        self.DataIOOperationsObject = dataIOOperationsObject
        self.taskFunctionsObject = taskFunctionsObject

        self.completedOneTimeTasks = self.DataIOOperationsObject.getTasks('completed', 'oneTimeTasks')
        self.activeOneTimeTasks = self.DataIOOperationsObject.getTasks('active', 'oneTimeTasks')

        self.lastActiveUniqueID = int(self.DataIOOperationsObject.getUniqueIDs('oneTimeTasks'))
        self.lastCompletedUniqueID = int(self.DataIOOperationsObject.getUniqueIDs('completedOneTimeTasks'))



    # FIXME: add more properties, because these are clearly not enough
    # FIXME: figure out how to take customized completeBy input
    def addOneTimeTask(self, taskString, priority=0, completeBy = False):
        self.lastActiveUniqueID += 1

        self.activeOneTimeTasks[str(self.lastActiveUniqueID)] = self.taskFunctionsObject.addTasks(
                                                        taskString, "oneTimeTasks", priority, completeBy)

    def markTaskAsCompleted(self, idToMarkAsCompleted):
        self.lastCompletedUniqueID += 1

        self.completedOneTimeTasks[str(self.lastCompletedUniqueID)] = self.activeOneTimeTasks[str(idToMarkAsCompleted)]

        del self.activeOneTimeTasks[str(idToMarkAsCompleted)]

    def saveActiveOneTimeTasks(self):
        self.DataIOOperationsObject.saveAsFile('active', 'oneTimeTasks', self.activeOneTimeTasks)

    def saveCompletedOneTimeTasks(self):
        self.DataIOOperationsObject.saveAsFile('completed', 'oneTimeTasks', self.completedOneTimeTasks)

    # TODO
    def sortByPriority(self):
        sortedByPriority = 0
        return sortedByPriority

    def updateIDs(self):
        self.DataIOOperationsObject.updateUniqueIDs("oneTimeTasks", self.lastActiveUniqueID)
        self.DataIOOperationsObject.updateUniqueIDs("completedOneTimeTasks", self.lastCompletedUniqueID)

    # GET operations

    def getActiveOneTimeTasks(self):
        return self.activeOneTimeTasks

    def getCompletedOneTimeTasks(self):
        return self.completedOneTimeTasks
