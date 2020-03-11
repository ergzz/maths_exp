N = int(input("Taille du plateau:"))
(x,y) = (int(input("x="), int(input("y=")))) #case départ
(x_ar, y_ar) = (int(input("x_ar="), int(input("y_ar=")))) #case arrivée

mvmt = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2, -2)]

visit = [] #liste vide pour ajouter cases déja visitées

def valide((i, j)): #regarde si case dans le plateau et pas déja visitée
    if ((i>=1) and (i<=N) and (j>=1) and j<=N): 
        if not (i,j) in visit: 
            return True
    return False

def knight_tour((i,j), step_count, mvmt):
    if (next_x,next_y) = (x_ar,y_ar):
        return True
    #test qui return true si arrivée atteinte

    for k in range(len(mvmt)+1): #longueur de la liste des différents mouvements
        (next_x, next_y) = (x,y)+mvmt[k] #test mouvement pour chaque index

        if(valide((next_x, next_y)):
            
