from utils import create_team, error

MENU_OPTIONS = ["Démarrer le jeu","Afficher le classement","Quitter"]


# Menu principal
#   1. Démarrer le jeu
#   2. Afficher le classement
#   3. Quitter

def menu_principal():
  print("------------------FAIRY TAIL GAME------------------")
  for i, option in enumerate(MENU_OPTIONS, start=1):
    print(f"{i} - {option}")
  

def get_choice (max_options, error):
  while True:
#      Recuperer choix utilisateur
    choice = int(input("Votre choix : "))
#        Verifier si choix est valide
#        Si valide
    if 1 <= choice <= max_options:
      return choice
    else:
#             Lancer fonction erreur
      error()

menu_principal()
choice = get_choice(len(MENU_OPTIONS),error)
# Demarrer le jeu
#   saisir le pseudo du joueur
#   creer son equipe
# def start_game():
#    player_name = input("Saisissez votre pseudo : ")
#    return player_name
#    create_team()
# constituer son equipe
#   pour chaque character dans la table characters
#     afficher i+= 1 character["name"]
#   recuperer les choix utilisateurs
#   afficher l'equipe actuelle

#sys.exit()

#while player_choice ==! 3:
# Tant que le choix est different de 3
#   si le choix est 1
#     demarrer le jeu
#   si le choix est 2
#     Afficher le classement
# Sinon 
# afficher un message d'aurevoir et break

# MENU = [
#   "Lancer Jeu",
#   "Afficher les scores",
#   "Quitter",
#    ]
# Menu
#   Boucle sur tout element de MENU
#       afficher numero element et texte element
# 
# Process
#    JEU
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