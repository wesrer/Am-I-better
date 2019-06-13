import pandas as pd
import numpy as np


class PandasTest:
    def __init__(self,
                 one_time_tasks_object):
        self.oneTimeTasks = one_time_tasks_object

    def print_active(self):
        pd.set_option('display.expand_frame_repr', False)
        print(pd.DataFrame(self.oneTimeTasks.get_active()).T)

