import json

class DataIOOperations:
    def __init__(self):
        #FIXME: this needs to be a read from the JSON file
        self.oneTimeTasks = {}

    def getOneTimeTasks(self):
        return self.oneTimeTasks

    def getHabits(self):
        return self.habits

    def getLongTermProjects(self):
        return self.longTermProjects

    def saveOneTimeTasks(self, oneTimeTasks):
        dataInJSON = json.dumps(oneTimeTasks, ensure_ascii=False)

        # FIXME: save data into the JSON file
        return dataInJSON

    def readOneTimeTasksLastUniqueID(self):
        # FIXME: this needs to be a read from a JSON file
        return 1
