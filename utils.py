import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
# connexion base de donnee
db = client["fairytail"]

def error():
    print("Choix invalide. Veuillez saisir un choix valide")

def add_player(player_name):
    collection_players = db["players"]
    is_existing = collection_players.find_one({"player_name":player_name})
    if not is_existing :
        collection_players.insert_one({"player_name":player_name})
        print(f"{player_name} ajoute avec succes")
    else:
        error()

collection_characters = db["characters"]
characters = collection_characters.find()

def create_team():

    
    print("Creer votre equipe de 3 personnage :")

    for i, character in enumerate(characters, start=1):
        print(f"{i} - {character["name"]} - ATK : {character["attack"]} - DEF : {character["defense"]} - HP : {character["hp"]}")


#        Recuperer scores base
collection_scores =db["scores"]


def three_best_players():
    scores = list(collection_scores.find().sort("waves"))
    podium = scores[-3:][::-1]
    for i, player in enumerate(podium, start=1):
        print(f"{i} - {player["player_name"]} - score : {player["waves"]}")


