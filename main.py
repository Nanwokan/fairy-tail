from game import game
from utils import get_choice, add_player, create_team, error, three_best_players
 
MENU_OPTIONS = ["Démarrer le jeu","Afficher le classement","Quitter"]


# Menu principal
#   1. Démarrer le jeu11
#   2. Afficher le classement
#   3. Quitter

def menu_principal():
  print("------------------FAIRY TAIL GAME------------------")
  for i, option in enumerate(MENU_OPTIONS, start=1):
    print(f"{i} - {option}")



def start_game():
  player_name=input("Saisissez Votre pseudo : ") 
  add_player(player_name)
  
  game(create_team(player_name))



menu_principal()
choice = get_choice(len(MENU_OPTIONS),error)

# while choice ==! 3 :
if choice == 1:
  start_game()
elif choice == 2:
  three_best_players()
else:
  exit()




# MENU = [
#   "Lancer Jeu",
#   "Afficher les scores",
#   "Quitter",
#    ]
# Menu
#   Boucle sur tout element de MENU
#       afficher numero element et texte element
# Choix (options, erreur)
#    while True:
#        Recuperer choix utilisateur
#        Verifier si choix est valide
#        Si valide
#             return choix
#        Sinon
#             Lancer fonction erreur
# Process
#    Demarrer le Jeu
#         Recuperer le nom du joueur
#             Verifier si nom valide
#               valide si nom > 3 caracteres et si non deja dispo dans le db
#               enregistrer en base de donnee
#
#         Recuperer la liste des personnage
#            ouvrir base
#            acceder a collection characters
#            find
#            Boucle sur tout personnage de la collection characters
#                afficher numero personnage et nom , attaque, defense et hp
#             initialiser player_team = []
#             tant que len(player_team) < 3
#                 recuperer choix utilisateur 
#                 Verifier si choix valide
#                   valide if choix pas deja dans player_team
#                   ajouter a player_team
#
#
#         Combat infini
#         
#         Afficher le score
#
#    Afficher les scores
#        Recuperer scores base
#            ouvrir base
#            acceder a collection score
#            find
#            convertir curseur en list
#        filtrer les 3 meilleurs
#             trie le tableau sur element.waves
#             prendre 3 derniers elements
#                    array[-3:-1]
#        Affiche les score
#    Quitter
#       sys.exit()