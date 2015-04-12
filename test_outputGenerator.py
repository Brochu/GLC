# test_outputGenerator.py
#------------------------
# Is this what we call unit testing?

import outputGenerator
import mathlab

NOTES = [(-1, 1), (0, 1), (1, 1), (2, 1), (3, 1), (None, None), (5, 1)]

def translateBaseNotes(notes):
    res = []
    for n in notes:
        res.append((mathlab.convertToLetterNote(n[0]), n[1]))
    
    return res

def testSimpleTranslator(notes):
    """simpleTranslator test"""
    print "================\nTesting simpleTranslator...\n================\n"
    outGen = outputGenerator.outputGenerator()
    outGen.translate(notes)
    print ""

if __name__ == "__main__":
    print "\n================\nNotes used for tests:\n\t{0}\n\t{1}\n================\n".format(NOTES, translateBaseNotes(NOTES))
    
    testSimpleTranslator(NOTES)
    print "================\nEND OF TESTS\n================"