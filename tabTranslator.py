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
import util

from baseTranslator import baseTranslator

BUFFER_LENGTH = 16

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
        
        self._maxStrings = 6
        self._maxFrets = 24
        
        self.guitStrings = self._initStrings()
        self.noteDictionnary = self._initNoteDictionnary()
    
    def _initStrings(self):
        """Initialisation of the visual component of the guitar strings on the tab"""
        guitStrings = []
        
        for i in range(0, 6):
            guitStrings.append(self.tuning[i] + (self.mesureSeparatorChar * self.mesureSeparatorCount) + (self.separatorChar * self.separatorCount))
            
        return guitStrings
    
    def _initNoteDictionnary(self):
        """Initialise a note dictionnary representing the guitar"""
        strings = self._maxStrings
        frets = self._maxFrets
        dict = [[0 for i in range(frets)] for i in range(strings)]
        
        dict[0][0] = (5, 4)     # E 4
        dict[1][0] = (12, 3)    # B 3
        dict[2][0] = (8, 3)     # G 3
        dict[3][0] = (3, 3)     # D 3
        dict[4][0] = (10, 2)    # A 2
        dict[5][0] = (5, 2)     # E 2
        
        for i in range(strings):
            for j in range(1, frets):
                baseNote = dict[i][j - 1]
                octave = baseNote[1]
                note = baseNote[0] + 1
                
                if baseNote[0] + 1 > 12:
                    octave += 1
                    note = 0
                
                dict[i][j] = (note, octave)
        
        return dict
    
    def _getNotePositionOnGuitar(self, note):
        """Retourne un tuple (Corde, Frette)"""
        
        """
        # C'est temporaire pour tester l'output du translator
        if random.randint(1, 100) >= 100:
            return (random.randint(5, 6), random.randint(12, 15))
        else:
            return (random.randint(5, 6), random.randint(0, 3))
        """
        
        strings = self._maxStrings
        frets = self._maxFrets
        
        for i in range(frets):
            for j in range(strings):
                if self.noteDictionnary[j][i] == note:
                    return (j + 1, i)
                    
        raise IndexError("Note not on guitar... {0}".format(note))
    
    def _translate(self, note):
        """Can only handle one note at a time right now..."""
        
        noteNormalized = (note[0], note[1])
        notePos = self._getNotePositionOnGuitar(noteNormalized)
        
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
        
        self.guitStrings = self._initStrings()

if __name__ == "__main__":
    tt = tabTranslator()
    util.printMatrix(tt.noteDictionnary)