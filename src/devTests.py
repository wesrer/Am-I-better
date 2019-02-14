import app_main
from pathlib import Path

def testOneTimeTasks():
    # definitions
    appObject = app_main.App()
    oneTimeTaskObject = appObject.get_one_time_task_object()

    # operations
    oneTimeTaskObject.addOneTimeTask("Fix This Shit Bug")
    oneTimeTaskObject.addOneTimeTask("Code for 4 hours")
    oneTimeTaskObject.addOneTimeTask("Study Japanese for 2 hours")
    oneTimeTaskObject.addOneTimeTask("Drink some Honey Tea")
    oneTimeTaskObject.addOneTimeTask("Drink some Hot Chocolate")
    # oneTimeTaskObject.addOneTimeTask("")
    # print(oneTimeTaskObject.getActiveOneTimeTasks())
    # print()
    oneTimeTaskObject.markTaskAsCompleted(1)
    oneTimeTaskObject.add_one_time_task("Test the new feature")
    # print(oneTimeTaskObject.getActiveOneTimeTasks())
    # print()
    # print(oneTimeTaskObject.getCompletedOneTimeTasks())
    appObject.on_close_operations()


def reInitializeData():
    pass

if __name__ == "__main__":
    testOneTimeTasks()
