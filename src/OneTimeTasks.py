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
        self.activeOneTimeTasks, self.completedOneTimeTasks = \
            self.taskFunctionsObject.markTaskAsCompleted(idToMarkAsCompleted=idToMarkAsCompleted,
                                                         activeDictionary=self.activeOneTimeTasks,
                                                         completedDictionary=self.completedOneTimeTasks,
                                                         taskType="oneTimeTasks",
                                                         completedTaskType="completedOneTimeTasks")

    def deleteTask(self, idToDelete):
        self.activeOneTimeTasks = \
            self.taskFunctionsObject.deleteTask(idToDelete=idToDelete,
                                                activeDictionary=self.activeOneTimeTasks,
                                                taskType='oneTimeTasks')

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
