import json
import os
import requests as rq
from constants import DIRECTORY, ALL_ENDPOINTS

# -----------------------------------------Low-level functions---------------------------------------------


def get_json(url: str, parameters: dict = None, headers: dict = None) -> rq.Response:
    """
    Send a GET request to the provided url (API endpoint) with optional parameters
    and headers.
    """
    _response = rq.get(url, params=parameters, headers=headers)

    if _response.status_code == 200:
        return _response.json()

    print(f'API returned: {_response.status_code}')


def store_response_json(json_object: dict, file_name: str,
                        directory: str = DIRECTORY) -> None:
    """
    Store response JSON object in a file.
    """
    _PATH = f'{directory}{file_name}'  # Concatenate the directory and file name.

    if not os.path.exists(directory):
        os.mkdir(directory)

    with open(_PATH, 'w') as _json_file:
        json.dump(json_object, _json_file, sort_keys=True, indent=4)


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

# ------------------------------------------Higher-level functions-----------------------------------


def get_response_from_endpoint_and_store_json(endpoint_parameters: dict) -> None:
    """Makes get requests to provided API endpoints using provided parameters
    and saves the JSON responses.

    parameter:
        endpoint parameters: dict   {
                                     'file': 'filename.json'
                                     'endpoint': 'https://api/search'
                                     'params': dict(query_parameters)
                                     'headers': dict(headers)
                                    }
    """
    _json_object = get_json(url=endpoint_parameters.get('endpoint'),
                            parameters=endpoint_parameters.get('params'),
                            headers=endpoint_parameters.get('headers'))

    store_response_json(_json_object,
                        file_name=endpoint_parameters.get('file'))


def make_requests_and_store_json_responses(all_endpoint_parameters: list[dict]) -> None:
    """
    Takes in a list of endpoint_parameters dictionaries and calls get_response_from_endpoint_and_store_json
    for each dictionary.
    """
    for endpoint_dictionary in all_endpoint_parameters:
        get_response_from_endpoint_and_store_json(endpoint_dictionary)


def main():
    # Sends GET requests using the endpoints and their parameters included in the list and stores the json objects in files.
    make_requests_and_store_json_responses(ALL_ENDPOINTS)


# Runs if this file is executed directly.
if __name__ == '__main__':
    main()
