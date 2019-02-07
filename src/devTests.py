import app_main
from pathlib import Path

def testOneTimeTasks():
    # definitions
    appObject = app_main.App()
    oneTimeTaskObject = appObject.getOneTimeTaskObject()

    # operations
    # oneTimeTaskObject.addOneTimeTask("Fix This Shit Bug")
    # oneTimeTaskObject.addOneTimeTask("Code for 4 hours")
    # oneTimeTaskObject.addOneTimeTask("Study Japanese for 2 hours")
    # oneTimeTaskObject.addOneTimeTask("Drink some Honey Tea")
    # oneTimeTaskObject.addOneTimeTask("Drink some Hot Chocolate")
    # oneTimeTaskObject.addOneTimeTask("")
    # print(oneTimeTaskObject.getActiveOneTimeTasks())
    # print()
    # oneTimeTaskObject.markTaskAsCompleted(1)
    oneTimeTaskObject.addOneTimeTask("Test the new feature")
    # print(oneTimeTaskObject.getActiveOneTimeTasks())
    # print()
    # print(oneTimeTaskObject.getCompletedOneTimeTasks())
    appObject.onCloseOperations()


def reInitializeData():
    pass


if __name__ == "__main__":
    testOneTimeTasks()
