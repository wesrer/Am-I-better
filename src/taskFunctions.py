import datetime

class taskFunctions:
    def __init__(self):

        pass


    def addTasks(self,
                 taskString,
                 taskID,
                 taskDictionary,
                 priority=0,
                 completeBy=False,
                 refreshRate=0):

        # By default, all tasks need to be completed by 24 hours of initializing them
        if not taskID == 'oneTimeTasks' and not completeBy:
            completeBy = datetime.datetime.now() + datetime.timedelta(hours=24)

        # formatting the string
        completeBy = completeBy.strftime("%c")

        # make a JSON object to append to the existing list
        dataDict = {
            "taskString": taskString,
            "assignedOn": (datetime.datetime.now()).strftime("%c"),
            "priority": priority,
        }

        if taskID == 'oneTimeTasks':
            dataDict["completeBy"] = completeBy
        elif taskID == 'habits':
            dataDict["refreshRate"] = refreshRate





    def addOneTimeTask(self, taskString, priority=0, completeBy=False):
        self.lastUniqueID += 1

        # By default, all tasks need to be completed by 24 hours of initializing them
        if not completeBy:
            completeBy = datetime.datetime.now() + datetime.timedelta(hours=24)

        # formatting the string
        completeBy = completeBy.strftime("%c")

        # make a JSON object to append to the existing list
        self.activeOneTimeTasks[self.lastUniqueID] = {
            "taskString": taskString,
            "assignedOn": (datetime.datetime.now()).strftime("%c"),
            "completeBy": completeBy,
            "priority": priority,
        }

        print(self.activeOneTimeTasks)
