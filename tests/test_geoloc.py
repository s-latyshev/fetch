from geoloc_util.geoloc import get_coordinates_by_city_state, get_coordinates_by_zip


def test_get_coordinates_by_city_state():
    result = get_coordinates_by_city_state("Madison, WI")
    print(result)
    assert result is not None
    assert result['name'] == "Madison"
    assert result['state'] == "Wisconsin"
    assert result['country'] == "US"
    assert result['lat'] == 43.074761
    assert result['lon'] == -89.3837613


def test_get_coordinates_by_zip():
    result = get_coordinates_by_zip("12345")
    print(result)
    assert result is not None
    assert result['name'] == "Schenectady"
    assert result['country'] == "US"
    assert result['lat'] == 42.8142
    assert result['lon'] == -73.9396


def test_no_data_found_city_state():
    result = get_coordinates_by_city_state("Nonexistent City, ZZ")
    print(result)
    assert result is None


def test_no_data_found_zip():
    result = get_coordinates_by_zip("99999")
    print(result)
    assert result['cod'] == "404"
    assert result['message'] == "not found"
