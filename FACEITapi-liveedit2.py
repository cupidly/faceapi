import requests
import json
from statistics import mean ##adds the mean average function
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
game = input("Please type game: dota2 or csgo: ")
print("Gathering data...")
request_url = "https://open.faceit.com/data/v4/players/" + get_guid(name) + "/history"

payload = {"player_id":get_guid(name),"game":game, "limit":50, "from":1}

header = {
    'Authorization': "Bearer e0caffdb-be9c-42cc-8f07-d9e655b56576"
    }

r = requests.get(request_url, params=payload, headers=header)

outcome = r.json()


##dumps the json object into an element
json_str = json.dumps(outcome)


##//load the json to a string
resp = json.loads(json_str)


print("GUID found for player " + name + ": " + get_guid(name))

matchidlist = []
matchcount = 0

for x in resp['items']:
        ##print(resp['items'][matchcount]['match_id'])
        matchidlist.append(resp['items'][matchcount]['match_id'])
        matchcount += 1


##matchlist = [match1['match_id'], match2['match_id']]
print('Collected data from ' + str(len(matchidlist)) + ' matches.')
##print('These are the players last matches: ' + str(matchidlist))

matchcount = 0
matchtimelist = []
for x in resp['items']:
        ##print(resp['items'][matchcount]['match_id'])
        ##matchtimelistmins = ((resp['items'][matchcount]['finished_at'] - resp['items'][matchcount]['started_at']) / 60 )
        matchtimelist.append(resp['items'][matchcount]['finished_at'] - resp['items'][matchcount]['started_at']) ## go through macthid on mathchid given in resp and minus start from finish
        matchcount += 1

print('Average match length is ' + str(mean(matchtimelist)) + ' seconds.')
