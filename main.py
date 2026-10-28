from game import game, start_game
from utils import get_choice, error, three_best_players

MENU_OPTIONS = ["Démarrer le jeu","Afficher le classement","Quitter"]

def menu_principal():
  print("------------------FAIRY TAIL GAME------------------")
  print(" ")

  for i, option in enumerate(MENU_OPTIONS, start=1):
    print(f"{i} - {option}")
  
  print(" ")
  print("---------------------------------------------------")


def main():

  menu_principal()
  choice = get_choice(len(MENU_OPTIONS),error)
  print(" ")
  print(f"Vous avez choisi : {choice}")
  print(" ")

  if choice == 1:
    start_game()
  elif choice == 2:
    three_best_players()
  else: 
    exit()

main()