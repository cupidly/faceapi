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
##print (resp)
##print(resp['items'][1]) ##orints out second match in that dictionary
match1 = resp['items'][0] ## puts first match into it's own dictionsary can then print its vars with print(match1['match_id'])
match2 = resp['items'][1]

matchlist = [match1['match_id'], match2['match_id']]
print('These are the players last matches: ' + str(matchlist))

