import CompletedTasksOperations as completed
import datetime

class DailyTaskOperations:
    def __init__(self, dailyTasksHash):
        self.dailyTasks = dailyTasksHash

    def addDailyTask(self, taskString, priority=0):
        self.dailyTasks[taskString] = {
            "assignedOnDate" : datetime.now.today(),
            "priority" : priority,
            "assignedOnTime": datetime.datetime.now(),
        }

    def markDailyTasksAsComplete(self, taskString):
        taskValue = self.dailyTasks.pop(taskString, None)
        completedOn = datetime.now.today()
        completed.addToCompletedTasks(taskValue, completedOn)
    
    def getTimeLeftForDailyTask(taskString){
                
    }
