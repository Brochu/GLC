# test_outputGenerator.py
#------------------------
# Is this what we call unit testing?

import outputGenerator
import mathlab
import sys
import io

from tabTranslator import tabTranslator

NOTES = [(5, 2), (1, 3), (2, 3), (2, 5), (3, 4), (None, None), (5, 2)]

def translateBaseNotes(notes):
    res = []
    for n in notes:
        res.append((mathlab.convertToLetterNote(n[0]), n[1]))
    
    return res

def testSimpleTranslator(notes, outStream):
    """simpleTranslator test"""
    outStream.write(u"\n================\nTesting simpleTranslator...\n================\n")
    outGen = outputGenerator.outputGenerator(outputStream = outStream)
    outGen.translate(notes)

def testTabTranslator(notes, outStream):
    """tabTranslator test"""
    outStream.write(u"\n================\nTesting tabTranslator...\n================\n")
    outGen = outputGenerator.outputGenerator(translator = tabTranslator(), outputStream = outStream)
    outGen.translate(notes)

if __name__ == "__main__":
    outStream = sys.stdout

    if len(sys.argv) > 1:
        outStream = io.open(sys.argv[1], 'w')
        
    print "\n================\nNotes used for tests:\n\t{0}\n\t{1}\n\nOutput is streamed into {2}\n================".format(NOTES, translateBaseNotes(NOTES), outStream.name)
    testSimpleTranslator(NOTES, outStream)
    testTabTranslator(NOTES, outStream)
    print "\n================\nEND OF TESTS\n================"