from timeit import default_timer
"""Version 3D avec cavalier mouvement (a,b,c)"""
print("ATTENTION: la numérotation commence à 0")

print("Choisir la taille du cube")
N1 = int(input("Largeur du cube:"))
N2 = int(input("Hauteur du cube:"))
N3 = int(input("Profondeur du cube:"))

print("Choisir la case de départ")
x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))

print("Choisir la case que l'on veut atteindre")
x_ar = int(input("x à atteindre:"))
y_ar = int(input("y à atteindre:"))
z_ar = int(input("z à atteindre:"))

print("Choisir la taille du mouvement du cavalier")
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

visited = [[[False]*N3 for _ in range(N2)]for _ in range(N1)] #aucune case n'est visitée au début

def valid(i, j, h):
    if  i>=0 and i<N1 and j>=0 and j<N2 and  h>=0 and h<N3 and (not visited[i][j][h]): #verifie si la case est dans le plateau + si elle n'a pas été déja visitée
        return True
    return False
        
def shortest(i,j,h):
    Q = [] #queue pour utiliser BFS 
    Q.append((i, j, h, 0))
    visited[i][j][h] = True #marque première case visitée comme vraie
   
    x_move = [a, a, a, a, -a, -a, -a, -a, b, b, b, b, -b, -b, -b, -b, c, c, c, c, -c, -c, -c, -c, b, b, b, b, -b, -b, -b, -b, c, c, c, c, -c, -c, -c, -c, a, a, a, a, -a, -a, -a, -a] 
    y_move = [b, -b, b, -b, b, -b, b, -b, a, -a, a, -a, a, -a, a, -a, a, -a, a, -a, a, -a, a, -a, c, -c, c, -c, c, -c, c, -c, b, -b, b, -b, b, -b, b, -b, c, -c, c, -c, c, -c, c, -c]
    z_move = [c, c, -c, -c, c, c, -c, -c, c, c, -c, -c, c, c, -c, -c, b, b, -b, -b, b, b, -b, -b, a, a, -a, -a, a, a, -a, -a, a, a, -a, -a, a, a, -a, -a, b, b, -b, -b, b, b, -b, -b]
    
    while len(Q)!=0: #début du Breadth-First Search: continue tant que la longueur de queue est diff de 0
        i, j, h, min_moves = Q.pop(0) #enleve elément d'indice 0
        if i == x_ar and j == y_ar and h == z_ar: #teste si on est arrivés à la position voulue
            print("Le nombre minimal de mouvements est:")
            return min_moves
        for k in range(48): #boucle *8 car longueur du nb de mouvements possibles
            next_x = i+x_move[k]
            next_y = j+y_move[k]
            next_z = h+z_move[k]
            if valid(next_x, next_y, next_z): #vérifie validité
                visited[next_x][next_y][next_z] = True #marque case comme visitée
                Q.append((next_x, next_y, next_z, min_moves+1)) #ajoute dans queue 
    return -1 #rend -1 si impossible à atteindre

start=default_timer() #mesure temps mis par l'algo: timeit serait meilleur? 
print(shortest(x,y,z))
end = default_timer()

print("Le temps mis par le programme est:", end-start,"s")
