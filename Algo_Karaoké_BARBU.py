from random import* #Ici j'appelle le module random pour pouvoir simuler le choix aléatoires des musiques et le résultats de chaque participant pour chaque musique

randomsong = randint (1,5) #Fonction pour choisir aléatoirement qu'elle musique est joué
randomscoresong1 = randint (10,100) #Fonction pour déterminer (aléatoirement) le résultat du joueur 1
randomscoresong2 = randint (10,100) #Même chose pour le joueur 2
randomscoresong3 = randint (10,100) #Même chose pour le joueur 3
randomscoresong4 = randint (10,100) #Même chose pour le joueur 4

print (randomsong) #Test des fonctions randoms pour vérification personel
print (randomscoresong1)
print (randomscoresong2)
print (randomscoresong3)
print (randomscoresong4)

class Player:
    def __init__(self,name,scoresong,song,scoretotal):
        self.nom = name #Nom/Peusdo du Joueur
        self.scoretotal = scoretotal #Score du joueur
        self.song = song #Chanson jouée 
        self.scoresong = scoresong #Score obtenu sur une chanson


    def playSong(self):
        while self.scoretotal < 100: #Oblige les manches à s'enchainer tant que personne n'est parvenu à un score de 100 ou plus
            self.scoretotal= self.scoretotal + self.scoresong #Le score d'une chanson est additionné au score total
            print(self.nom + " gagne " + str(self.scoresong) + " points de score.") # Print de la phrase qui annonce le gain de score
            print(self.nom +  str(self.scoretotal)) #Print du score total de chaque joueur


Jean = Player("Jean",randomscoresong1,randomsong,0) # Constructeur du premier joueur, j'utilise les fonction randoms comme arguments
Kevin = Player("Kevin",randomscoresong2,randomsong,0) # Constructeur du second joueur, j'utilise les fonction randoms comme arguments

Jean.playSong() 
Kevin.playSong()



 # Problèmes : Comme je suis olbigé de mettre le while dans une classe si je veux prendre en compte self.scoretotal la répétition des manche se fait toujours avec les même valeurs obtenus par les fonctions random et ne changent pas d'une manche à une autre.           