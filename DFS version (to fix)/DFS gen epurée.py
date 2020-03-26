from timeit import default_timer
import sys
sys.setrecursionlimit(2000)

"""Version avec cavalier mouvement (a,b)"""
print("ATTENTION: la numérotation commence à 0")

print("Choisir la taille du plateau")
N1 = int(input("Largeur du plateau:"))
N2 = int(input("Hauteur du plateau:"))

print("Choisir la case de départ")
x = int(input("x:"))
y = int(input("y:"))

print("Choisir la case que l'on veut atteindre")
x_ar = int(input("x à atteindre:"))
y_ar = int(input("y à atteindre:"))

print("Choisir la taille du mouvement du cavalier")
a = int(input("a:"))
b = int(input("b:"))

visited = [[False]*N2 for _ in range(N1)]

def valide(i, j): #regarde si case dans le plateau et pas déja visitée
    if ((i>=0) and (i<N1) and (j>=0) and j<N2) and (not visited[i][j]): 
        return True
    return False

def possiblePath(i,j):  
    visited[i][j]=True
    mvmt_x= [-a, -b, -b, -a, a, b, b, a] #liste des mouvements dans directions x et y
    mvmt_y = [-b, -a, a, b, -b, -a, a, b]  
    if i == x_ar and j == y_ar:
        return True

    for k in range(0,8): #longueur de la liste des différents mouvements
        next_x = i + mvmt_x[k]
        next_y = j + mvmt_y[k] #test mouvement pour chaque 
        if valide(next_x, next_y):
            if possiblePath(next_x,next_y): #recursion
                return True 
            visited[next_x][next_y]=False; #backtracking
    return False

start = default_timer()
print(possiblePath(x,y))
end = default_timer()

print("Le temps mis par le programme est:", end-start,"s")
