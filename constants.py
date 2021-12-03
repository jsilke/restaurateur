import os


DIRECTORY = './data/'
# -------------------------------Foursquare Places API--------------------------------------------

FOURSQUARE_ENDPOINT = 'https://api.foursquare.com/v3/places/search'
FOURSQUARE_HEADERS = {
    'Accept': 'application/json',
    'Authorization': os.getenv('foursquare')
}
FOURSQUARE_PARAMS = {
    # 'cursor': 'c3I6NTA',  # NOTE Pagination needs cursor from header link
    'll': '45.429123,-75.691283',  # ~center of Google's ByWard Market area
    'radius': 330,                 # int, in meters
    'categories': '13065',         # restaurants
    'fields': 'name,location,rating,stats,price,tastes',
    'limit': 50                    # 50 is the most a 'Places' search will return
}
FOURSQUARE_DICT = {
    'file': 'Foursquare_restaurants_p1.json',  # NOTE PAGINATION
    'endpoint': FOURSQUARE_ENDPOINT,
    'params': FOURSQUARE_PARAMS,
    'headers': FOURSQUARE_HEADERS
}
FOURSQUARE_LEGEND_DISCREPANCIES = {
    'Source': 'Foursquare',
    'Type': 'tastes',
    # This will need further processing.
    'RatingCount': 'stats'
}

# ---------------------------------Yelp Fusion API-----------------------------------------------

YELP_ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
YELP_HEADERS = {'Authorization': f"Bearer {os.getenv('yelp_api_key')}"}
YELP_PARAMS = {
    'latitude': 45.429123,
    'longitude': -75.691283,
    'radius': 330,
    'categories': 'restaurants,All',
    'limit': 50                        # 50 is the max here as well.
}
YELP_DICT = {
    'file': 'Yelp_restaurants.json',
    'endpoint': YELP_ENDPOINT,
    'params': YELP_PARAMS,
    'headers': YELP_HEADERS
}
YELP_LEGEND_DISCREPANCIES = {
    'Source': 'Yelp',
    'Type': 'categories'
}

# ------------------------------------Google Place Search API-----------------------------------

GOOGLE_ENDPOINT = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
GOOGLE_PARAMS = {
    'location': '45.429123,-75.691283',
    'radius': 330,
    'type': 'restaurant',
    'key': os.getenv('google_maps_key')
}
GOOGLE_DICT = {
    'file': 'Google_restaurants_p1.json',  # NOTE Pagination
    'endpoint': GOOGLE_ENDPOINT,
    'params': GOOGLE_PARAMS
}
GOOGLE_LEGEND_DISCREPANCIES = {
    'Source': 'Google',
    'Price': 'price_level',
    'RatingCount': 'user_ratings_total'
}


ALL_ENDPOINTS = [FOURSQUARE_DICT, YELP_DICT, GOOGLE_DICT]
