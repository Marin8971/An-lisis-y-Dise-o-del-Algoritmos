import time 

def tabulacion(u: str, v: str):
    n = len(u)
    m = len(v)

    # matriz de costos
    dpm = [[0] * (m+1) for _ in range(n+1)]

    # matriz de pasos 
    pasos = [[""] * (m+1) for _ in range(n+1)]

    inicio = time.time()

    # inicializacion de la matriz
    for i in range(n+1):
        dpm[i][0] = i

    for j in range(m+1):
        dpm[0][j] = j

    

    # llenado de la matriz
    for i in range(1, n+1):
        for j in range(1, m+1):
            eliminar = dpm[i-1][j] + 1
            insertar = dpm[i][j-1] + 1  
            cambiar = dpm[i-1][j-1]

            if u[i-1] != v[j-1]:
                cambiar += 1
            mejor_costo = min(eliminar, insertar, cambiar)
            dpm[i][j] = mejor_costo

            if mejor_costo == cambiar:
                if u[i-1] == v[j-1]:
                    pasos[i][j] = f"mantener"
                else:
                    pasos[i][j] = f"cambiar"

            elif mejor_costo == eliminar:
                pasos[i][j] = f"eliminar"
            else:
                pasos[i][j] = f"insertar"


    fin = time.time()
    tiempo_ms = (fin - inicio) * 1000

    # reconstruccion de operaciones
    operaciones = []
    i = n
    j = m

    while i > 0 or j > 0:
        if i == 0:
            operaciones.append(f"Insertar '{v[j-1]}'")
            j -= 1
            continue
        if j == 0:
            operaciones.append(f"Eliminar '{u[i-1]}'")
            i -= 1
            continue

        operacion = pasos[i][j]

        match operacion:
            case "eliminar":
                operaciones.append(f"Eliminar '{u[i-1]}'")
                i -= 1

            case "insertar":
                operaciones.append(f"Insertar '{v[j-1]}'")
                j -= 1

            case "cambiar":
                operaciones.append(f"Cambiar '{u[i-1]}' por '{v[j-1]}'")
                i -= 1
                j -= 1

            case "mantener":
                operaciones.append(f"Mantener '{u[i-1]}'")
                i -= 1
                j -= 1

    operaciones.reverse()

    return dpm[n][m], tiempo_ms, operaciones

