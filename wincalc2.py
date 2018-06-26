import time


print(time.time())


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


print("Welcome to CupidKit (Mission-count), please follow the intructions!\n")
print("CupidKit is tool developed for the CS team, by the CS team, to aid us in our daily operations")
print("Cupidkit currently contains a range of tools to allow us to identify players abusing ladders/tournaments and\nto calculate wins for missions.")
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

payload = {"player_id":guid,"game":game, "limit":100, "to":time.time(), "from":1527811200}

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



if len(matchidlist) == 100:

    request_url = "https://open.faceit.com/data/v4/players/" + guid + "/history"

    payload = {"player_id":guid,"game":game, "limit":100, "to":time.time(), "from":1527811200, "offset":100}

    header = {
        'Authorization': "Bearer e0caffdb-be9c-42cc-8f07-d9e655b56576"
        }

    r = requests.get(request_url, params=payload, headers=header)

    outcome = r.json()


    ##dumps the json object into an element
    json_str = json.dumps(outcome)


    ##//load the json to a string
    resp = json.loads(json_str)

    matchcount = 0
    for x in resp['items']:
            ##print(resp['items'][matchcount]['match_id'])
            matchidlist.append(resp['items'][matchcount]['match_id'])
            matchcount += 1


##matchlist = [match1['match_id'], match2['match_id']]
print('Collected data from ' + str(len(matchidlist)) + ' matches.')
##print('These are the players last matches: ' + str(matchidlist))



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


def usercontrol():
    userchoice = input('What would you like to do now? (Type number and hit ENTER)\n1. Calculate wins\n2. Display list and count of all won matches\n')
    if userchoice == '4':
        print(uniquetournamentlist)
        print('\nNow showing all unique tournaments!\n')
        usercontrol()

    if userchoice == '5':
        print(tournamentmatchlist)
        print('\nNow showing all matches played in a tournament!\n')
        usercontrol()

    if userchoice == '1':
        get_winlist()
        usercontrol()

    if userchoice == '2':
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

    if x[0] == "1" and x[1] == "-":
        
        matchwinner = matchresult['results']['winner']

        playercount = len(matchresult['teams'][matchwinner]['roster'])

        if guid == matchresult['teams'][matchwinner]['roster'][0]['player_id']:
            winlist.append(matchresult['match_id'])

        if playercount > 1:
            if guid == matchresult['teams'][matchwinner]['roster'][1]['player_id']:
                winlist.append(matchresult['match_id'])

        if playercount > 2:
            if guid == matchresult['teams'][matchwinner]['roster'][2]['player_id']:
                winlist.append(matchresult['match_id'])

        if playercount > 3:
            if guid == matchresult['teams'][matchwinner]['roster'][3]['player_id']:
                winlist.append(matchresult['match_id'])

        if playercount >4:
            if guid == matchresult['teams'][matchwinner]['roster'][4]['player_id']:
                winlist.append(matchresult['match_id'])

        return

    else:

        matchwinner = matchresult['results']['winner']
        
        playercount = len(matchresult['teams'][matchwinner]['roster_v1'])

    if guid == matchresult['teams'][matchwinner]['roster_v1'][0]['guid']:
        winlist.append(matchresult['match_id'])

    if playercount > 1:
        if guid == matchresult['teams'][matchwinner]['roster_v1'][1]['guid']:
            winlist.append(matchresult['match_id'])

    if playercount > 2:
        if guid == matchresult['teams'][matchwinner]['roster_v1'][2]['guid']:
            winlist.append(matchresult['match_id'])

    if playercount > 3:
        if guid == matchresult['teams'][matchwinner]['roster_v1'][3]['guid']:
            winlist.append(matchresult['match_id'])

    if playercount > 4:
        if guid == matchresult['teams'][matchwinner]['roster_v1'][4]['guid']:
            winlist.append(matchresult['match_id'])

    if playercount > 5:
        if guid == matchresult['teams'][matchwinner]['roster_v1'][5]['guid']:
            winlist.append(matchresult['match_id'])

    if playercount > 6:
        if guid == matchresult['teams'][matchwinner]['roster_v1'][6]['guid']:
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
