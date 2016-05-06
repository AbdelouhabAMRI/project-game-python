from Game import *
from Player import *

b=0

while(b<100):

    b+=1

    playerCPU1= CPUPlayer('PC1','easy',15)

    playerCPU2=CPUPlayer('PC2','medium',15)


    g = Game(15)
    g.start(playerCPU2,playerCPU2,True)




