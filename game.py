import random

from utils import add_player, create_team, pick_random_ennemy, save_scores

def get_alive_characters(player_team):
    return [character for character in player_team if character['hp'] > 0]
# def is_ennemy_alive():

def character_attack(player_team, ennemy):
    alive_characters = get_alive_characters(player_team)
    for character in alive_characters:
        print(f"{character["name"]} - ATK : {character["attack"]} - DEF : {character["defense"]} - HP : {character["hp"]} attaque .")
        degats = max(0, character['attack'] - ennemy['defense'])
        ennemy['hp'] -= degats
    
        if ennemy['hp'] <=0:
            ennemy['hp'] = 0
            break
    print(f"{ennemy['name']} : hp - {ennemy['hp']}")
                    

def ennemy_attack(player_team, ennemy):
    alive_characters = get_alive_characters(player_team)
    if len(alive_characters) == 0:
       print("Vous avez perdu !")
       return
    
    if ennemy['hp'] > 0:
        print(f"au tour de {ennemy['name']} d'attaquer .")
        character = random.choice(alive_characters)
        print(f"{character["name"]} - ATK : {character["attack"]} - DEF : {character["defense"]} - HP : {character["hp"]}")
        degats = max(0, ennemy['attack'] - character['defense'])
        character['hp'] -= degats
        
        if character['hp']<=0:
            character['hp'] = 0
            print(f'{character["name"]} est mort.')
    else:
        print("l'ennemi est mort")


def game(player_name, player_team):
    print("--------------Le jeu commence-------------")
    waves = 0

    alive_characters = get_alive_characters(player_team)
    while len(alive_characters) > 0 :
        ennemy = pick_random_ennemy()
        
        while ennemy['hp'] > 0 and len(alive_characters) > 0:
            character_attack(alive_characters, ennemy)
            

            if ennemy['hp'] > 0:
                ennemy_attack(alive_characters, ennemy)
            alive_characters=get_alive_characters(player_team)
        if ennemy['hp'] <= 0:
            waves += 1
    print("Vous avez perdu !")
    print(f"waves : {waves}")
    save_scores(player_name,waves)

                      
def start_game():
  player_name=input("Saisissez Votre pseudo : ") 
  print(" ")
  add_player(player_name)
  player_team=create_team(player_name)
  game(player_name,player_team)
                           
