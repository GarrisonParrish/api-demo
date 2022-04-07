### About this demo

[API guide](https://www.nylas.com/blog/use-python-requests-module-rest-apis/)

This is a demo for APIs using Python's requests library. Before we get started, you should download the library using `pip install requests` if prompted, you should update pip to the latest version using `python3 -m pip install --upgrade pip`. Once that's done you can import the requests library into your Python file using `import requests`.

An API (Application Programming Interface) is a way to send data between computers, usually through the Internet through "requests" and "responses". A program sends a request to an API on the web, which fetches that data and sends it back to the program in a simple file format. APIs are very powerful and have many real-world applications.

Many APIs are available on the Internet for free use, and many companies and organizations like Google or NASA have "public APIs" that anyone can get data from. To start this demo, we're going to show you how to get data from a very simple API called Open Notify, which tracks the current location of the ISS and the names of all astronauts currently in space.

[Simple ISS info API](http://api.open-notify.org/)

This simple API has two endpoints: `iss_now` and `astros`. Think of endpoints as functions, each with their own parameters and return values. For example, to get the names of all astronauts currently in space, simply add `"/astros.json"` to the URL. Try opening that URL in your browser. It's a bit of a mess, but you should see some names in what looks like a bunch of Python dictionaries. This is actually a file format called JSON, and it's a common and versatile file type that we can easily translate to Python dictionaries!

Here is a [simple guide](https://www.w3schools.com/python/python_json.asp) to using the JSON format with Python.

[NASA API browser](https://api.nasa.gov/)

[NASA Astronomy Picture of the Day](https://github.com/nasa/apod-api)

Let's try a slightly more complex: NASA's Astronomy Picture of the Day (APOD) API. All the information for today's APOD is available on their [website](https://apod.nasa.gov/apod/astropix.html), but let's try using the API to get the data in a form we can use! [Here](https://github.com/nasa/apod-api) is the full documentation for the API--scroll down to "Docs" to see descriptions of the different endpoints. We will cover how to use these endpoints soon.

You will need to sign up for an account with NASA's API service. Once you have made an account, you will get a unique API key, which is used as authorization when you call any of NASA's public APIs. When you call an API, just add `"?api-key=YOUR_API_KEY_HERE"` to the end of the URL.

Since we used the `requests.get` function to retrieve this data from the API, it is in a special object of a class called `Response`, which is something the `requests` library uses to package retrieved data. To get this data in a JSON object, we will call `OBJECT_NAME.json()` function (OBJECT_NAME here is the name of the Response we created). Python translates this JSON object to a dictionary.

There are a lot of steps in this small snippet of code, but once we've retrieved the dictionary with the appropriate data, we are free to use it any way we like in our program! For example, let's say we called the API and got a dictionary that we named `result`. If we want a specific piece of data in this dictionary, like the URL to the picture, all we have to do is lookup the key with subscript notation: `res2_dict['url']` returns this URL as a string. Try copying this link into your browser to see the image!

You can see a table of the API's endpoints on the website. To specify an endpoint in the request, follow this format in the request URL:

    https://api.nasa.gov/planetary/apod?api_key=INSERT_KEY&ENDPOINT_NAME=ARG

To specify multiple endpoints, just chain &ENDPOINT_NAME=ARG statements one after the other. Make sure to include the & before the endpoint. For example, 

    https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&start_date=2017-07-08&end_date=2017-07-10

will return a list of 3 APOD data for 7/8/2017, 7/9/2017, and 7/10/2017.

Note: if date input does not match the YYYY-MM-DD (4-digit year, 2-digit month, 2-digit day) format, you will get a 'bad request' result that looks something like this:
`{'code': 400, 'msg': "time data '2005-06-0' does not match format '%Y-%m-%d'", 'service_version': 'v1'}`
This can be tricky to work around in some cases. If you want a better way to format dates, take a look at the
`datetime` library. [Here](https://www.geeksforgeeks.org/python-validate-string-date-format/) is a helpful guide on using that library.