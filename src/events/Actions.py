from src.operations.PrettyPrinter import PrettyPrinter
from src.operations.UserInputParser import UserInputParser

import sys


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

    def add(self,
            args,
            task_object) -> None:
        task_string = self.UserInputParser.generate_task_string(args=args)
        task_object.add(task_string=task_string)

    def delete(self,
               task_id: str,
               args,
               task_object,
               task_type) -> None:
        try:
            if task_id not in ["completed", "inactive", "active"]:
                raise ValueError

            if args[1] == "all":
                task_object.clear_all_tasks_from_queue(queue=task_id)

            ids_to_delete = self.UserInputParser.generate_list_of_ids(args=args)
            task_object.delete_from_queue(queue=task_id,
                                          list_of_ids_to_delete=ids_to_delete)
                if args[1] == "all":
                    if task_type == "task":
                        task_object.
                    elif task_type == "habit":
                        task_object.clear_all_inactive_tasks()
                else:
                    ids_to_delete = self.UserInputParser.generate_list_of_ids(args[1:])

                    if task_id == "completed":
                        task_object.delete_completed(list_of_ids_to_delete=ids_to_delete)
                    elif task_id == "inactive":
                        task_object.delete_inactive(list_of_ids_to_delete=ids_to_delete)
                    else:
                        raise ValueError
        except ValueError as e:
            sys.exit(f"The {task_id} action is not available on {task_type}")

    def update(self, args, task_object) -> None:
        # TODO: implement updating priorities / weight / dates
        try:
            if type(args[0]) is int:
                id_to_update = int(args[0])
                properties = self.UserInputParser.find_properties(args=args[1:])

                for key, value in properties.items():
                    task_object.update(id_to_update=id_to_update,
                                       option_to_update=key,
                                       updated_value=value)
                task_string = self.UserInputParser.generate_task_string(args[1:])

                if task_string:
                    task_object.update(id_to_update=id_to_update,
                                       option_to_update="task_string",
                                       updated_value=task_string)
            elif "id" in args:
                raise NotImplementedError
            else:
                raise TypeError
        except TypeError as err:
            print(err)
            sys.exit("update needs an id to update")
        except NotImplementedError:
            sys.exit("Using id: isn't implemented yet. Sorry!")

    def unmark(self, task_type, task_object, args) -> None:
        ids_to_unmark = self.UserInputParser.generate_list_of_ids(args)
        if task_type == "task":
            task_object.unmark_completed(list_of_ids_to_unmark=ids_to_unmark)
        elif task_type == "habit":
            task_object.unmark_completed(list_of_ids_to_unmark=ids_to_unmark)

    def mark(self, task_type, task_object, args, action_type, is_processed=False) -> None:

        try:
            if is_processed:
                ids_to_mark = self.UserInputParser.generate_list_of_ids(args)

                if action_type == "completed":
                    task_object.mark_as_completed(list_of_ids_to_mark_as_completed=ids_to_mark)
                elif action_type == "inactive":
                    task_object.mark_as_inactive(list_of_ids_to_mark_as_inactive=ids_to_mark)
            else:
                if ':' in action_type:
                    property_type, action_type = action_type.split(':')
                    if action_type == "active":
                        raise NotImplementedError
                    elif not (action_type == "completed" or action_type == "inactive"):
                        raise ValueError
                else:
                    action_type = "completed"

                self.mark(task_type=task_type,
                          task_object=task_object,
                          args=args,
                          action_type=action_type,
                          is_processed=True)
        except ValueError as e:
            sys.exit(f"{action_type} not a recognized task status.")
        except NotImplementedError as e:
            sys.exit(f"marking to {action_type} hasn't been implemented yet. Sorry!")
