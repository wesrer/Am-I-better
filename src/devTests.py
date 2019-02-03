import app_main

def testOneTimeTasks():
    # definitions
    appObject = app_main.App()
    oneTimeTaskObject = appObject.getOneTimeTaskObject()


    # operations
    # oneTimeTaskObject.addOneTimeTask("Fix this shit bug")
    # oneTimeTaskObject.addOneTimeTask("Code for 4 hours")
    # oneTimeTaskObject.addOneTimeTask("Study Japanese for 2 hours")
    # print(oneTimeTaskObject.getActiveOneTimeTasks())
    # print()
    oneTimeTaskObject.markTaskAsCompleted(1)
    # print(oneTimeTaskObject.getActiveOneTimeTasks())
    # print()
    # print(oneTimeTaskObject.getCompletedOneTimeTasks())
    appObject.onCloseOperations()

if __name__ == "__main__":
    testOneTimeTasks()
