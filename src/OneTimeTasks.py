import DataIOOperations
import datetime
import json

#TODO: write on close app operations - save the last used uniqueID
class OneTimeTasks:
    def __init__(self):
        self.DataIOOperationsObject = DataIOOperations.DataIOOperations() 
        self.oneTimeTasks = self.DataIOOperationsObject.getOneTimeTasks()
        self.lastUniqueID = self.DataIOOperationsObject.readOneTimeTasksLastUniqueID()

    # FIXME: add more properties, because these are clearly not enough
    # FIXME: figure out how to take customized completeBy input
    def addOneTimeTask(self, taskString, priority=0, completeBy = False):

        self.lastUniqueID += 1

        # By default, all tasks need to be completed by 24 hours of initializing them
        if (completeBy == False):
            completeBy = datetime.datetime.now() + datetime.timedelta(hours = 24)
        
        # formatting the string
        completeBy = completeBy.strftime("%c")
        
        # make a JSON object to append to the existing list
        self.oneTimeTasks[self.lastUniqueID] = {
            "taskString" : taskString,
            "assignedOn" : (datetime.datetime.now()).strftime("%c"),
            "completeBy" : completeBy,
            "priority" : priority,
        }

    def getOneTimeTasks(self):
        return self.oneTimeTasks

    def saveOneTimeTasks(self):
        print(self.DataIOOperationsObject.saveOneTimeTasks(self.oneTimeTasks))

    def sortByPriority(self):
        # TODO
        sortedByPriority = 0
        
        return sortedByPriority
