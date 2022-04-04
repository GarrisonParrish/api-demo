### About this demo

[API guide](https://www.nylas.com/blog/use-python-requests-module-rest-apis/)

This is a demo for APIs using Python's requests library. Before we get started, you should download the library using `pip install requests` if prompted, you should update pip to the latest version using `python3 -m pip install --upgrade pip`. Once that's done you can import the requests library into your Python file using `import requests`.

An API (Application Programming Interface) is a way to send data between computers, usually through the Internet through "requests" and "responses". A program sends a request to an API on the web, which fetches that data and sends it back to the program in a simple file format. APIs are very powerful and have many real-world applications.

Many APIs are available on the Internet for free use, and many companies and organizations like Google or NASA have "public APIs" that anyone can get data from. To start this demo, we're going to show you how to get data from a very simple API called Open Notify, which tracks the current location of the ISS and the names of all astronauts currently in space.

[Simple ISS info API](http://api.open-notify.org/)

This simple API has two endpoints: `iss_now` and `astros`. Think of endpoints as functions, each with their own parameters and return values. For example, to get the names of all astronauts currently in space, simply add `"/astros.json"` to the URL. Try opening that URL in your browser. It's a bit of a mess, but you should see some names in what looks like a bunch of Python dictionaries. This is actually a file format called JSON, and it's a common and versatile file type that we can easily translate to Python dictionaries!

Here is a [simple guide](https://www.w3schools.com/python/python_json.asp) to using the JSON format with Python.

[NASA API browser](https://api.nasa.gov/)

Let's try a slightly more complex: NASA's Astronomy Picture of the Day API. All the information for today's APOD is available on their [website](https://apod.nasa.gov/apod/astropix.html), but let's try using the API to get the data in a form we can use! You can also access older APOD data using the `start_date` and `end_date` endpoints.

You will need to sign up for an account with NASA's API service. Once you have made an account, you will get a unique API key, which is used as authorization when you call any of NASA's public APIs. When you call an API, just add `"?api-key=YOUR_API_KEY_HERE"` to the URL.

Since we used the `requests.get` function to retrieve this data from the API, it is in a special object of a class called `Response`, which is something the `requests` library uses to package retrieved data. To get this data in a JSON object, we will call `OBJECT_NAME.json()` function (OBJECT_NAME here is the name of the Response we created). Python translates this JSON object to a dictionary.

There are a lot of steps in this small snippet of code, but once we've retrieved the dictionary with the appropriate data, we are free to use it any way we like in our program! For example, let's say we called the API and got a dictionary that we called `result`. If we want a specific piece of data in this dictionary, like the URL to the picture, all we have to do is get that value with subscript notation: `res2_dict['url']` returns this URL as a string. Try copying this link into your browser!