class Partie:
    "classe qui comprend les informations sur la partie "
   
    # Constructeur de la classe
    def __init__(self, nomJoueur, pointage, listeSequence):
        self.nomJoueur = nomJoueur
        self.pointage = pointage
        self.listeSequence = listeSequence
        
    
    # Méthode qui retourne la date et le nom des joueurs de la partie pour représenter l’objet dans les boîtes de liste ou autres
    def __repr__(self):
        return self.nomJoueur + self.pointage
    
    # Méthode qui permet de retourner dans la console, tous les attributs de l’objet sur une ou plusieurs lignes
    def afficherPartie(self):
        print("Le nom du joueur : "+ self.nomJoueur)
        print("le pointage du joueur : " + str(self.pointage))