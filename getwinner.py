import requests
import json
matchid = 'd4d451f9-5c42-4991-8ac8-4fd19515c586'
matchresult = None

def get_winner(x):
    guid = None

    header = {
    'Authorization': "Bearer e0caffdb-be9c-42cc-8f07-d9e655b56576"
    }

    r = requests.get("https://open.faceit.com/data/v4/matches/" + str(x), headers=header)

    outcome = r.json()


    ##dumps the json object into an element
    json_str = json.dumps(outcome)

    ##//load the json to a string
    resp = json.loads(json_str)

    ##//print the resp
    ##print (resp)

    ##//extract an element in the response
    
    matchresult = resp
    return matchresult


matchresult = get_winner(matchid)

print(matchresult['results']['winner'])

print(matchresult['teams']['faction1']['roster_v1'][4]['guid'])

def get_winlist(guid):
    for match in matchidlist:
        get_winner(guid)
        print(matchresult['results']['winner'])
