# puntajes crudos[10, -5, 95, 120, 50, -1]

# necesitamos una lista que solo tenga valores válidos entre 0 y 100

#bucle for de recorrido de lista
puntajes_crudos = [10, -5, 95, 120, 50, -1]
puntajes_validos=[]
for puntaje in puntajes_crudos:
    if 0 <= puntaje <= 100:
        puntajes_validos.append(puntaje) 