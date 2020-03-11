'''Choisir la taille du plateau'''
N = int(input("Taille du plateau:"))
'''Choisir la case de départ'''
x = int(input("x:"))
y = int(input("y:"))
'''Choisir la case que l'on veut atteindre'''
x_ar = int(input("x à atteindre:"))
y_ar = int(input("y à atteindre:"))

mvmt = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2, -1)]

visit = [] #liste vide pour ajouter cases déja visitées

def valide(i, j): #regarde si case dans le plateau et pas déja visitée
    if ((i>=1) and (i<=N) and (j>=1) and j<=N): 
        #if not (i,j) in visit: 
        return True
    return False

def possiblePath((i,j), mvmt):
    if (next_x,next_y) == (x_ar,y_ar):
        return True
    #test qui return true si arrivée atteint
    for k in range(len(mvmt)+1): #longueur de la liste des différents mouvements
        (next_x, next_y) = (i,j)+mvmt[k] #test mouvement pour chaque index
        if(valide((next_x, next_y)):
            if possiblePath((next_x,next_y),mvmt): #recursion
                return True 
    return False

#def startTour():

print(valide(x,y))

            
