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



print("Welcome to CupidKit, please follow the intructions!")
print("""                                       
                                       
                            ,/         
                           ///         
                          ////         
                        //////         
                       ///////         
                      ////////         
     /////////////////////////         
          ////////////////////         
              ,///////////////         
                   *//////////         
                        */////         
                             /         
                                                
""")
print("CupidKit created by Jake Dent (Cupidly)\n")

name = input("Please input username: ")
game = input("Please type game: dota2 or csgo: ")
print("Gathering data...")
request_url = "https://open.faceit.com/data/v4/players/" + get_guid(name) + "/history"

payload = {"player_id":get_guid(name),"game":game, "limit":100, "from":1}

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
if matchtimelist == []: ##returns 0 if no matches found for game
    matchtimelist = [0]

print('Average match length is ' + str((mean(matchtimelist))/60) + ' minutes.')



matchcount = 0
tournamentmatchtimelist = []
for x in resp['items']:
    if resp['items'][matchcount]['game_type'] == "Tournament":
        tournamentmatchtimelist.append(resp['items'][matchcount]['finished_at'] - resp['items'][matchcount]['started_at']) ## go through macthid on mathchid given in resp and minus start from finish
        matchcount += 1
if tournamentmatchtimelist == []: ## return 0 if no tournaments played for that game
    tournamentmatchtimelist = [0]

print('Average match length in tournaments is ' + str((mean(tournamentmatchtimelist))/60) + ' minutes.') 





tournamentlist = []
tournamentmatchlist = []

def gentournamentlist():
    matchcount = 0
    for x in resp['items']:
        if resp['items'][matchcount]['game_type'] == "Tournament":
            tournamentlist.append(resp['items'][matchcount]['competition_id'])
            matchcount += 1


def gentournamentmatchlist():
    matchcount = 0
    for x in resp['items']:
        if resp['items'][matchcount]['game_type'] == "Tournament":
            tournamentmatchlist.append(resp['items'][matchcount]['match_id'])
            matchcount += 1
        
gentournamentlist()
gentournamentmatchlist()
uniquetournamentlist = list(set(tournamentlist)) ##removes any duplicates from the tournament list

print('This player played a total of ' + str(len(tournamentmatchlist)) + ' tournament matches in their last 100.')
print('This player played in a total of ' + str(len(uniquetournamentlist)) + ' unique tournaments in their last 100 matches.\n')

def usercontrol():
    userchoice = input('What would you like to see now? (Type number and hit ENTER)\n1. A list of all tournaments played in\n2. A list of all matches played in a tournament\n3. Exit\n')
    if userchoice == '1':
        print(uniquetournamentlist)
        print('Now showing all unique tournaments!')
        usercontrol()

    if userchoice == '2':
        print(tournamentmatchlist)
        print('Now showing all matches played in a tournament!')
        usercontrol()

    if userchoice == '3':
        quit()

    else:
        print('Invalid command, please use specified command!')
        usercontrol()


usercontrol()
