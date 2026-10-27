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


def GetName():
    name = input("Entrez votre nom: ")
    return name


def GetRNDName():
    import random
    names = ["Alice", "Bob", "Charlie", "Diana"]
    return random.choice(names)


def print_hello(name_func):
    name = name_func()
    print(f"Bonjour, {name} !")


print_hello(GetName)
print_hello(GetRNDName)