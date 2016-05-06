# Inutile de modifier cette classe normalement
class Game:
    def __init__(self,nbSticks):
        self.nbSticks = nbSticks

    def start(self,player1,player2,verbose):
        if verbose: print("New game")
        sticks = self.nbSticks
        currp = player1
        while sticks>0:
            if verbose: print("Remaining sticks:",sticks)
            n = currp.play(sticks)
            if n<1 or n>3: print("Error")
            if verbose: print(currp.getName(),"takes",n)
            sticks-=n
            if currp==player1: currp = player2
            else: currp = player1
        if verbose: print(currp.getName(),"wins!")
        if player1==currp:
            player1.addWin()
            player2.addLoss()
        else:
            player1.addLoss()
            player2.addWin()

