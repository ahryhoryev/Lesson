# Dict with countries and cities

countries_and_cities = {
    "Belarus": ["Minsk", "Bobruysk", "Mogilev"],
    "USA": ["Washington", "Boston", "Chicago"],
    "Italy": ["Rome", "Milan"],
    "Germany": ["Berlin"]
}


def find_country_by_city():
    city_from_search = input("Enter city name: ")  # Input city for search
    for key, value in countries_and_cities.items():  # Run cycle and splitting values
        if str(city_from_search).lower() in str(value).lower():  # Transform text and value to lowercase and check
            print(key)


find_country_by_city()
