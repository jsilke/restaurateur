# Restaurateur ![Issues](https://img.shields.io/github/issues/jsilke/restaurateur) ![Last Commit](https://img.shields.io/github/last-commit/jsilke/restaurateur) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Motivation

This project (adapted from [mini-project-II](https://github.com/lighthouse-labs/mini-project-II) of Lighthouse Labs' Data Science bootcamp) aims to compare API coverage for restaurants in the ByWard Market area of Ottawa, ON, CA.

## Data sources

This project compares data sourced from the following APIs:
- [Foursquare](https://developer.foursquare.com/places)
- [Yelp](https://www.yelp.com/developers/documentation/v3/get_started)
- [Google](https://developers.google.com/maps/documentation/places/web-service/search)

## Project Structure

```bash
.
│   API_requests.py             # Make and store API requests.
│   README.md                   # You are here.
│   constants.py                # Configuration for API queries.
│   data_analysis.ipynb         # Preliminary EDA with pandas.
│   db_setup.py                 # Creates tables in a database.
│   parse_json.py               # Functions to parse API responses.
│   parsing_notes.ipynb         # Brief examples of extracted fields.
│   restaurateur_functions.py   # Functions for creating tables.
```

## Results

See [here](./data_analysis.ipynb) for the preliminary results of this project.