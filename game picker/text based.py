from random import *
#===============================================================================================================================
games_list=[]
#===============================================================================================================================
with open("game.txt","r") as file_games:
    for count, line in enumerate(file_games):pass
#===============================================================================================================================
def delbyte1(name):
    nama=""
    l = False
    for i in name:
        if l == False:
            l = True
            continue
        nama=nama+i
    return nama
#===============================================================================================================================
class games:
#-------------------------------------------------------------------------------------------------------------------------------
    def __init__(self,name):
            if name == "\n":return
            if name[0] == "U": launcher = "Ubisoft connect"
            elif name[0] == "S": launcher = "steam"
            elif name[0] == "E": launcher = "Epic games"
            elif name[0] == "G": launcher = "Gog"
            elif name[0] == "O": launcher = "Origin"
            #-------------------------------------------------------------------------------------------------------------------------------
            name = delbyte1(name)
            #-------------------------------------------------------------------------------------------------------------------------------
            self.game_info = {
            "name":name,
            "launcher":launcher
        }
#===============================================================================================================================

with open("game.txt","r") as file_games:
    for i in range(count):
        name = file_games.readline()
        if name == "\n":continue
        game_info=games(name)

        games_list.append(game_info.game_info)

chossen_game= randint(0,len(games_list))
print("The game is:",games_list[chossen_game]["name"])
print("useing the luncher:",games_list[chossen_game]["launcher"])