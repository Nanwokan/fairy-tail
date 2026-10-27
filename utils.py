from random import choice

import pymongo

from main import get_choice


client = pymongo.MongoClient("mongodb://localhost:27017/")
# connexion base de donnee
db = client["fairytail"]

def error():
    print("Choix invalide. Veuillez saisir un choix valide")

def add_player(player_name):
    collection_players = db["players"]
    is_existing = collection_players.find_one({"player_name":player_name})
    while is_existing or len(player_name) < 3 :
        error()
        player_name=input("Saisissez un pseudo valide : ")  
        
    collection_players.insert_one({"player_name":player_name})
    print(f"{player_name} ajoute avec succes")
    
    
def create_team(player_name):

    collection_teams = db["teams"]
    collection_characters = db["characters"]
    characters = list(collection_characters.find())
    print("Liste des personnages :")

    for i, character in enumerate(characters, start=1):
        print(f"{i} - {character["name"]} - ATK : {character["attack"]} - DEF : {character["defense"]} - HP : {character["hp"]}")

    print("Creer votre equipe de 3 personnage :")
    player_team= []

#    while len(player_team) < 3:
#        choice = int(input("Votre choix : "))
    first_member = input("")
    first_member = get_choice(len(characters), error)

    second_member = input("")
    second_member = get_choice(len(characters), error)

    last_member = input("")
    last_member = get_choice(len(characters), error)

    collection_teams.insert_one({"player_name":player_name}, {"first_member":first_member}, {"second_member":second_member}, {"last_member":last_member})

#        Recuperer scores base
def three_best_players():
    collection_scores =db["scores"]
    scores = list(collection_scores.find().sort("waves"))
    podium = scores[-3:][::-1]
    for i, player in enumerate(podium, start=1):
        print(f"{i} - {player["player_name"]} - score : {player["waves"]}")

