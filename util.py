# util.py
#------------------------
# Fonctions utilitaires

# Merci a: http://stackoverflow.com/questions/17870612/printing-a-two-dimensional-array-in-python
# 10/10
def printMatrix(matrix):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))