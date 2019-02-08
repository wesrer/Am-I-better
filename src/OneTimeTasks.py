from typing import List, Dict

# TODO: figure out how to Type Cast Custom Objects
# Custom Type Hints for Type Checking
StringList = List[str]
StringDict = Dict[str,str]

class OneTimeTasks:
    def __init__(self,
                 dataIOOperationsObject,
                 taskFunctionsObject,
                 activeOneTimeTasks: StringDict,
                 completedOneTimeTasks: StringDict):

        self.DataIOOperationsObject = dataIOOperationsObject
        self.taskFunctionsObject = taskFunctionsObject

        self.completedOneTimeTasks = completedOneTimeTasks
        self.activeOneTimeTasks = activeOneTimeTasks

    # FIXME: add more properties, because these are clearly not enough
    # FIXME: figure out how to take customized completeBy input
    def addOneTimeTask(self,
                       taskString: str,
                       priority: int = 0,
                       completeBy: bool = False) -> None:

        uniqueID = self.DataIOOperationsObject.getNewUniqueIDForTask('oneTimeTasks')

        self.activeOneTimeTasks[str(uniqueID)] = \
            self.taskFunctionsObject.add_tasks(task_string=taskString,
                                               task_type="oneTimeTasks",
                                               priority=priority,
                                               complete_by=completeBy)

    def markTaskAsCompleted(self,
                            idToMarkAsCompleted: int) -> None:

        self.activeOneTimeTasks, self.completedOneTimeTasks = \
            self.taskFunctionsObject.mark_task_as_completed(id_to_mark_as_completed=idToMarkAsCompleted,
                                                            active_dictionary=self.activeOneTimeTasks,
                                                            completed_dictionary=self.completedOneTimeTasks,
                                                            task_type="oneTimeTasks",
                                                            completed_task_type="completedOneTimeTasks")

    def deleteTask(self,
                   idToDelete: int) -> None:

        self.activeOneTimeTasks = \
            self.taskFunctionsObject.delete_task(id_to_delete=idToDelete,
                                                 active_dictionary=self.activeOneTimeTasks,
                                                 task_type='oneTimeTasks')

    def saveActiveOneTimeTasks(self) -> None:

        self.DataIOOperationsObject.saveAsFile(taskStatus='active',
                                               taskType='oneTimeTasks',
                                               dictionaryToSave=self.activeOneTimeTasks)

    def saveCompletedOneTimeTasks(self) -> None:

        self.DataIOOperationsObject.saveAsFile(taskStatus='completed',
                                               taskType='oneTimeTasks',
                                               dictionaryToSave=self.completedOneTimeTasks)

    # TODO: implement priorities
    def sortByPriority(self) -> StringDict:

        sortedByPriority = 0
        return sortedByPriority

    # GET operations
    def getActiveOneTimeTasks(self) -> StringDict:
        return self.activeOneTimeTasks

    def getCompletedOneTimeTasks(self) -> StringDict:
        return self.completedOneTimeTasks
