lab = [
    [1, 1, 1, 1, 99, 1, 1, 1, 'I'],
    [1, 99, 99, 1, 99, 1, 99, 1, 99],
    [1, 1, 99, 1, 1, 1, 99, 1, 99],
    [99, 1, 99, 1, 99, 99, 99, 1, 99],
    [1, 1, 99, -1, 1, 1, 1, 3, 99],
    [-2, 99, 99, 1, 99, 99, 99, 1, 1],
    [1, 99, 1, -1, 1, 1, 1, 1, 99],
    [1, 99, 99, 99, 99, 2, 99, 1, 99],
    ['F', 1, 3, 1, 1, 1, 99, 1, 1]
]

filas = len(lab)
cols = len(lab[0])
energia_ini = 18
energia_final = None

camino = [[0]*cols for _ in range(filas)]


def buscar(fi, co, energia):
    global energia_final
    if fi < 0 or fi >= filas or co < 0 or co >= cols:
        return False
    if lab[fi][co] == 99:
        return False
    if camino[fi][co] == 1:
        return False
    if lab[fi][co] == 'F':
        camino[fi][co] = 1
        energia_final = energia
        return True
    gasto = 0
    if isinstance(lab[fi][co], int):
        gasto = lab[fi][co]
    nueva_ene = energia - gasto if gasto > 0 else energia - gasto
    if nueva_ene < 0:
        return False
    camino[fi][co] = 1
    if buscar(fi, co-1, nueva_ene):
        return True
    if buscar(fi+1, co, nueva_ene):
        return True
    if buscar(fi-1, co, nueva_ene):
        return True
    if buscar(fi, co+1, nueva_ene):
        return True
    camino[fi][co] = 0
    return False


pos_ini = None
for i in range(filas):
    for j in range(cols):
        if lab[i][j] == 'I':
            pos_ini = (i, j)
            break
    if pos_ini:
        break

ok = buscar(pos_ini[0], pos_ini[1], energia_ini)

print("Laberinto original:")
for f in lab:
    print(f)

print()

if ok:
    gastado = energia_ini - energia_final
    print("Se puede llegar.")
    print("Energia inicial:", energia_ini)
    print("Energia final:", energia_final)
    print("Energia gastada:", gastado)
    print()
    for f in camino:
        print(f)
else:
    print("No se puede llegar.")
    for f in camino:
        print(f)
