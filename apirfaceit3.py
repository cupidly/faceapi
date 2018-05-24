import requests
import json

##funnction to retrieve GUID using players username 
def get_guid(x):
    guid = None
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
    guid =(resp['player_id'])
    
    return guid

    
    




name = input("Please input username: ")
request_url = "https://open.faceit.com/data/v4/players/" + get_guid(name) + "/history"

payload = {"player_id":get_guid(name), "limit":2, "from":1}

header = {
    'Authorization': "Bearer e0caffdb-be9c-42cc-8f07-d9e655b56576"
    }

r = requests.get(request_url, params=payload, headers=header)

outcome = r.json()


##dumps the json object into an element
json_str = json.dumps(outcome)


##//load the json to a string
resp = json.loads(json_str)

##//print the resp
print("GUID found for player " + name + ": " + get_guid(name))
print (resp)


input("Press Enter key to exit")


