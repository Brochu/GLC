# tabTranslator.py
# --------------------------
# TODO: Remplir ici
#
# NOTE: Difficulte rencontree lorsqu'on fait les tablatures (a mettre dans le rapport ca veut dire ca):
#           Etant donne qu'il y a plusieurs fois la meme note sur la guitar, il est difficile de trouver ou le guitariste
#           jous lorsqu'on analyse une note. Je pense qu'il serait possible avec des notions d'IA (fuck that, on a pas le temps)
#           de trouver quelle note exactement il jous, mais ca prendrait une crisse de bonne heuristique
#

import mathlab
import random # Temporaire

from baseTranslator import baseTranslator

BUFFER_LENGTH = 8

SEPARATOR_COUNT = 2 # Should not be < 2
SEPARATOR_CHAR = '-'
MESURE_SEPARATOR_CHAR = '|'
MESURE_SEPRATOR_COUNT = 1

TUNING = ['e', 'B', 'G', 'D', 'A', 'E']

class tabTranslator(baseTranslator):
    def __init__(self, bufferLength=BUFFER_LENGTH, separatorCount = SEPARATOR_COUNT, separatorChar = SEPARATOR_CHAR, mesureSeparatorChar = MESURE_SEPARATOR_CHAR, mesureSeparatorCount = MESURE_SEPRATOR_COUNT, tuning = TUNING):
        baseTranslator.__init__(self, bufferLength)
        self.separatorCount = separatorCount
        self.separatorChar = separatorChar
        self.mesureSeparatorChar = mesureSeparatorChar
        self.mesureSeparatorCount = mesureSeparatorCount
        self.tuning = tuning
        
        self._initStrings()
    
    def _initStrings(self):
        self.guitStrings = []
        
        for i in range(0, 6):
            self.guitStrings.append(self.tuning[i] + (self.mesureSeparatorChar * self.mesureSeparatorCount) + (self.separatorChar * self.separatorCount))
    
    def _getNotePositionOnGuitar(self, note):
        """Oh boy, ca en sera pas une facile ca...
            Retourne un tuple (Corde, Frette)"""
        
        # C'est temporaire pour tester l'output du translator
        if random.randint(1, 100) >= 100:
            return (random.randint(5, 6), random.randint(12, 15))
        else:
            return (random.randint(5, 6), random.randint(0, 3))
    
    def _translate(self, note):
        """Can only handle one note at a time right now..."""
        
        notePos = self._getNotePositionOnGuitar(note)
        
        for i in range(0, 6):
            if notePos[0] == i + 1:
                noteVal = str(notePos[1]) # Valeur numerique de la note
                separatorVal = (self.separatorChar * (self.separatorCount - len(noteVal) + 1)) # Si la note est plus haute que 10, le separator devrait etre moins long
                self.guitStrings[i] += noteVal + separatorVal
            else:
                self.guitStrings[i] += self.separatorChar * (self.separatorCount + 1)
        
        self.bufferSize += 1
    
    def _flush(self):
        for s in self.guitStrings:
            padAmount = (self.bufferMaxSize - self.bufferSize) * (self.separatorCount + 1)
            self.buffer += s + (self.separatorChar * padAmount) + (self.mesureSeparatorChar * self.mesureSeparatorCount) + '\n'
        
        self._initStrings()