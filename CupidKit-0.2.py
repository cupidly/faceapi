import requests
import json
from statistics import mean ##adds the mean average function
##funnction to retrieve GUID using players username 
def get_guid(x):
    guid = None
    payload = {"nickname":x}

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


print("Welcome to CupidKit, please follow the intructions!\n")
print("CupidKit is tool developed for the CS team, by the CS team, to aid us in our daily operations")
print("Cupidkit currently contains a range of tools to allow us to identify players abusing ladders/tournaments")
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
print("CupidKit 0.2 created by Jake Dent (Cupidly)\n")

name = input("Please input username: ")
guid = get_guid(name)
game = input("Please type game: dota2, csgo, lol_EUN, lol_EUW, wot_NA, wot_EU, wot_RU: ")
print("Gathering data...\n")
request_url = "https://open.faceit.com/data/v4/players/" + guid + "/history"

payload = {"player_id":guid,"game":game, "limit":100, "from":1}

header = {
    'Authorization': "Bearer e0caffdb-be9c-42cc-8f07-d9e655b56576"
    }

r = requests.get(request_url, params=payload, headers=header)

outcome = r.json()


##dumps the json object into an element
json_str = json.dumps(outcome)


##//load the json to a string
resp = json.loads(json_str)


print("GUID found for player " + name + ": " + guid)

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
    userchoice = input('What would you like to see now? (Type number and hit ENTER)\n1. A list of all tournaments played in\n2. A list of all matches played in a tournament\n3. A list of all tournament match lengths \n4. Calculate wins (This will take a minute)\n5. Display list of wins\n6. Exit\n')
    if userchoice == '1':
        print(uniquetournamentlist)
        print('\nNow showing all unique tournaments!\n')
        usercontrol()

    if userchoice == '2':
        print(tournamentmatchlist)
        print('\nNow showing all matches played in a tournament!\n')
        usercontrol()

    if userchoice == '4':
        get_winlist()
        usercontrol()

    if userchoice == '5':
        print(winlist)
        print('Now showing a list of all matches won! ' + name + ' won ' + str(len(winlist)) + ' matches!\n') 
        usercontrol()

    if userchoice == '3':
        print(tournamentmatchtimelist)
        print('\nNow showing length of all tournament matches (in seconds)\n')
        usercontrol()

    if userchoice == '6':
        quit()

    else:
        print('\nInvalid command, please use specified command!')
        usercontrol()

counter = 0
winlist = []
def get_winner(x):
    
    
    header = {
    'Authorization': "Bearer e0caffdb-be9c-42cc-8f07-d9e655b56576"
    }

    r = requests.get("https://open.faceit.com/data/v4/matches/" + str(x), headers=header)

    outcome = r.json()


    ##dumps the json object into an element
    json_str = json.dumps(outcome)

    ##//load the json to a string
    resp = json.loads(json_str)

    
    matchresult = resp
    ##print(matchresult['results']['winner'])
    ## NEED TO DO A FOR LOOP HERE INSTEAD TO LOOP THORUGH ALL PLAYERS
    ## IN WINNING TEAM, TO FIX ISSUE WITH GAMES OF MORE OR LESS THAN 5
    matchwinner = matchresult['results']['winner']
    if guid == matchresult['teams'][matchwinner]['roster_v1'][0]['guid']:
        winlist.append(matchresult['match_id'])
    if guid == matchresult['teams'][matchwinner]['roster_v1'][1]['guid']:
        winlist.append(matchresult['match_id'])
    if guid == matchresult['teams'][matchwinner]['roster_v1'][2]['guid']:
        winlist.append(matchresult['match_id'])
    if guid == matchresult['teams'][matchwinner]['roster_v1'][3]['guid']:
        winlist.append(matchresult['match_id'])
    if guid == matchresult['teams'][matchwinner]['roster_v1'][4]['guid']:
        winlist.append(matchresult['match_id'])
    return

matchresult = None

def get_winlist():
    counter = 0
    for match in matchidlist:
        matchresult = get_winner(match)
        print(str(matchidlistpercent * counter) + ' percent complete!')
        counter += 1
        if counter == len(matchidlist):
            print('Calculation complete!')
        

matchidlistpercent = 100/ len(matchidlist)

usercontrol()

