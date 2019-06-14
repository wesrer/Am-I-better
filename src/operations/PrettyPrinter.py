import pandas as pd
import numpy as np

class PrettyPrinter:
    def __init__(self):
        pd.set_option('display.expand_frame_repr', False)
        pd.options.display.max_colwidth = 200

    @staticmethod
    def print_header(header_string):
        print('-'*100)
        print(' '*50, header_string.upper())
        print('-'*100)

    # FIXME: implement actual pretty printing

    @staticmethod
    def pprint(task_dict):
        # for key, value in task_dict.items():
        #     print(key, value['taskString'], value['weight'])

        task_dataframe = pd.DataFrame(task_dict).T
        date_headers = ['assignedOn', 'scheduledStart', 'completeBy']
        for x in date_headers:
            task_dataframe[x] = pd.to_datetime(task_dataframe[x])

        # FIXME: this doesn't work for habits
        colums_to_print = task_dataframe[['taskString', 'completeBy', 'priority', 'weight']]
        print(colums_to_print.sort_values(['completeBy', 'priority']))

