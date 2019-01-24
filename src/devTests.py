import OneTimeTasks

def testOneTimeTasks():
    oneTimeTaskObject = OneTimeTasks.OneTimeTasks()
    oneTimeTaskObject.addOneTimeTask("test Python code")
    oneTimeTaskObject.saveOneTimeTasks()
    

if __name__ == "__main__":
    testOneTimeTasks()
