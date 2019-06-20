from fire import Fire
from src import AppMain

from src.operations.PrettyPrinter import PrettyPrinter
from src.operations.UserInputParser import UserInputParser
from src.events.Actions import Actions

import sys

app = AppMain.App()

PrettyPrinter = PrettyPrinter()
UserInputParser = UserInputParser()
Actions = Actions()


def parse_cli(task_type,
              action_type="list",
              *args):

    task_type = task_type.lower()

    app.on_start_operations()

    perform_actions(task_type=task_type,
                    action_type=action_type,
                    args=args)

    app.on_close_operations()


# FIXME: refactor this?
def perform_actions(task_type,
                    action_type,
                    args,
                    weight=3):

    try:
        if task_type not in ["all", "test", "pandas"]:
            obj = parse_task(task_type=task_type)

        elif task_type == "pandas":
            app.get_pandas().print_active()
            return

        elif action_type in ["list", "view", "active"]:
            PrettyPrinter.print_header("habits")
            perform_actions(task_type="habit", action_type="list", args=[])

            PrettyPrinter.print_header("tasks")
            perform_actions(task_type="task", action_type="list", args=[])
            return

        elif task_type == "test":
            print(UserInputParser.generate_task_string(args=args))
            return

        if action_type == "add":
            task_string = UserInputParser.generate_task_string(args=args)
            obj.add(task_string=task_string)

        elif action_type in ['update', 'edit']:
            # TODO: implement updating priorities / weight / dates
            try:
                if type(args[0]) is int:
                    id_to_update = int(args[0])
                    properties = UserInputParser.find_properties(args=args[1:])

                    for key, value in properties.items():
                        obj.update(id_to_update=id_to_update,
                                   option_to_update=key,
                                   updated_value=value)
                    task_string = UserInputParser.generate_task_string(args[1:])

                    if task_string:
                        obj.update(id_to_update=id_to_update,
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

        elif action_type in ["active", "list", "view"]:
            PrettyPrinter.pprint(task_dict=obj.get_active(), task_type=task_type)

        elif action_type == "completed":
            if len(args) == 0:
                PrettyPrinter.pprint(task_dict=obj.get_completed(), task_type=task_type)

        elif action_type == "delete" or action_type == "del":
            task_id = args[0]

            Actions.delete(task_id=task_id, args=args, task_object=obj, task_type=task_type)

        elif action_type == "mark":
            ids_to_mark = UserInputParser.generate_list_of_ids(args)

            if task_type == "task":
                obj.mark_as_completed(list_of_ids_to_mark_as_completed=ids_to_mark)
            elif task_type == "habit":
                obj.mark_as_completed(list_of_ids_to_mark_as_completed=ids_to_mark)

        # TODO: implement unmarking inactive habits
        elif action_type == "unmark":
            ids_to_unmark = UserInputParser.generate_list_of_ids(args)
            if task_type == "task":
                obj.unmark_completed(list_of_ids_to_unmark=ids_to_unmark)
            elif task_type == "habit":
                obj.unmark_completed(list_of_ids_to_unmark=ids_to_unmark)

        else:
            raise ValueError
    except ValueError:
        sys.exit(f"{action_type} is not a valid action on {task_type}")


def parse_task(task_type: str):

    try:
        if task_type == 'task':
            task_object = app.get_one_time_task_object()
        elif task_type == 'habit':
            task_object = app.get_habit_object()
        else:
            raise ValueError
    except ValueError:
        sys.exit("task type is not recognized")

    return task_object


if __name__ == '__main__':
    Fire(parse_cli)
