import OneTimeTasks
import DataIOOperations


def testOneTimeTasks():
    dataIOOperationsObject = DataIOOperations.DataIOOperations()
    dataIOOperationsObject.initializeIDs()
    dataIOOperationsObject.writeUniqueIDs()
    oneTimeTaskObject = OneTimeTasks.OneTimeTasks()
    oneTimeTaskObject.addOneTimeTask("test Python code")
    oneTimeTaskObject.saveActiveOneTimeTasks()
    

if __name__ == "__main__":
    testOneTimeTasks()
