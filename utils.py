import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
# connexion base de donnee
db = client["fairytail"]



collection_characters = db["characters"]


characters = collection_characters.find()

for character in characters:
    i = 1
    print(f"{i+=1} - {character["name"]}")

collection_ennemies = db["ennemies"]
ennemies = collection_ennemies.find()

for ennemy in ennemies:
    print("-------------Ennemies-------------")
    print(ennemy)
    print("-----------------------------------")


collection_scores =db["scores"]
scores = collection_scores.find()

for score in scores:
    print("-------------Scores-------------")
    print(score)
    print("-----------------------------------")