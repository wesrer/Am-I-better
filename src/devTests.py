import OneTimeTasks
import DataIOOperations
import app_main


def testOneTimeTasks():
    # definitions
    dataIOOperationsObject = DataIOOperations.DataIOOperations()
    oneTimeTaskObject = OneTimeTasks.OneTimeTasks()
    appObject = app_main.App(oneTimeTaskObject, dataIOOperationsObject)


    # operations
    oneTimeTaskObject.addOneTimeTask("test Python code")
    oneTimeTaskObject.addOneTimeTask("Write some more code")
    #print(oneTimeTaskObject.getActiveOneTimeTasks())
    #print()
    oneTimeTaskObject.markTaskAsCompleted(1)
    # print(oneTimeTaskObject.getActiveOneTimeTasks())
    # print()
    # print(oneTimeTaskObject.getCompletedOneTimeTasks())
    appObject.onCloseOperations()

if __name__ == "__main__":
    testOneTimeTasks()
