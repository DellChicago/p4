# ce fichier (app.py) qui est situé  dans le dossier controllers et 
# qui représente l'application sera lancé en premier !

# on importe les classes necessaires
from controllers.tournament import TournamentController # (ici on importe TournamentController qui se situe dans le fichier tournament.py du dossier controllers).
from controllers.player import PlayerController # (ici on importe PlayerController qui se situe dans le fichier player.py du dossier controllers).
from views.view_app import ViewApp # (ici on importe la classe ViewApp qui se situe dans le fichier view_app.py du dossier views qui contient toutes les vues).


class ApplicationController: #ici on definie la classe ApplicationController qui represente l'application et qui va s'occuper du sequençage
    """Represents the application""" # ??? pourquoi apres le self, on ne met pas une virgule et ensuite view_app, tournament_controller, player_controller ???

    def __init__(self) -> None: #  La méthode __init__  Initialise la classe ApplicationController en fonction des paramètres, La méthode __init__ est une méthode spéciale qui est appelée lors de la création d'une instance. La méthode __init__ est une méthode spéciale, elle doit par exemple obligatoirement retourner None .
        self.view_app = ViewApp() # La méthode __init__  permet de définir directement certains des attributs de l'objet dès sa création, d'attribuer des valeurs par défaut ou d'appeler d'autres méthodes qui ont un même rôle d'initialisation.
        self.tournament_controller = TournamentController()
        self.player_controller = PlayerController()

    def start(self): # ici la methode start lance l'application, on aurait pu lui donner un autre nom
        """Display the main menu and manage user choice"""
        exit_requested = False # ici une petite astuce pour dire que tant exit_requested = False, cad tant que l'utilisateur ne veut pas quitter l'app, execute cette boucle
        
        while not exit_requested: # bien noté la présence du mot not !
            choice = self.view_app.display_main_menu() # dans tous les cas tant que not exit_requested, lance choice qui lance la méthode display_main_menu() de la variable view_app qui = ViewApp()

            if choice == "1": # donc ici si  à partir du display_main_menu() le choix est 1, lance la méthode .handle_tournament() de la vairable tournament_controller qui est egale à la classe TournamentController() importée au début du fichier
                # gestion des tournois
                self.tournament_controller.handle_tournament()
            elif choice == "2": # donc ici si  à partir du display_main_menu() le choix est 2, lance la méthode handle_player() de la vairable player_controller qui est egale à la classe PlayerController() importée au début du fichier
                # Gestion des joueurs
                self.player_controller.handle_player()
                # exit
            elif choice == "3": # donc ici si  à partir du display_main_menu() le choix est 3, transforme le resultat de la variable exit_requested en "True"
                exit_requested = True # ??? ici normalement, a verifier , vu que exit_requested passe à True, on lui demande d'arreter et de ne plus faire un display_main_menu() ???
                

