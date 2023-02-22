class ViewPlayer: #creation de la classe ViewPlayer qui affiche le menu du joueur avec la methode display_player_menu(self):

    def display_player_menu(self):
        """Display the player main menu and return the user choice"""
        
        while True: # tant que c 'est vrai donc true, print ce menu
            print("\n", " Gestion des joueurs ".center(80, "-"), "\n")
            print("1. Création d'un joueur")
            print("2. Modification d'un joueur")
            print("3. Liste des joueurs classée par nom")
            print("4. Liste des joueurs classée par rang")
            print("5. Revenir au menu précédent")

            choice = input("\nEntrez votre choix : ") # recuperation du choix dans la variable choice grace à l input

            if choice in ["1", "2", "3", "4", "5"]: # si choix compris dans ["1", "2", "3", "4", "5"]
                return choice # on retourne le choix sinon

            print("Choix invalide.\n") #sinon on affiche "Choix invalide.\n" + saut de ligne