class Partie:
    "classe qui comprend les informations sur la partie "
   
    # Constructeur de la classe
    def __init__(self, nomJoueur, pointage, sequence_en_cours, niveau_pause, partie_en_cours):
        self.nomJoueur = nomJoueur
        self.pointage = pointage
        self.sequence_en_cours = sequence_en_cours
        self.niveau_pause = niveau_pause
        self.partie_en_cours = partie_en_cours
        
    
    def __repr__(self):
        return self.nomJoueur + self.pointage
    
    
    def afficherPartie(self):
        print("Le nom du joueur : "+ self.nomJoueur)
        print("le pointage du joueur : " + str(self.pointage))
        