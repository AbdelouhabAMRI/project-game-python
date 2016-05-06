from Game import *
from Player import *

b=True

while(b==True):
    level=input("entrez l'un des niveau comme suit:\n easy\n hard \n medium\n")
    player= HumanPlayer('abdel')

    playerCPU=CPUPlayer('PC1',level,15)


    g = Game(15)
    g.start(player,playerCPU,True)

    continuer =input("voulez vous rejouer o/n \n")

    if continuer=="o" or continuer=="O": b=True
    else:b= False





