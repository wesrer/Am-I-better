import OneTimeTasks
import DataIOOperations
import app_main


def testOneTimeTasks():
    # definitions
    appObject = app_main.App()
    dataIOOperationsObject = DataIOOperations.DataIOOperations()
    oneTimeTaskObject = OneTimeTasks.OneTimeTasks()

    # operations
    oneTimeTaskObject.addOneTimeTask("test Python code")
    oneTimeTaskObject.addOneTimeTask("Write some more code")
    print(oneTimeTaskObject.getActiveOneTimeTasks())
    print()
    oneTimeTaskObject.markTaskAsCompleted(1)
    print(oneTimeTaskObject.getActiveOneTimeTasks())
    print()
    print(oneTimeTaskObject.getCompletedOneTimeTasks())
    appObject.onCloseOperations()

if __name__ == "__main__":
    testOneTimeTasks()
