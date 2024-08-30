import requests

API_BASE_URL = "http://api.openweathermap.org/geo/1.0"
API_KEY = "f897a99d971b5eef57be6fafa0d83239"


def get_coordinates_by_city_state(city_state):
    url = f"{API_BASE_URL}/direct"
    params = {
        'q': f"{city_state},US",
        'limit': 1,
        'appid': API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data[0] if data else None


def get_coordinates_by_zip(zip_code):
    url = f"{API_BASE_URL}/zip"
    params = {
        'zip': f"{zip_code},US",
        'appid': API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data if data else None
