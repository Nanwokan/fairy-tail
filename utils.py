import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
# connexion base de donnee
db = client["fairytail"]



collection_characters = db["characters"]
characters = collection_characters.find()

def create_team():

    
    print("Creer votre equipe de 3 personnage :")

    for i, character in enumerate(characters, start=1):
        print(f"{i} - {character["name"]}")


#        Recuperer scores base
collection_scores =db["scores"]


def three_best_players():
    scores = list(collection_scores.find().sort("waves"))
    podium = scores[-3:][::-1]
    print(podium)
    for i, player in enumerate(podium, start=1):
        print(f"{i} - {player["player_name"]} - score : {player["waves"]}")

def exit():
    sys.exit()
    

    
def error():
    print("Choix invalide. Veuillez saisir un choix valide")