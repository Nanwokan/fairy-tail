import collections

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
# connexion base de donnee
db = client["fairytail"]

def error():
    print("Choix invalide. Veuillez saisir un choix valide")

def get_choice (max_options, error):
  while True:
#      Recuperer choix utilisateur
    choice = int(input("Votre choix : "))
#        Verifier si choix est valide
#        Si valide
    if 1 <= choice <= max_options:
      return choice
    else:
#             Lancer fonction erreur
      error()

def add_player(player_name):
    collection_players = db["players"]

    while len(player_name) < 3 or collection_players.find_one({"player_name":player_name}) :
        error()
        player_name=input("Saisissez un pseudo valide : ")  
        
    collection_players.insert_one({"player_name":player_name})
    print(f"{player_name} ajoute avec succes")

def pick_random_ennemy():
   collections_ennemies = db["ennemies"]
   random = [{"$sample": {"size": 1}}]
   result = list(collections_ennemies.aggregate(random))
   ennemy = result[0]

   print(f"Adversaire : {ennemy['name']} - {ennemy['attack']} - {ennemy['defense']} - {ennemy['hp']}")
   return ennemy

    
def create_team(player_name):

    collection_teams = db["teams"]
    collection_characters = db["characters"]
    characters = list(collection_characters.find())

    player_team= []

    while len(player_team) < 3:
        print("Liste des personnages disponible:")

        for i, character in enumerate(characters, start=1):
            print(f"{i} - {character["name"]} - ATK : {character["attack"]} - DEF : {character["defense"]} - HP : {character["hp"]}")

        print(f"Team actuelle {len(player_team)}/3.")
        choice = get_choice(len(characters), error)
        chosen_character = characters[choice - 1]
        player_team.append(chosen_character)
    
    collection_teams.insert_one({"player_name":player_name, "team":player_team})
    
    print("votre team : ")
    for i, character in enumerate(player_team, start=1):
        print(f"{i} - {character["name"]}")

    return player_team

#        Recuperer scores base
def three_best_players():
    collection_scores =db["scores"]
    scores = list(collection_scores.find().sort("waves"))
    podium = scores[-3:][::-1]
    for i, player in enumerate(podium, start=1):
        print(f"{i} - {player["player_name"]} - score : {player["waves"]}")

