import pandas as pd
import numpy as np
from typing import Dict
import sys


class PrettyPrinter:
    def __init__(self):
        pd.set_option('display.expand_frame_repr', False)
        pd.options.display.max_colwidth = 200

    @staticmethod
    def print_header(header_string):
        print('-'*150)
        print(' '*70, header_string.upper())
        print('-'*150)

    # FIXME: implement actual pretty printing

    @staticmethod
    def pprint(task_dict: Dict[str, str],
               task_type: str,
               queue: str = "active",
               default_behavior_exit: bool = True):

        if len(task_dict) == 0:
            if default_behavior_exit:
                sys.exit("No items to display.")
            else:
                print("No items to display.")
                return


        # loading the dictionary as a DataFrame
        task_dataframe = pd.DataFrame(task_dict)

        # we need to transpose because in the JSON, the data is organized under their id's
        # translating them into column headers but we want their attributes as column headers
        task_dataframe = task_dataframe.T
        task_dataframe['id'] = task_dataframe.index

        date_headers = []
        columns_to_print = task_dataframe
        sort_by = []

        # FIXME: these need to updated to cover custom queues
        if task_type in ["task", "tasks"]:
            if queue == "active":
                date_headers = ['assignedOn', 'scheduledStart', 'completeBy']
                columns_to_print = task_dataframe[['taskString', 'completeBy','priority', 'weight']]
                sort_by = ['completeBy', 'priority', 'weight']
            elif queue == "inactive":
                date_headers = ['assignedOn', 'scheduledStart']
                columns_to_print = task_dataframe[['taskString', 'scheduledStart', 'priority', 'weight']]
                sort_by = ['priority', 'weight', 'scheduledStart']

        elif task_type in ["habit", "habits"]:
            date_headers = ['assignedOn', 'scheduledStart']
            columns_to_print = task_dataframe[['taskString', 'priority', 'weight', 'refreshRate']]
            sort_by = ['priority', 'weight']

        for x in date_headers:
            task_dataframe[x] = pd.to_datetime(task_dataframe[x])

        # FIXME: longTermTasks not implemented
        print(columns_to_print.sort_values(sort_by))

