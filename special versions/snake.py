from timeit import default_timer

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

visited = [[False]*N2 for _ in range(N1)] #aucune case n'est visitée au début

def valid(i, j):
    if  i>=0 and i<N1 and j>=0 and j<N2 and (not visited[i][j]): #verifie si la case est dans le plateau + si elle n'a pas été déja visitée
        return True
    return False
       
def shortest(i,j):
    Q = [] #queue pour utiliser BFS 
    Q.append((i, j, 0))
    visited[i][j] = True #marque première case visitée comme vraie
   
    x_move = [-a, -b, -b, -a, a, b, b, a] #liste des mouvements dans directions x et y
    y_move = [-b, -a, a, b, -b, -a, a, b]
    
    while len(Q)!=0: #début du Breadth-First Search: continue tant que la longueur de queue est diff de 0
        i, j, min_moves = Q.pop(0) #enleve elément d'indice 0
        if i == x_ar and j == y_ar: #teste si on est arrivés à la position voulue
            print("Le nombre minimal de mouvements est:")
            return min_moves
        for k in range(8): #boucle *8 car longueur du nb de mouvements possibles
            next_x = ((i+x_move[k])+N1)%N1 #utilisation des congruences pour obtenir coordonnée valide 
            next_y = ((j+y_move[k])+N2)%N2
            if valid(next_x, next_y): #vérifie validité
                visited[next_x][next_y] = True #marque case comme visitée
                Q.append((next_x, next_y, min_moves+1)) #ajoute dans queue 
    return -1 #rend -1 si impossible à atteindre

start=default_timer() #mesure temps mis par l'algo: timeit serait meilleur? 
print(shortest(x,y))
end = default_timer()

print("Le temps mis par le programme est:", end-start,"s")
