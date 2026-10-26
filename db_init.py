# initialisation de la base de donnee
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["fairytail"]

# test de reception database

collection_characters = db["characters"]
characters = collection_characters.find()

for character in characters:
    print("-------------Character-------------")
    print(character)
    print("-----------------------------------")


collection_rivals = db["rivals"]
rivals = collection_rivals.find()

for rival in rivals:
    print("-------------Rivals-------------")
    print(rival)
    print("-----------------------------------")


collection_scores =db["scores"]
scores = collection_scores.find()

for score in scores:
    print("-------------Scores-------------")
    print(score)
    print("-----------------------------------")