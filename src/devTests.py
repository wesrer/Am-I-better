import app_main
from pathlib import Path

def testOneTimeTasks():
    # definitions
    appObject = app_main.App()
    oneTimeTaskObject = appObject.get_one_time_task_object()

    # operations
    oneTimeTaskObject.addOneTimeTask("Fix This Shit Bug",
                                     priority=8)
    oneTimeTaskObject.addOneTimeTask("Code for 4 hours",
                                     priority=4)
    oneTimeTaskObject.addOneTimeTask("Study Japanese for 2 hours",
                                     priority=4)
    oneTimeTaskObject.addOneTimeTask("Drink some Honey Tea",
                                     priority=0)
    oneTimeTaskObject.addOneTimeTask("Drink some Hot Chocolate",
                                     priority=0)
    # oneTimeTaskObject.addOneTimeTask("")
    # print(oneTimeTaskObject.getActiveOneTimeTasks())
    # print()
    oneTimeTaskObject.markTaskAsCompleted(1)
    oneTimeTaskObject.add_one_time_task("Test the new feature",
                                        priority=0)
    # print(oneTimeTaskObject.getActiveOneTimeTasks())
    # print()
    # print(oneTimeTaskObject.getCompletedOneTimeTasks())
    appObject.on_close_operations()


def reInitializeData():
    pass

if __name__ == "__main__":
    testOneTimeTasks()
