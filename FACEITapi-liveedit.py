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





def get_matchlength(x):

    payload2 = {"match_id":matchid}
    matchdetails = None

    header = {
    'Authorization': "Bearer e0caffdb-be9c-42cc-8f07-d9e655b56576"
    }

    r = requests.get("https://open.faceit.com/data/v4/matches/" + matchid, headers=header) ## this is owrking whengiven hole url here, can'tmake i work atm using matchid variable

    outcome = r.json()


    ##dumps the json object into an element
    json_str = json.dumps(outcome)

    ##//load the json to a string
    resp = json.loads(json_str)

    ##//print the resp
    ##print (resp)

    ##//extract an element in the response
    matchdetails = resp
    
    return matchdetails
    




name = input("Please input username: ")
request_url = "https://open.faceit.com/data/v4/players/" + get_guid(name) + "/history"

payload = {"player_id":get_guid(name), "limit":15, "from":1}

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
matchid = match1['match_id']
##print(get_matchlength(matchid))
match1result = get_matchlength(matchid)
##print(match1result['configured_at']) ## this works, now gottaa make some for loops


##need loops to put each match id into a list, then run thoguh that list and make new list showing total time of match``
matchidlist = []

##>>> resp['items'][0]['match_id']
##'f9edf087-a812-4b35-829e-df96e0143d35'

##for x in resp['items']:
   ## matchidlist.append ('match_id')
matchcount = 0

for x in resp['items']:
        ##print(resp['items'][matchcount]['match_id'])
        matchidlist.append(resp['items'][matchcount]['match_id'])
        matchcount += 1
    
