import sys 
sys.setrecursionlimit(5000)

'''Choisir la taille du plateau'''
N = int(input("Taille du plateau:"))
'''Choisir la case de départ'''
x = int(input("x:"))
y = int(input("y:"))
'''Choisir la case que l'on veut atteindre'''
x_ar = int(input("x à atteindre:"))
y_ar = int(input("y à atteindre:"))

mvmt_x = [1, 1, -1, -1, 2, 2, -2, -2]
mvmt_y = [2, -2, 2, -2, 1, -1, 1, -1]

visit = [] #liste vide pour ajouter cases déja visitées

def valide(i, j): #regarde si case dans le plateau et pas déja visitée
    if ((i>=1) and (i<=N) and (j>=1) and j<=N): 
        if not (i,j) in visit: 
            return True
    return False

def possiblePath(i,j):
    #test qui return true si arrivée atteint
    if i == x_ar and j == y_ar:
        #print("ex") #test
        return True

    for k in range(len(mvmt_x)+1): #longueur de la liste des différents mouvements
        next_x = i + mvmt_x[k]
        next_y = j + mvmt_y[k] #test mouvement pour chaque 
        if valide(next_x, next_y):
            if possiblePath(next_x,next_y): #recursion
                #print(next_x, next_y)
                return True 
    return False

#def startTour(): visualisation
#vérifier si destination valide


print(possiblePath(x,y))

            
