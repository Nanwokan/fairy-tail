import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
# connexion base de donnee
db = client["fairytail"]

def error():
    print("Choix invalide. Veuillez saisir un nombre valide parmis ceux propose")

def get_choice(max_options, error):
  while True:  
    choice = int(input("Votre choix : "))
    print(" ")

    if 1 <= choice <= max_options:
      return choice
    else:
      error()

def add_player(player_name):
    collection_players = db["players"]

    while len(player_name) < 3 or collection_players.find_one({"player_name":player_name}) :
        error()
        print(" ")
        player_name=input("Saisissez un pseudo valide : ")
        print(" ")  
        
    collection_players.insert_one({"player_name":player_name})
    print(" ")
    print(f"{player_name} ajoute avec succes")
    print(" ")

def pick_random_ennemy():
   collections_ennemies = db["ennemies"]
   random = [{"$sample": {"size": 1}}]
   result = list(collections_ennemies.aggregate(random))
   ennemy = result[0]

   print(f"Adversaire : {ennemy['name']} - {ennemy['attack']} - {ennemy['defense']} - {ennemy['hp']}")
   return ennemy

collection_characters = db["characters"]
characters = list(collection_characters.find())
player_team=[]

def display_characters():
    print("Liste des personnages disponible:")
    print(" ")
   
    for i, character in enumerate(characters, start=1):
        print(f"{i} - {character["name"]} - ATK : {character["attack"]} - DEF : {character["defense"]} - HP : {character["hp"]}")

def display_team():
    print(" ")
    print("votre team : ")
    print(" ")
    for i, character in enumerate(player_team, start=1):
        print(f"{i} - {character["name"]}")

def create_team(player_name):
    collection_teams = db["teams"]
    while len(player_team) < 3:
        display_characters()
        print(" ")
        print(f"Team actuelle {len(player_team)}/3.")
        print(" ")
        choice = get_choice(len(characters), error)
        chosen_character = characters[choice - 1]
        player_team.append(chosen_character)
    
    collection_teams.insert_one({"player_name":player_name, "team":player_team})
    display_team()
    return player_team



   
def save_scores(player_name,waves):
   collection_scores =db["scores"]
   collection_scores.insert_one({"player_name":player_name, "waves":waves})

def three_best_players():
    collection_scores =db["scores"]
    scores = list(collection_scores.find().sort("waves"))
    podium = scores[-3:][::-1]
    for i, player in enumerate(podium, start=1):
        print(f"{i} - {player["player_name"]} - score : {player["waves"]}")