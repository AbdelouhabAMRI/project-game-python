import random
from Neuron import *

class Player:
    def __init__(self,name):
        self.name = name
        self.nbWin = 0
    def getName(self):
        return self.name
    def getNbWin(self):
        return self.nbWin
    def addWin(self):
        self.nbWin+=1
    def addLoss(self):
        pass

class HumanPlayer(Player):
    def play(self,sticks):
        if sticks==1: return 1
        else:
            correct = False
            while not correct:
                nb = input('Sticks?\n')
                try:
                    nb=int(nb)
                    if nb>=1 and nb<=3 and sticks-nb>=0:
                        correct=True
                except: pass
            return nb

class CPUPlayer(Player):
    def __init__(self,name,mode,nbSticks):
        super().__init__(name)
        self.mode = mode
        self.netw = NeuronNetwork(3,nbSticks)
        self.previousNeuron = None
    def play(self,sticks):
        if self.mode=='easy': return self.playEasy(sticks)
        elif self.mode=='hard': return self.playHard(sticks)
        else: return self.playMedium(sticks)
    def playMedium(self,sticks):
        # TODO compléter ici avec les quelques conditions pour éviter de faire
        # une grosse erreur aux derniers tours

        if (sticks<=4):
            return sticks-1
        else:
            return self.playRandom(sticks)
    def playEasy(self,sticks):
        return self.playRandom(sticks)
    def playRandom(self,sticks):
        #return random.randint(1, (sticks%3)+1)
        if (sticks<4): return random.randint(1,sticks)
        else: return random.randint(1,3)
    def playHard(self,sticks):
        # TODO utiliser le réseau neuronal pour choisir le nombre de bâtons à jouer

        if  self.previousNeuron!=None:
            pn = self.previousNeuron
            shift=  pn - sticks
        else:
            shift=0
            pn=self.netw.getNeuron(sticks)

        neuron1=pn.chooseConnectedNeuron(shift)
        if(neuron1==None):
            return 1
        if (pn == None):
            return 1
        #explication a faire
        #il faut enregistrer la valeur de self.previous neuroone pour ne pas
        # la perdre pour le prochiane coup
        #le neuron peut etre NONE
        self.netw.activateNeuronPath(pn,neuron1)
        # utiliser l'attribut self.previousNeuron pour avoir le neuron précédemment sollicité dans la partie
        # calculer un 'shift' qui correspond à la différence entre la valeur du précédent neurone et le nombre de bâtons encore en jeu
        # utiliser la méthode 'chooseConnectedNeuron' du self.previousNeuron puis retourner le nombre de bâtons à jouer
        # bien activer le réseau de neurones avec la méthode 'activateNeuronPath' après avoir choisi un neurone cible
        # attention à gérer les cas particuliers (premier tour ou sticks==1)
        return self.playMedium(sticks)
    def getNeuronNetwork(self): return self.netw
    def addWin(self):
        super().addWin()
        self.netw.recompenseConnections()
        self.previousNeuron=None
    def addLoss(self):
        super().addLoss()
        self.previousNeuron=None




        


