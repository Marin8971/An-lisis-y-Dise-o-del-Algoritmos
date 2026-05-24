def backtracking(u, v):

    mejor_distancia = [float("inf")]
    mejor_camino = []

    def backtracking(i, j, costo, camino):

        # poda
        if costo >= mejor_distancia[0]:
            return

        # caso base
        if i == 0 and j == 0:

            mejor_distancia[0] = costo
            mejor_camino.clear()
            mejor_camino.extend(camino)

            return

        # si u se acabó -> insertar restantes
        if i == 0:

            nuevo = camino.copy()
            for k in range(j - 1, -1, -1):
                nuevo.append(f"Insertar '{v[k]}'")
            backtracking(0, 0, costo + j, nuevo)

            return

        # si v se acabó -> eliminar restantes
        if j == 0:

            nuevo = camino.copy()
            for k in range(i - 1, -1, -1):
                nuevo.append(f"Eliminar '{u[k]}'")
            backtracking(0, 0, costo + i, nuevo)
            return

        # mantener o cambiar
        if u[i - 1] == v[j - 1]:

            camino.append(f"Mantener '{u[i-1]}'")
            backtracking(i - 1, j - 1, costo, camino)
            camino.pop()

        else:

            camino.append(f"Cambiar '{u[i-1]}' por '{v[j-1]}'")
            backtracking(i - 1, j - 1, costo + 1, camino)
            camino.pop()

        # eliminar
        camino.append(f"Eliminar '{u[i-1]}'")
        backtracking(i - 1, j, costo + 1, camino)
        camino.pop()

        # insertar
        camino.append(f"Insertar '{v[j-1]}'")
        backtracking(i, j - 1, costo + 1, camino)
        camino.pop()



    return mejor_distancia[0], mejor_camino


