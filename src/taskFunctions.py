import datetime

from typing import List, Dict

# Custom Type Hints for Type Checking
StringList = List[str]
StringDict = Dict[str,str]

class taskFunctions:
    # TODO: figure out how to Type Cast Custom Objects
    def __init__(self, dataIOOperationsObject):
        self.DataIOOperationsObject = dataIOOperationsObject

    def addTasks(self,
                 taskString: str,
                 taskType: str,
                 priority: int = 0,
                 completeBy: bool = False,
                 refreshRate: int = 0):

        # By default, all tasks need to be completed by 24 hours of initializing them
        if not taskType == 'habits' and not completeBy:
            completeBy = datetime.datetime.now() + datetime.timedelta(hours=24)

        # formatting the string
        completeBy = completeBy.strftime("%c")

        # make a JSON object to append to the existing list
        dataDict = {
            "taskString": taskString,
            "assignedOn": (datetime.datetime.now()).strftime("%c"),
            "priority": priority,
        }

        if taskType == 'oneTimeTasks':
            dataDict["completeBy"] = completeBy
        elif taskType == 'habits':
            dataDict["refreshRate"] = refreshRate

        return dataDict

    # Moves Task From Active Dictionary to Completed Dictionary
    # and adjusts ids to reflect this task

    def markTaskAsCompleted(self,
                            idToMarkAsCompleted: int,
                            activeDictionary: StringDict,
                            completedDictionary: StringDict,
                            taskType: str,
                            completedTaskType: str,
                            parentID: int,
                            hasChildren: bool = False) -> [StringDict, StringDict]:


        uniqueID = self.DataIOOperationsObject.getNewUniqueIDForTask(taskType=completedTaskType,
                                                                     parentID=parentID,
                                                                     hasChildren=hasChildren)

        completedDictionary[uniqueID] = activeDictionary[str(idToMarkAsCompleted)]

        self.DataIOOperationsObject.markIDAsAvailable(taskType=taskType,
                                                      parentID=parentID,
                                                      hasChildren=hasChildren,
                                                      idToMarkAsCompleted=idToMarkAsCompleted)

        del activeDictionary[str(idToMarkAsCompleted)]

        return activeDictionary, completedDictionary

    def deleteTask(self,
                   idToDelete: int,
                   activeDictionary: StringDict,
                   taskType: str,
                   parentID: int,
                   hasChildren: bool = False) -> StringDict:

        del activeDictionary[str(idToDelete)]

        self.DataIOOperationsObject.markIDAsAvailable(taskType=taskType,
                                                      idToMarkAsAvailable=idToDelete,
                                                      hasChildren=hasChildren,
                                                      parentID=parentID)

        return activeDictionary
