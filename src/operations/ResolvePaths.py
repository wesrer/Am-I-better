from pathlib import Path


class ResolvePaths:
    def __init__(self,
                 module_path: str,
                 execution_type: str = "test"):
        self.module_path_resolution = Path(module_path)
        self.execution_type = execution_type

    def default_values_path(self):
        return self.data_directory_path() / 'defaultValues.json'

    def unique_ids_path(self):
        return self.data_directory_path() / 'uniqueIDs.json'

    def data_directory_path(self):
        if self.execution_type.lower() == "dev" or self.execution_type.lower() == "build":
            return self.module_path_resolution / '..' / 'data'
        elif self.execution_type.lower() == "test":
            return self.module_path_resolution / '..' / 'tests' / 'test_data'

