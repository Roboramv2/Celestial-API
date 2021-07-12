import json
import requests

apiurl = "https://celestial-api.herokuapp.com/"

def getdata(typ, name):
    response = requests.post(apiurl+"getdata", json = {"body": typ, "name":name})
    print(response.json())

# "type" can be "planets", "moons", "asteroids", "stars", "blackholes"
# "name" must be capitalised
getdata("planets", "Jupiter")