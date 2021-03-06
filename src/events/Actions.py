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

    # FIXME:
    def delete(self,
               queue: str,
               args,
               task_object,
               task_type) -> None:
        try:
            if queue == "completed" or queue == "inactive":
                if args[1] == "all":
                    task_object.clear_all_tasks_from_queue(queue=queue)
                else:
                    ids_to_delete = self.UserInputParser.generate_list_of_ids(args[1:])

                    task_object.delete_from_queue(list_of_ids_to_delete=ids_to_delete,
                                                  queue=queue)
            elif queue == "active":
                ids_to_delete = self.UserInputParser.generate_list_of_ids(args=args)
                task_object.delete_from_queue(queue=queue,
                                              list_of_ids_to_delete=ids_to_delete)

        except ValueError as e:
            sys.exit(f"The {queue} action is not available on {task_type}")

    def update(self, args, task_object) -> None:
        # TODO: implement updating priorities / weight / dates
        try:
            ids_to_update = self.UserInputParser.generate_list_of_ids(args=args)
            properties = self.UserInputParser.find_properties(args=args)

            if len(ids_to_update) == 0:
                raise TypeError

            for key, value in properties.items():
                task_object.update(ids_to_update=ids_to_update,
                                   option_to_update=key,
                                   updated_value=value)

            task_string = self.UserInputParser.generate_task_string(args)

            if task_string:
                task_object.update(ids_to_update=ids_to_update,
                                   option_to_update="task_string",
                                   updated_value=task_string)
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
