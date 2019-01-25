import OneTimeTasks
import DataIOOperations
import app_main


def testOneTimeTasks():
    # definitions
    appObject = app_main.App()
    dataIOOperationsObject = DataIOOperations.DataIOOperations()
    oneTimeTaskObject = OneTimeTasks.OneTimeTasks()

    # operations
    dataIOOperationsObject.initializeIDs()
    dataIOOperationsObject.writeUniqueIDs()
    oneTimeTaskObject.addOneTimeTask("test Python code")
    oneTimeTaskObject.saveActiveOneTimeTasks()

    

if __name__ == "__main__":
    testOneTimeTasks()
