import app_main

def testOneTimeTasks():
    # definitions
    appObject = app_main.App()
    one_time_tasks_object = appObject.get_one_time_task_object()

    # operations

    one_time_tasks_object.add_one_time_task("Fix This Shit Bug",
                                            priority=8)
    one_time_tasks_object.add_one_time_task("Code for 4 hours",
                                            priority=4)
    one_time_tasks_object.add_one_time_task("Study Japanese for 2 hours",
                                            priority=4)
    one_time_tasks_object.add_one_time_task("Drink some Honey Tea",
                                            priority=0)
    one_time_tasks_object.add_one_time_task("Drink some Hot Chocolate",
                                            priority=0)

    appObject.on_close_operations()

if __name__ == "__main__":
    testOneTimeTasks()
