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
        print(_response.headers)
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


# ------------------------------------------Higher-level functions-----------------------------------

def get_response_from_endpoint_and_store_json(endpoint_parameters: dict) -> None:
    """
    Makes get requests to provided API endpoints using provided parameters and saves 
    the JSON responses. See the below for necessary key names and value examples.

    parameter:
        endpoint_parameters: dict   {
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


def make_requests_and_store_json_responses(all_endpoint_parameters: list[dict] = ALL_ENDPOINTS) -> None:
    """
    Takes in a list of endpoint_parameters dictionaries and calls get_response_from_endpoint_and_store_json
    for each dictionary.
    """
    for endpoint_dictionary in all_endpoint_parameters:
        get_response_from_endpoint_and_store_json(endpoint_dictionary)


# -------------------------------------For Google's pagination-----------------------------------------------

def get_next_page(next_page_token: str, google_endpoint_parameters: dict = ALL_ENDPOINTS[-1]):
    """
    Takes in a next_page_token from a previous API search and uses it 
    """
    json_object = get_json(url=google_endpoint_parameters.get('endpoint'),
                           parameters={'pagetoken': next_page_token,
                                       'key': google_endpoint_parameters['params']['key']})

    return json_object


def main():
    # Sends GET requests using the endpoints and their parameters included in the list and stores the json objects in files.
    make_requests_and_store_json_responses()

    # TODO automate Google pagination.

    # Google page 2
    # json_object = get_next_page("Aap_uECe41Ay0uxoHNwt3D0AN30zMnrgm21rISDF7Kxf6OSzJBXEiHKcz7wunxdmzQvn8Pt0iJZAmGeP00NuXYe-ZeDAuq1m8MjmXkpg5WY1d7B6YzZVDdV-yerFsVi1_4cKd4hJ98fa_hO_fO4mBQ_enThE7A6cTGFPC6Aphcy6DjRv1g2v27pOGXLaTqdRKQy3tz5i54SDMbnMOwHjopbRkZ-nDpSLYJJBzGcZMbn4m8b9w0Y8s6KdTkKHMmGxjW9pqUTG1sdvHoKLAoiV2v01aHQxUn23Z8cccHXT0tGgv-6GiZTZIUy7yR2vjXJ8vLnFGJPW8ilnr4D5uMIQO-GyKT_B3lelTMOydD1_VYf7gwTPNFUlZhkTqnA4p5pTGJDwwHGXq_smtMNptrXGPxMklHD6kfrZQCkw9WDBRqgbREUfpjLaUQqs5QuH9M1I")
    # store_response_json(json_object, 'Google_restaurants_p2.json')

    # Google page 3
    # json_object = get_next_page("Aap_uECwxPUSdlxWhJTI4DMmOFYL1oOHQ90cX8oDhMSdW6Fh5a5H2R8S-UUTHbxLnUfu1mRXOXnw2hZIvGQas-2XPKnooyrtv5611sTDFwmspwinVyYpsmhXuwjI7BwWNQyoAEscSSHtzff8yxcwPSezn2IOJGqLxzwFhB_0mhbv54f4SSr24dLZC_6I5SDkwDd4qyHBVqTVPpVUPavhO-fgedL6KmROc42vDIivgfX7Mv4Ow4pB4HgcLkN5IV_8NBjv0chdSKq01wK2RyoUp2wYRoXy5oNaJ57DMOe_6Y0tLhZHpSH9wW2oCGn7Ke2F1mNZbVY1oxZMNQOrXz5B7uCYCx3baqMLmlaWPuGgN5Z61zSSRuyjlw9YI2PqLJP8WJAIjOeJoirHWgWq-Q70fs66Ufy7Cw4_fKzCpOkYbaJAK4PPq2ZkLHAu9MrkCr-M0hiYAHqXt2MnYv4Mpfggb3kVqxm7Hp5Xvanz7jT4OGIOGgW6QWQ4GrJWtFg1m1RETHuh2c_QZRtsSH1x0Xcs-NzxRis82fSE9yVWMy4j0RShjKE__sJY_NolCWWIIJljwdVrW4LHTFlShWWmw48dfmFzWXV5JxklHlPZim_M-_Lbmnt2V30DvYE6gsUqaiIQs60DAvr2hUorwhjq5M21GQ")
    # store_response_json(json_object, 'Google_restaurants_p3.json')

    # Runs if this file is executed directly.
if __name__ == '__main__':
    main()
