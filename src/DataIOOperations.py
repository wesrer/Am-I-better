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
    #   - taskType - "oneTimeTasks" or "habits" or "longTermProjects"
    #
    # FUNCTION PURPOSE:
    #   reads the JSON file '< taskType >.json' from directory < taskStatus >
    #   inside the data directory and returns it

    def getTasks(self, taskStatus, taskType):
        pathAddress = self.dataDirectory / taskStatus / (taskType + ".json")

        # FIXME: this needs to be a read from a JSON file
        with pathAddress.open() as f:
            data = json.load(f)

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

    def saveAsFile(self, taskStatus, taskType, dictionaryToSave):
        fileAddress = self.dataDirectory / taskStatus / (taskType + ".json")
        #fileAddress.unlink()

        with open(fileAddress, 'w') as writefile:
            json.dump(
                dictionaryToSave,
                writefile,
                sort_keys=True,
                indent=4,
                ensure_ascii=False)

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

    def getUniqueIDs(self, taskType):
        return self.uniqueIDs[taskType]

    def updateUniqueIDs(self, taskType, newID):
        self.uniqueIDs[taskType] = newID

    def writeUniqueIDs(self):
        with open(self.uniqueIDsFile, 'w') as idfile:
            dataToWrite = json.dumps(self.uniqueIDs,
                      sort_keys=True,
                      indent=4,
                      ensure_ascii=False)
            idfile.write(dataToWrite)
            idfile.close()



