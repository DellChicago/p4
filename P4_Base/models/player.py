# MVC, les vues sont pensées, crées mais restent staitques, elles existent mais ne s'affichent que 
# lorsque le controleur les appelles
# pareil pour le model, les models sont pensés et presnts, ils existent mais sont executé que lorque le 
# controleur les appels

"""Classe joueur"""

class Player: # ici on vas initeiliser et creer la classe player, donc tout ce qu'il faut pour créer un joueur,
    #ici chaque joueur crée aura un nom et un rang (parametre definis dans la methode __init__)
    """Represents a player"""

    table_name = "player" # ici on crée une variable nommé table_name qui aura pour valeur "player"

    def __init__(self, name:str, rank:int) -> None:
        self.name = name
        self.rank = rank

    def __str__(self) -> str:
        return self.name
    
    def serialize(self) -> dict:  # une mlethode pour serializer le joueur qui retourne un dico
        """Return a dictionnary with the object attribute value"""
        data = {
            'name': self.name,
            'rank': self.rank
        }
        return data  # la valeur retournée sera data ( un dico clé - valeur)

    @classmethod    # ici une méthode de classe qui permet de déserialiser, elle retournera un joueur à partir d un dico
    def deserialize(self, data: dict) -> "Player":
        """Return a Player from a dictionnary"""
        return Player(**data)  # ??? vouble étoiles???


    def save(self):  # ici une metahode pour sauver un joueur devra etre implémentée
        print("player sauvegardé")

if __name__ == '__main__':  #??? pourquoi mettre ici if __name__ == '__main__': ??? peut etre exemple??
    """Test a player"""
    p1 = Player("Carlsen", 3000)  # ici surment un test de creation d'instance de joueurs???
    p2 = Player("Kasparov", 2800)

    print(p1.table_name)
    print(p2.table_name)
    print(Player.table_name)

    # p1.save()

    print(f"sérialisation p1: {p1.serialize()}")  # ici surment un test de serialisation ??

    data = {'name': "Carlsen", 'rank': 3100}
    player = Player.deserialize(data)
    print(player)
    