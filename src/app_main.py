from DataIOOperations import DataIOOperations
from taskFunctions import taskFunctions
from oneTimeTasks import OneTimeTasks
from habits import Habits

class App:
    def __init__(self):
        self.dailyTasks = []
        self.DataIOOperationsObject = DataIOOperations()
        self.TaskFunctionsObject = taskFunctions(self.DataIOOperationsObject)

        self.MainOneTimeTasksObject = self.initializeMainOneTimeTasksObject()
        self.HabitsObject = Habits(self.DataIOOperationsObject,
                                   self.TaskFunctionsObject)

    def onStartOperations(self):
        pass

    # This is the Class Level Initialization of One Time Tasks
    # There can also be long term tasks level initialization of oneTimeTasks
    def initializeMainOneTimeTasksObject(self):
        completedOneTimeTasks = \
            self.DataIOOperationsObject.getTasks(taskStatus='completed',
                                                 taskType='oneTimeTasks')
        activeOneTimeTasks = \
            self.DataIOOperationsObject.getTasks(taskStatus='active',
                                                 taskType='oneTimeTasks')

        return OneTimeTasks(self.DataIOOperationsObject,
                            self.TaskFunctionsObject,
                            activeOneTimeTasks,
                            completedOneTimeTasks)

    def onCloseOperations(self):
        # TODO: have to do this for all the kinds of operations
        self.OneTimeTasksObject.saveActiveOneTimeTasks()
        self.OneTimeTasksObject.saveCompletedOneTimeTasks()

        self.DataIOOperationsObject.writeUniqueIDs()

    # GET operations
    def getOneTimeTaskObject(self):
        return self.OneTimeTasksObject



