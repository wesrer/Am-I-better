import DataIOOperations
import taskFunctions
import OneTimeTasks

class App:
    def __init__(self):
        self.dailyTasks = []
        self.DataIOOperationsObject = DataIOOperations.DataIOOperations()
        self.taskFunctionsObject = taskFunctions.taskFunctions()
        self.OneTimeTasksObject = OneTimeTasks.OneTimeTasks(self.DataIOOperationsObject,
                                                            self.taskFunctionsObject)

    def onCloseOperations(self):
        # TODO: have to do this for all the kinds of operations
        self.OneTimeTasksObject.saveActiveOneTimeTasks()
        self.OneTimeTasksObject.saveCompletedOneTimeTasks()

        self.updateAllUniqueIDs()
        self.DataIOOperationsObject.writeUniqueIDs()

    def updateAllUniqueIDs(self):
        # TODO: do this for all the Task Types
        self.OneTimeTasksObject.updateIDs()

    # GET operations
    def getOneTimeTaskObject(self):
        return self.OneTimeTasksObject



