from os import path
import src
from pathlib import Path


class ResolvePaths:
    def __init__(self):
        self.module_path = path.dirname(src.__file__)
        self.module_path_resolution = Path(self.module_path)

    def default_values_path(self):
        return self.data_directory_path() / 'defaultValues.json'

    def unique_ids_path(self):
        return self.data_directory_path() / 'uniqueIDs.json'

    def data_directory_path(self):
        return self.module_path_resolution / '..' / 'data'

