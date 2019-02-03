
import DataIOOperations
import OneTimeTasks

class App:
    def __init__(self, oneTimeTaskObject, dataIOOperationsObject):
        self.dailyTasks = []
        self.DataIOOperationsObject = dataIOOperationsObject
        self.OneTimeTasksObject = oneTimeTaskObject

    def onCloseOperations(self):

        # TODO: have to do this for all the kinds of operations
        self.OneTimeTasksObject.saveActiveOneTimeTasks()
        self.OneTimeTasksObject.saveCompletedOneTimeTasks()

        self.DataIOOperationsObject.writeUniqueIDs()



