import requests
import json

name = input("Please input name: ")
payload = {"nickname":name}

header = {
    'Authorization': "Bearer e0caffdb-be9c-42cc-8f07-d9e655b56576"
    }

r = requests.get("https://open.faceit.com/data/v4/players", params=payload, headers=header)

outcome = r.json()


##dumps the json object into an element
json_str = json.dumps(outcome)

##//load the json to a string
resp = json.loads(json_str)

##//print the resp
##print (resp)

##//extract an element in the response
print (resp['nickname'])
print (resp['player_id'])
print (resp['country'])

