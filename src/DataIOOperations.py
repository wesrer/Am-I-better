from pathlib import Path 
import json

from typing import List, Dict

# Type Hints for Type Checking
StringList = List[str]
StringDict = Dict[str,str]

class DataIOOperations:
    def __init__(self):
        self.currentDirectory = Path('.')
        self.dataDirectory = self.currentDirectory / '..' / 'data'
        self.uniqueIDsFile = self.dataDirectory / 'uniqueIDs.json'
        self.uniqueIDs = self.readUniqueIDs()

    # FUNCTION PARAMETERS:
    #   - taskStatus - "active" or "completed"
    #   - taskType - "oneTimeTasks" or "habits" or "longTermProjects"
    #
    # FUNCTION PURPOSE:
    #   reads the JSON file '< taskType >.json' from directory < taskStatus >
    #   inside the data directory and returns it

    def getTasks(self,
                 taskStatus: str,
                 taskType: str,
                 childTaskType: str = "None",
                 parentTaskID: int = 0) -> StringDict:

        pathAddress = self.dataDirectory / taskStatus / (taskType + ".json")

        with pathAddress.open() as f:
            data = json.load(f)

        if childTaskType != "None":
            data = data[parentTaskID][childTaskType]

        return data

    # FUNCTION PARAMETERS:
    #   - taskStatus - "active" or "completed"
    #   - taskType - "oneTimeTasks" or "habits" or "longTermProjects"
    #   - dictionaryToSave - The python dictionary that is going to be converted
    #   to JSON and then saved
    #
    # FUNCTION PURPOSE:
    #   saves a python dictionary to a ' < taskType >.json' file in directory
    #   < taskStatus >

    def saveAsFile(self,
                   taskStatus: str,
                   taskType: str,
                   dictionaryToSave: StringDict) -> None:
        fileAddress = self.dataDirectory / taskStatus / (taskType + ".json")

        with open(fileAddress, 'w') as writefile:
            json.dump(dictionaryToSave,
                      writefile,
                      sort_keys=True,
                      indent=4,
                      ensure_ascii=False)


    def readUniqueIDs(self) -> StringDict:
        with self.uniqueIDsFile.open() as f:
            data = json.load(f)
        return data

    # returns a new ID for the task being created
    def getNewUniqueIDForTask(self,
                              taskType: str,
                              parentID: int,
                              hasChildren: bool = False) -> int:

        # The dictionary has ID content at differing depths,
        # based on whether the taskType can have Children or not

        # NOTE: Current case only handles depth of 0 and 1
        # Will need to be reimplemented if any other depths
        # are present in the data structure
        if hasChildren:
            parentDictionary = self.uniqueIDs[taskType][parentID]
        else:
            parentDictionary = self.uniqueIDs[taskType]

        # send the next available ID, which is either an old ID that can
        # be recycled, or a newly generated ID
        if len(self.uniqueIDs[taskType]["available"]) == 0:
            newUniqueID = parentDictionary["next"]

            parentDictionary["next"] = str(int(newUniqueID) + 1)
        else:
            newUniqueID = parentDictionary["available"].pop(0)

        return int(newUniqueID)

    # FUNCTION PARAMETERS:
    #   taskType - "oneTimeTasks"
    #
    # FUNCTION PURPOSE: Recycles old IDs

    def markIDAsAvailable(self,
                          taskType: str,
                          parentID: int,
                          idToMarkAsAvailable: int,
                          hasChildren: bool = False,) -> None:

        # The dictionary has ID content at differing depths,
        # based on whether the taskType can have Children or not

        if hasChildren:
            parentID = self.uniqueIDs[taskType][parentID]
        else:
            parentID = self.uniqueIDs[taskType]

        parentID["available"].append(str(idToMarkAsAvailable))

    # sets up the data structure for tasks and subtasks that need their own
    # independent ID scheme
    def initializeNewIDSlots(self,
                             parentID: int,
                             parentTaskType: str) -> None:

        self.uniqueIDs[parentTaskType][parentID] = {
            "available": [],
            "next": 0
        }

    def updateUniqueIDs(self,
                        taskType: str,
                        newID: int) -> None:
        self.uniqueIDs[taskType] = str(newID)

    def writeUniqueIDs(self) -> None:
        with open(self.uniqueIDsFile, 'w') as idfile:
            dataToWrite = json.dumps(self.uniqueIDs,
                                     sort_keys=True,
                                     indent=4,
                                     ensure_ascii=False)
            idfile.write(dataToWrite)
            idfile.close()



