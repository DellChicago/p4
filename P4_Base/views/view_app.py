class ViewApp:  # creation de la class ViewApp, qui a pour méhode display_main_menu(self)

    def display_main_menu(self):  # affiche le menu
        """Display the main menu and return the user choice"""
        
        while True:
            print("\n", " Bienvenue dans chess manager ".center(80, '-'))  # .center pour faire joli :)
            print("\n1. Gestion des tournois") # \n pour saut de ligne
            print("2. Gestion des joueurs") # 
            print("3. Quitter")

            choice = input("\nEntrez votre choix : ") # un inpiut qui receuillera une donnée qui sera stockée dans choice

            if choice in ["1", "2", "3"]: # condition if si choice est contenu dans la liste 
                if choice == "3": # et si choice = "3 ", donc print au revoir
                    print("Au revoir")
                    
                return choice # puis retourne au choice après avoir printer "Au revoir"

            print("Choix invalide.\n")  # print de "Choix invalide.\n" + saut de ligne si choice pas compris dans ["1", "2", "3"]