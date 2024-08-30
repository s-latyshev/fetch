import shlex
from .geoloc import get_coordinates_by_city_state, get_coordinates_by_zip


def process_locations(locations):
    results = []
    for location in locations:
        if "," in location:
            result = get_coordinates_by_city_state(location)
        else:
            result = get_coordinates_by_zip(location)
        if result:
            place_name = f"{result.get('name')}, {result.get('state')}" if 'state' in result else result.get('name')
            country = result.get('country')
            lat = result.get('lat')
            lon = result.get('lon')
            results.append(f"Location: {place_name}, {country} | Latitude: {lat} | Longitude: {lon}")
        else:
            results.append(f"No data found for {location}")

    return results


def main():
    print("Welcome to the Geolocation Utility!")
    input_string = input("Enter locations: ")
    locations = shlex.split(input_string)
    if locations:
        results = process_locations(locations)
        for result in results:
            print(result)


if __name__ == '__main__':
    main()
