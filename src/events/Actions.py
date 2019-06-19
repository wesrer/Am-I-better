from src.operations.PrettyPrinter import PrettyPrinter
from src.operations.UserInputParser import UserInputParser


class Actions:
    def __init__(self):
        self.PrettyPrinter = PrettyPrinter()
        self.UserInputParser = UserInputParser()

    def list_tasks_by_category(self, task_type, dictionary):
        PrettyPrinter.pprint(dictionary)

    def list_all(self, action_type, ):
        if action_type in ["active", "list", "view"]:
            self.PrettyPrinter.print_header("habits")
            self.list_tasks_by_category(task_type="habit")

            self.PrettyPrinter.print_header("tasks")
            self.list_tasks_by_category(task_type="task")
            return

    def delete(self, task_id: str, args, task_object, task_type) -> None:

        if not (task_id == "completed" or task_id == "inactive"):
            ids_to_mark = self.UserInputParser.generate_list_of_ids(args=args)
            task_object.delete_active(list_of_ids_to_delete=ids_to_mark)
        else:
            if args[1] == "all":
                if task_type == "task":
                    task_object.clear_all_completed_tasks()
                elif task_type == "habit":
                    task_object.clear_all_inactive_tasks()
            else:
                ids_to_delete = self.UserInputParser.generate_list_of_ids(args[1:])
                if task_id == "completed":
                    if task_type == "task":
                        task_object.delete_completed(list_of_ids_to_delete=ids_to_delete)
                    elif task_type == "habit":
                        task_object.delete_completed(list_of_ids_to_delete=ids_to_delete)
                elif task_id == "inactive":
                    if task_type == "habit":
                        task_object.delete_inactive(list_of_ids_to_delete=ids_to_delete)
                    else:
                        raise ValueError(f"The {task_id} action is not available on {task_type}")
