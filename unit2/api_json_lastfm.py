import json
import requests

def api_get_request(url):
    data = requests.get(url).text
    data = json.loads(data)
    # for x in xrange(50):
    #     print data["topartists"]["artist"][x]["name"]
    #     print data["topartists"]["artist"][x]["@attr"]["rank"]
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    
    return data["topartists"]["artist"][0]["name"]

url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=69fba4756bd1ab3813d8ec59bd5a0def&format=json'
print api_get_request(url)