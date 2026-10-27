# initialisation de la base de donnee
import json
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
# connexion base de donnee
db = client["fairytail"]

# Nettoyer la base des anciennes donnees
db.characters.drop()
db.ennemies.drop()
db.scores.drop()

# lire le fichier .json 
with open ("characters.json", "r") as file :
    characters = json.load(file)
# creer une collection et y inserer le jeu de donnee
db.characters.insert_many(characters)


# lire le fichier .json 
with open ("ennemies.json", "r") as file :
    ennemies = json.load(file)
# creer une collection et y inserer le jeu de donnee
db.ennemies.insert_many(ennemies)


# lire le fichier .json 
with open ("scores.json", "r") as file :
    scores = json.load(file)
# creer une collection et y inserer le jeu de donnee
db.scores.insert_many(scores)
