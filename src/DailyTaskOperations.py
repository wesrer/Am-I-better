import CompletedTasksOperations as completed
import datetime


class DailyTaskOperations:
    def __init__(self, dailyTasksHash):
        self.dailyTasks = dailyTasksHash

    def add_daily_task(self, task_string, priority=0):
        self.dailyTasks[task_string] = {
            "assignedOnDate": datetime.now.today(),
            "priority": priority,
            "assignedOnTime": datetime.datetime.now(),
        }

    def mark_daily_task_as_complete(self, task_string):
        task_value = self.dailyTasks.pop(task_string, None)
        completed_on = datetime.now.today()
        completed.addToCompletedTasks(task_value, completed_on)

    # def getTimeLeftForDailyTask(taskString):
    #     pass
