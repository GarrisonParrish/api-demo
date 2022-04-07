"""This is a guide on how to use NASA's Astronomy Picture of the Day API."""

import requests

# Once you have signed up for a NASA API key, you can use it to access any of their public APIs.
# Your API key will be a long string of numbers and letters. Copy it and replace DEMO_KEY below.
API_KEY = "DEMO_KEY"

# HTTPS request format: GET https://api.nasa.gov/planetary/apod
# We will use the requests library to send requests to the API

# Get today's APOD
def get_today() -> dict[str, str]:
    """Get today's APOD data as a Python dictionary."""
    response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}")
    response_dict: dict[str, str] = response.json()   # get the response data in JSON format
    return response_dict

def get_date(date: str) -> dict[str, str]:
    """Get APOD data on a given date. Date format YYYY-MM-DD."""
    response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&date={date}")
    response_dict: dict[str, str] = response.json()   # get the response data in JSON format
    return response_dict

def get_date_range(start_date: str, end_date: str) -> list[dict[str, str]]:
    """Get list of APOD data over a given range of dates. Date format YYYY-MM-DD."""
    response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&start_date={start_date}&end_date={end_date}")
    response_dict: dict[str, str] = response.json()   # get the response data in JSON format
    return response_dict

# print(get_date_range("2005-06-05", "2005-06-08"))

def get_field(dict_list: list[dict[str, str]], field_name: str) -> list[str]:
    result: list[str] = []
    for i in dict_list:
        result.append(i[field_name])

def main() -> None:
    res = get_date("2005-06-05")
    print(res)