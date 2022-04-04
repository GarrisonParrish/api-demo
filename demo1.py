import requests

# 'Open Notify' API endpoint URLs
iss_now: str = "http://api.open-notify.org/iss-now.json"
astros: str = "http://api.open-notify.org/astros.json"
joke = "https://official-joke-api.appspot.com/random_joke"

# using the requests library's get function to call the API, store data as a variable
response = requests.get(joke)  # don't worry about the type, Python will take care of this
print(response.json())

API_KEY = "LbtwFYA0AeXnVCgWt6Gs9MUXbAgCrDXBNQ5mkYO1"

res2 = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}")
res2_dict: dict = res2.json()
print(res2)
print(res2_dict['url'])