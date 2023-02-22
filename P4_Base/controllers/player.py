# de quoi avons nous besoin pour faire fonctionner le controller player?

from views.view_player import ViewPlayer # ici on importe depuis le fichier  views_player qui est dans le dossier  views, la classe ViewPlayer


class PlayerController: # ici on crée la classe PlayerController

    def __init__(self) -> None:  # on initialise la classe, grace a la méthode constructeur __init__.py
        self.view = ViewPlayer() # on initialise la variable view, qui contient la classe ViewPlayer

    def handle_player(self): # on definie la méthode handel_player
        exit_requested = False # création d'une variable exit_requested ayant pour valeur False
        
        while not exit_requested: # boucle while, tant que la variable exit_requested est not, donc tant qu'elle est true
            choice = self.view.display_player_menu() # on crée la variable choice qui lance la methode display_player_menu à partir de la variable view qui a pour valeur View_Player

            if choice == "1": # si choix 1, on lance la methode .create_player() de la classe PlayerController
                # creation d'un joueur
                self.create_player()
            elif choice == "2": # si choix 2, on lance la methode .update_player() de la classe PlayerController
                # Update player
                self.update_player()
            elif choice == "3":  # si choix 3, on lance la methode display_players_order_by_name() de la classe PlayerController
                # gestion des listes
                self.display_players_order_by_name()
            elif choice == "4":  # si choix 4, on lance la methode .display_players_order_by_name() de la classe PlayerController
                # gestion des listes
                self.display_players_order_by_name()
            elif choice == "5": # si choix 5, on lance la variable exit_requested  passe a true et donc on réaffiche le menu ???
                # gestion des listes
                # Retour au menu précédent
                exit_requested = True

    def create_player(self):  # début de la méthode create_player(self) avec quelques indications il faut encore l'implementer
        """Manage player creation"""
        print("Gestion de la création d'un joueur")
        input('\nAppuyez sur Entreé pour continuer ')

    def update_player(self): # début de la méthode  update_player qui va mettre a jour le joueur avec quelques indications il faut encore l'implementer
        """Manage player update"""
        print("Gestion de la modification d'un joueur")
        input('\nAppuyez sur Entreé pour continuer ')

    def display_players_order_by_name(self): # début de la méthode  display_players_order_by_name(self) qui va afficher les joueurs par noms
        """Print players order by name"""
        print("Gestion de l'impression de la liste des joueurs triée par nom")
        input('\nAppuyez sur Entreé pour continuer ')

    def display_players_order_by_rank(self): # début de la méthode  display_players_order_by_rank(self) qui va afficher les joueurs par rangs
        """Print players order by rank"""
        print("Gestion de l'impression de la liste des joueurs triée par rang")
        input('\nAppuyez sur Entreé pour continuer ')
