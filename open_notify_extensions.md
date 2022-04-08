## Example extensions that can be used in Open-Notify

So now you understand a little how APIs generally work on websites. Lets try practicing with the given methods for the Open-Notify API provides us with.

## ISS Curent Location 

This allows us to see the current location of the International Space Station from whereever it is currently in time. You can observe this API in real time at the [website] ('http://open-notify.org/Open-Notify-API/') as an example as to what it does

## Number of People out in Space

This gives us the identities of the people currently out in space, as well as any relevant associated data that comes with them. Unlike a lot APIs, this one takes in no inputs and just displays the data as is on the webpage. 
Using it is quite simple, import these two libraries `urllib2` and `json`

Set a request variable equal to `req = urllib2.Request("http://api.open-notify.org/iss-now.json")` and a respone variable equal to `response = urllib2.urlopen(req)`. 

Next we must have a variable that reads our response and converts it to a dictionary. We can do that by creating a variable that uses the json.loads operator, like here, `obj = json.loads(response.read())`. 

With this we can use this print as many different combination of values we like, such as `print obj['timestamp']` or `print obj['data']['iss_position']['lattitude']` or even `print obj['iss_position']['lattitude']`


----------------------------------------------------------------------------------
