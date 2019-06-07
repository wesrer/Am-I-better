from src.operations.PrettyPrinter import PrettyPrinter


class Actions:
    def __int__(self):
        self.PrettyPrinter = PrettyPrinter()

    def list_tasks_by_category(self, task_type, dictionary):
        PrettyPrinter.pprint(dictionary)

    def list_all(self, action_type, ):
        if action_type in ["active", "list", "view"]:
            self.PrettyPrinter.print_header("habits")
            self.list_tasks_by_category(task_type="habit")

            self.PrettyPrinter.print_header("tasks")
            self.list_tasks_by_category(task_type="task")
            return
