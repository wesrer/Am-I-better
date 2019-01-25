import datetime

class taskFunctions:
    def __init__(self):

        pass


    def addTasks(self,
                 taskString,
                 taskType,
                 priority=0,
                 completeBy=False,
                 refreshRate=0):

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
