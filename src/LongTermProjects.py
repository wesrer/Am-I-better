# TODO:
#   The implementation of long term projects would be almost exactly the
#   same as oneTimeTasks, except tasks would be grouped together based on their
#   outer long term project association.

class LongTermProjects:
    def __init__(self,
                 dataIOOperationsObject,
                 taskFunctionsObject):
        self.DataIOOperationsObject = dataIOOperationsObject
        self.TaskFunctionsObject = dataIOOperationsObject
        pass

    def addLongTermProject(self):
        pass

    def addSubTaskToLongTermProject(self,
                                    longTermProjectID: int,
                                    taskString: str,
                                    ) -> None:
        pass

    # TODO: add a check that doesn't let a project with incomplete subtasks to be
    #       marked as completed
    def markLongTermProjectAsCompleted(self, idToMarkAsCompleted: int) -> None:
        pass

    def deleteLongTermProject(self, idToDelete: int) -> None:
        pass

    def markSubTaskAsCompleted(self,
                               longTermProjectID: int,
                               subTaskID: int) -> None:
        pass

    def deleteSubTask(self,
                      longTermProjectID: int,
                      subTaskID: int) -> None:
        pass
