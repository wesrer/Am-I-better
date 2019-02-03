
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

        self.DataIOOperationsObject.writeUniqueIDs()

    def updateAllUniqueIDs(self):
        # getting all the unique IDs from the respective classes
        oneTimeTasksID = self.OneTimeTasksObject.getLastUniqueID()

        # updating them in the data records
        self.DataIOOperationsObject.updateUniqueIDs("oneTimeTasks", oneTimeTasksID)




