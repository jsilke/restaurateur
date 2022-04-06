from constants import (
    DIRECTORY,
    FOURSQUARE_LEGEND_DISCREPANCIES,
    YELP_LEGEND_DISCREPANCIES,
    GOOGLE_LEGEND_DISCREPANCIES,
)
import json
import pandas as pd


def json_from_file(file_name: str, directory: str = DIRECTORY) -> dict:
    """
    Retrieve a JSON object from a file.
    """
    _PATH = f"{directory}{file_name}"  # Concatenate the directory and file name.
    try:
        with open(_PATH) as json_file:
            query_dict = json.load(json_file)
    except FileNotFoundError:
        print(f"{_PATH} does not exist!")

    return query_dict


def parse_object_to_df(
    json_object: dict, results_key: str = "results", legend_discrepencies: dict = None
) -> pd.DataFrame:
    """
    Takes in a JSON object, key to the results list, and a legend which is applied to extract
    the desired data. The resulting object is then converted to a pandas DataFrame and returned.

    parameters:
        json_object: dict = the JSON object to parse
        results_key: str = the key to the results list
        legend_exceptions: dict = dict('column_key': 'json_key_to_replace')
    """
    _legend_template = {
        "Name": "name",
        "Price": "price",
        "Type": "types",
        "Rating": "rating",
        "RatingCount": "review_count",
        "Source": "unknown",
    }

    # Adjust discrepencies in the key names of the data to be parsed
    for key, value in legend_discrepencies.items():
        _legend_template[key] = value

    # set the column names based on legend values
    _pre_df = {column_key: [] for column_key in _legend_template}
    _key_list = json_object[results_key]
    print(len(_key_list))
    # As long as the key list isn't empty, pop out the last element and store it.
    while _key_list:
        _current = _key_list.pop()
        # Use the corresponding key_value pairs in the legend to add to the column.
        for column_key, json_key in _legend_template.items():
            if column_key != "Source":
                _pre_df[column_key].append(_current.get(json_key))
            else:
                _pre_df[column_key].append(json_key)

    return pd.DataFrame.from_dict(_pre_df)


def post_process_series(column: pd.Series, key: str = "total_ratings") -> pd.Series:
    """
    Takes in a column (Series) and a key, converts the column to a dictionary
    and applies the key to each element to get the nested values. Returns the
    processed column.
    """
    _temp = column.to_dict()
    for integer, element in _temp.items():
        if element:
            # For elements that aren't None, get the nested values.
            _temp[integer] = element.get(key)

    return pd.Series(_temp)


def main():
    # ----------------------------------Preview Foursquare-----------------------------------
    # json_obj = json_from_file('Foursquare_restaurants.json')
    # df = parse_object_to_df(
    #     json_obj, legend_discrepencies=FOURSQUARE_LEGEND_DISCREPANCIES)
    # # extra processing step for ratings, just need to cooerce them to int somehow...or not.
    # df['RatingCount'] = post_process_series(df['RatingCount'])
    # print(df.head(10))

    # ------------------------------------Preview Yelp--------------------------------------
    # json_obj = json_from_file('Yelp_restaurants.json')
    # df = parse_object_to_df(
    #     json_obj, 'businesses', legend_discrepencies=YELP_LEGEND_DISCREPANCIES)
    # print(df.head(10))

    # -----------------------------------Preview Google--------------------------------------
    # json_obj = json_from_file('Google_restaurants.json')
    # df = parse_object_to_df(
    #     json_obj, legend_discrepencies=GOOGLE_LEGEND_DISCREPANCIES)
    # print(df.head(10))
    # NOTE: Google results are currently divided across 3 files.
    pass


if __name__ == "__main__":
    main()
