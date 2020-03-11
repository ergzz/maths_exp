N = int(input("Taille du plateau:"))
x = int(input("x:"))
y = int(input("y:"))

#x_ar ,y_ar = int(input("x_ar,y_ar:")).split() #case arrivée

mvmt = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2, -1)]

visit = [(1,2)] #liste vide pour ajouter cases déja visitées

def valide(i, j): #regarde si case dans le plateau et pas déja visitée
    if ((i>=1) and (i<=N) and (j>=1) and j<=N): 
        if not (i,j) in visit: 
            return True
    return False

print(valide(x,y))