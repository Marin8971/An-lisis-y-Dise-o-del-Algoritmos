import time 

def fuerza_bruta(u: str, v: str):
    mejor_distancia = [float('inf')]
    mejor_camino = []

    def exploracion(i: int, j: int, costo: float, camino: list):
        # caso base 
        if i == 0 and j == 0:
            if costo < mejor_distancia[0]:
                mejor_distancia[0] = costo
                mejor_camino.clear()
                mejor_camino.extend(camino)
            return
         
        # si u se anuló
        if i == 0:
            nuevo = camino.copy()
            for m in range(j-1, -1, -1):
                nuevo.append(f"Insertar '{v[m]}'")
            exploracion(0, 0, costo + j, nuevo)
            return
        
        # si v se anuló
        if j == 0:
            nuevo = camino.copy()
            for n in range(i-1, -1, -1):
                nuevo.append(f"eliminar '{u[n]}'")
            exploracion(0,0,costo+i, nuevo)
            return
        
        # mantener o cambiar 
        if u[i-1] == v[j-1]:
            camino.append(f"mantener '{u[i-1]}'")
            exploracion(i-1, j-1, costo, camino)   
            camino.pop()
        else:
            camino.append(f"cambiar '{u[i-1]}' por '{v[j-1]}'")
            exploracion(i-1, j-1, costo+1, camino)
            camino.pop()
        
        # eliminar 
        camino.append(f"eliminar '{u[i-1]}'")
        exploracion(i-1, j, costo+1, camino)
        camino.pop()

        # insertar 
        camino.append(f"insertar '{v[j-1]}'")
        exploracion(i, j-1, costo+1, camino)
        camino.pop()

    exploracion(len(u), len(v), 0, [])
    mejor_camino.reverse()
    return mejor_distancia[0], mejor_camino

