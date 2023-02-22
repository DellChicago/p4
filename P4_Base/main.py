from controllers.app import ApplicationController # depuis le dossier controllers, on importe la classe ApplicationController contenue dans le fichier .app

def main():  # definition de main pour demarer l application
    """Start application"""
    app = ApplicationController()    # creation de la variable app qui est egale a ApplicationController() que l'on a importé
    app.start()  # lancement de la methode start() qui est une méthode de la classe ApplicationController() que l'on a importé



    
if __name__ == "__main__":  # lancement de l'app
    main()