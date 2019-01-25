import DataIOOperations
import datetime
import taskFunctions

class OneTimeTasks:
    def __init__(self):
        self.DataIOOperationsObject = DataIOOperations.DataIOOperations() 
        # FIXME: replace this with an actual file
        self.activeOneTimeTasks = {}
        # self.completedOneTimeTasks = self.DataIOOperationsObject.getTasks('completed', 'oneTimeTasks')
        # self.activeOneTimeTasks = self.DataIOOperationsObject.getTasks('active', 'oneTimeTasks')

        self.lastUniqueID = int(self.DataIOOperationsObject.getUniqueIDs('oneTimeTasks'))

    # FIXME: add more properties, because these are clearly not enough
    # FIXME: figure out how to take customized completeBy input
    def addOneTimeTask(self, taskString, priority=0, completeBy = False):
        self.lastUniqueID += 1

        # By default, all tasks need to be completed by 24 hours of initializing them
        if not completeBy:
            completeBy = datetime.datetime.now() + datetime.timedelta(hours = 24)
        
        # formatting the string
        completeBy = completeBy.strftime("%c")
        
        # make a JSON object to append to the existing list
        self.activeOneTimeTasks[self.lastUniqueID] = {
            "taskString" : taskString,
            "assignedOn" : (datetime.datetime.now()).strftime("%c"),
            "completeBy" : completeBy,
            "priority" : priority,
        }

        print(self.activeOneTimeTasks)

    # TODO: write this function
    def markTaskAsCompleted(self):
        pass

    def getActiveOneTimeTasks(self):
        return self.activeOneTimeTasks

    def getCompletedOneTimeTasks(self):
        return self.completedOneTimeTasks

    def saveActiveOneTimeTasks(self):
        self.DataIOOperationsObject.updateUniqueIDs('oneTimeTasks', self.lastUniqueID)
        self.DataIOOperationsObject.saveAsFile('active', 'oneTimeTasks', self.activeOneTimeTasks)

    def saveCompletedOneTimeTasks(self):
        self.DataIOOperationsObject.saveAsFile('completed', 'oneTimeTasks', self.completedOneTimeTasks)

    def sortByPriority(self):
        # TODO
        sortedByPriority = 0
        return sortedByPriority
