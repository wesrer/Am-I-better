from pathlib import Path 
import json

class DataIOOperations:
    def __init__(self):
        self.currentDirectory = Path('.')
        self.dataDirectory = self.currentDirectory / '..' / 'data'
        self.uniqueIDsFile = self.dataDirectory / 'uniqueIDs.json'
        self.uniqueIDs = self.initializeIDs()
        # self.uniqueIDs = self.readUniqueIDs()

    # FUNCTION PARAMETERS:
    #   - taskStatus - "active" or "completed"
    #   - taskType - "oneTimeTasks" or "Habits" or "longTermProjects"
    #
    # FUNCTION PURPOSE:
    #   reads the JSON file '< taskType >.json' from directory < taskStatus >
    #   inside the data directory and returns it
    def getTasks(self, taskStatus, taskType):
        pathAddress = self.dataDirectory / taskStatus / taskType

        # FIXME: this needs to be a read from a JSON file
        with pathAddress.open() as f:
            data = json.load(f)

        return data

    # save
    def saveAsFile(self, taskStatus, taskType, dictionaryToSave):
        fileAddress = self.dataDirectory / taskStatus / (taskType + ".json")

        with open(fileAddress, 'w') as writefile:
            json.dump(
                dictionaryToSave,
                writefile,
                sort_keys=True,
                indent=4,
                ensure_ascii=False)

    def getUniqueIDs(self, taskType):
        return self.uniqueIDs[taskType]

    def initializeIDs(self):
        return {
            "oneTimeTasks" : "0",
            "habits" : "0",
            "longTermProjects": "0"

        }

    def readUniqueIDs(self):
        # FIXME: this needs to be a read from a JSON file
        with self.uniqueIDsFile.open() as f:
            data = json.load(f)

        return data

    def writeUniqueIDs(self):
        with open(self.uniqueIDsFile, 'w') as idfile:
            json.dump(self.uniqueIDs,
                      idfile,
                      sort_keys=True,
                      indent=4,
                      ensure_ascii=False)

