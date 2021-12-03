from constants import DIRECTORY
import json


def json_from_file(file_name: str, directory: str = DIRECTORY) -> dict:
    """
    Retrieve a JSON object from a file.
    """
    _PATH = f'{directory}{file_name}'  # Concatenate the directory and file name.
    try:
        with open(_PATH) as json_file:
            query_dict = json.load(json_file)
    except FileNotFoundError:
        print(f'{_PATH} does not exist!')

    return query_dict

