class OneTimeTasks:
    def __init__(self, dataIOOperationsObject, taskFunctionsObject):
        self.DataIOOperationsObject = dataIOOperationsObject
        self.taskFunctionsObject = taskFunctionsObject

        self.completedOneTimeTasks = self.DataIOOperationsObject.getTasks('completed', 'oneTimeTasks')
        self.activeOneTimeTasks = self.DataIOOperationsObject.getTasks('active', 'oneTimeTasks')


    # FIXME: add more properties, because these are clearly not enough
    # FIXME: figure out how to take customized completeBy input
    def addOneTimeTask(self, taskString, priority=0, completeBy = False):
        uniqueID = self.DataIOOperationsObject.getNewUniqueIDForTask('oneTimeTasks')

        self.activeOneTimeTasks[str(uniqueID)] = self.taskFunctionsObject.addTasks(
                                                        taskString, "oneTimeTasks", priority, completeBy)

    def markTaskAsCompleted(self, idToMarkAsCompleted):
        uniqueID = self.DataIOOperationsObject.getNewUniqueIDForTask('completedOneTimeTasks')

        self.completedOneTimeTasks[uniqueID] = self.activeOneTimeTasks[str(idToMarkAsCompleted)]
        self.DataIOOperationsObject.markIDAsAvailable('oneTimeTasks', idToMarkAsCompleted)

        del self.activeOneTimeTasks[str(idToMarkAsCompleted)]


    # TODO: the empty id can be reused so make sure that it is
    def deleteTask(self, idToDelete):
        del self.activeOneTimeTasks[str(idToDelete)]

    def saveActiveOneTimeTasks(self):
        self.DataIOOperationsObject.saveAsFile('active', 'oneTimeTasks', self.activeOneTimeTasks)

    def saveCompletedOneTimeTasks(self):
        self.DataIOOperationsObject.saveAsFile('completed', 'oneTimeTasks', self.completedOneTimeTasks)

    # TODO: implement priorities
    def sortByPriority(self):
        sortedByPriority = 0
        return sortedByPriority

    # GET operations

    def getActiveOneTimeTasks(self):
        return self.activeOneTimeTasks

    def getCompletedOneTimeTasks(self):
        return self.completedOneTimeTasks
