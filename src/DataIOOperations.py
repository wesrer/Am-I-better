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

        print("trying to save this dict")
        print(dictionaryToSave)
        print()

        with open(fileAddress, 'w') as writefile:
            json.dump(
                dictionaryToSave,
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
                              taskType: str) -> int:
        if len(self.uniqueIDs[taskType]["available"]) == 0:
            newUniqueID = self.uniqueIDs[taskType]["next"]

            self.uniqueIDs[taskType]["next"] = str(int(newUniqueID) + 1)
        else:
            newUniqueID = self.uniqueIDs[taskType]["available"].pop(0)

        return int(newUniqueID)

    def markIDAsAvailable(self,
                          taskType: str,
                          idToMarkAsAvailable: int) -> None:
        self.uniqueIDs[taskType]["available"].append(str(idToMarkAsAvailable))

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



