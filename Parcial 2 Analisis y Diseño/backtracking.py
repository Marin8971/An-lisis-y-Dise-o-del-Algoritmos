import time


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

    inicio = time.time()
    backtracking(len(u), len(v), 0, [])
    fin = time.time()
    tiempo_ms = (fin - inicio) * 1000
    mejor_camino.reverse()

    return mejor_distancia[0], tiempo_ms, mejor_camino




#----------FUNCION AUXILIAR PARA ESCRIBIR--------------------------------------------------
#esta funcion es universal para los algoritmos, si te parece comoda usarla

def aux(algoritmo, u, v):

    distancia, tiempo_ms, operaciones = algoritmo(u, v)

    print("=" * 50)
    print(f"Algoritmo : {algoritmo.__name__}")
    print(f"Cadena U  : {u}")
    print(f"Cadena V  : {v}")

    print("\nOperaciones:\n")

    for op in operaciones:
        print("-", op)

    print("\nDistancia :", distancia)
    print("Tiempo    :", round(tiempo_ms, 3), "ms")
    print("=" * 50)



#--------------------------------------CASO PARTICULAR----------------
#en este al usar aux podemos ver el paso a paso que se realizo

aux(backtracking,"gato","gata")





#------------------FUNCIONES AXULIAR PARA PRUEBAS---------------------
#esta es universal si se sigue la misma logica en los 3 algoritmos


#------------------FUNCIONES AXULIAR PARA PRUEBAS---------------------
#esta es universal si se sigue la misma logica en los 3 algoritmos


def test(algoritmo, pruebas):

    print("=" * 70)
    print(f"RESULTADOS - {algoritmo.__name__.upper()}")
    print("=" * 70)

    for i, (cadena1, cadena2) in enumerate(pruebas, start=1):

        distancia, tiempo_ms, _ = algoritmo(cadena1, cadena2)

        print(f"\nPrueba #{i}")
        print("-" * 70)

        print(f"Cadena U   : {cadena1}")
        print(f"Cadena V   : {cadena2}")

        print(f"Distancia  : {distancia}")
        print(f"Tiempo     : {formatear_tiempo(tiempo_ms)}")

    print("\n" + "=" * 70)
    
    
def formatear_tiempo(tiempo_ms):


    if tiempo_ms < 1000:
        return f"{round(tiempo_ms, 4)} ms"

    elif tiempo_ms < 60000:
        segundos = tiempo_ms / 1000
        return f"{round(segundos, 4)} s"


    else:
        minutos = int(tiempo_ms // 60000)
        segundos = (tiempo_ms % 60000) / 1000
        return f"{minutos} min {round(segundos, 2)} s"









#-----------------EVALUACION DE CASOS DE PRUEBA---------------------------------------
#esto es provicional, mientras organizo y busco datos que demoren mucho
pruebas = [

    # Igualdad exacta
    ("hola", "hola"),

    # Un cambio
    ("gato", "gata"),

    # Cadena vacía 
    ("", "casa"),

    # Cadena vacía 
    ("mesa", ""),

    # Repeticiones
    ("aaaa", "aaab"),

    # Símbolos
    ("@#!", "#@!"),


    # Números
    ("12345", "123"),

    # Mezcla corta
    ("a1b2", "ab12"),

    # Palabras  distintas
    ("luna", "sol"),

    # Eliminaciones múltiples
    ("abcdef", "abc"),

    # Palabras similares
    ("algoritmo", "algoritmos"),

    # caso grande
    ("z" * 20,
     "x" * 20)
]


test(backtracking,pruebas)