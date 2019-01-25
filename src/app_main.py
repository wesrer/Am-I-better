
import DataIOOperations
import OneTimeTasks

class App:
    def __init__(self):
        self.dailyTasks = []
        self.DataIOOperationsObject = DataIOOperations.DataIOOperations()
        self.OneTimeTasksObject = OneTimeTasks.OneTimeTasks()

    def onCloseOperations(self):

        # TODO: have to do this for all the kinds of operations
        self.OneTimeTasksObject.saveActiveOneTimeTasks()
        self.OneTimeTasksObject.saveCompletedOneTimeTasks()



        self.DataIOOperationsObject.writeUniqueIDs()



