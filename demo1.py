import requests

# 'Open Notify' API endpoint URLs
iss_now: str = "http://api.open-notify.org/iss-now.json"
astros: str = "http://api.open-notify.org/astros.json"
joke = "https://official-joke-api.appspot.com/random_joke"

# using the requests library's get function to call the API, store data as a variable
response = requests.get(iss_now)  # don't worry about the type, Python will take care of this
print(response.json())