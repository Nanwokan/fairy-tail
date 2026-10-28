from utils import pick_random_ennemy

def character_attack(player_team, ennemy):
    for character in player_team:
        if character['hp'] > 0:
            degats = max(0, character['attack'] - ennemy['defense'])
            ennemy['hp'] -= degats
    
            if ennemy['hp'] <=0:
                ennemy['hp'] = 0
                break
        else:
            player_team = player_team.remove(character)
                    

def ennemy_attack(player_team, ennemy):
    if ennemy['hp'] > 0:
        random = [{"$sample": {"size": 1}}]
        result = player_team.aggregate(random)
        if result:
            character = result[0]
            degats = max(0, ennemy['attack'] - character['defense'])
            character['hp'] -= degats
        
            if ennemy['hp']<=0:
                ennemy['hp'] = 0


def game(player_team):
    print("--------------Le jeu commence-------------")
    waves = 0
    while len(player_team) > 0 :
        ennemy = pick_random_ennemy()
        while ennemy['hp'] > 0 and len(player_team) > 0:
            character_attack(player_team, ennemy)
            ennemy_attack(player_team, ennemy)
        waves += 1
    print(f"waves : {waves}")

            
                        
        

            

                           
