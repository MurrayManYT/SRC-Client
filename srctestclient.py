import urllib.request,json
counter=0
homeVariables = 5
with urllib.request.urlopen(f"https://www.speedrun.com/api/v1/") as url:
    data = json.loads(url.read().decode())
    while counter<=homeVariables:
        print(data['data']['links'][counter]['rel'])
        counter+=1
    select = input("\nwhere would you like to go (only games available for now)?") #asks the user where they would like to go
    if select.lower() == "games":
        with urllib.request.urlopen("https://www.speedrun.com/api/v1/games?max=99999999") as url:
            gameData = json.loads(url.read().decode())
            gameRange=0
            for i in gameData['data']:
                gameRange+=1
                print(gameRange) #prints the number of/the top games on speedrun.com at any given time by alphabetical order.
                gameCounter=0
                gamesearch = input("what game are you looking for (please input abbreviation)?")
                with urllib.request.urlopen(f"https://www.speedrun.com/api/v1/games?abbreviation={gamesearch}") as url:
                    gameData = json.loads(url.read().decode())
                    gameID = (gameData['data'][0]['id'])
                    print(gameData['data'][0]['names']['international'])
                    print(gameData['data'][0]['release-date'])
                    print('categories\nlevels\nrecords')
                    gamesubselect = input("what would you like to view?") #gives the user a selection (3 ik so big) of choices to choose from to select to view hBHJAEHLHVLHLJFSJHFD.skkskskira.
                    if gamesubselect!="records":
                        with urllib.request.urlopen(f"https://www.speedrun.com/api/v1/games/{gameID}/{gamesubselect}") as url:
                            gamesubdata = json.loads(url.read().decode())
                            gamesubcounter = 0
                            for x in gamesubdata['data']:
                               gamesubcounter+=1
                            print(f"number of {gamesubselect} in this game is",gamesubcounter)
                            gamecatcounter = 0
                            while gamecatcounter<=gamesubcounter:
                                if gamecatcounter<gamesubcounter:
                                    gamecatcounter+=1
                                    print(gamesubdata['data'][gamecatcounter-1]['name'])
                                else:
                                    break
                    elif gamesubselect == "records":
                    	with urllib.request.urlopen(f"https://www.speedrun.com/api/v1/games/{gameID}/{gamesubselect}") as url: #fetches records in the game specified.
                            recorddata = json.loads(url.read().decode())
                            recordcounter = 0
                            for x in recorddata['data']:
                               recordcounter+=1
                            print(f"number of {gamesubselect} in this game is",recordcounter)
                            recordscounter = 0
                            while recordscounter<=recordcounter:
                                if recordscounter<recordcounter:
                                    recordscounter+=1
                                    if recorddata['data'][recordscounter-1]['runs'][0]['run']['videos'] == 'null':
                                    	pass
                                    else:
                                    	print(recorddata['data'][recordscounter-1]['runs'][0]['run']['videos']['links'][0]['uri'])
                                    	print("Comment: ",recorddata['data'][recordscounter-1]['runs'][0]['run']['comment'])
                                else:
                                    break
                                 #it breaks if there is a run without a video. el treago why the fuck did you add an mcbe run to the boards as a placeholder without a vid? youre killing me man, youre killing me. D: im crying rn jkjk.