import app_main
from pathlib import Path

def testOneTimeTasks():
    # definitions
    appObject = app_main.App()
    oneTimeTaskObject = appObject.get_one_time_task_object()

    # operations


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
