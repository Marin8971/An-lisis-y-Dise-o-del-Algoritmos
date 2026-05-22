import time

def dyv(u, v):
    m = len(u)  # Paso Base
    n = len(v)  # Cadena Objetivo

    memoria = {}     # Guarda costos mínimos
    pasos = {} # Guarda la operación elegida

    def resolver(i, j):

        # Si u quedó vacía
        if i == 0:
            return j

        # Si v quedó vacía
        if j == 0:
            return i

        # Si ya se calculó
        if (i, j) in memoria:
            return memoria[(i, j)]

        eliminar = resolver(i - 1, j) + 1
        insertar = resolver(i, j - 1) + 1
        cambiar = resolver(i - 1, j - 1)

        if u[i - 1] != v[j - 1]:
            cambiar += 1

        mejor = min(eliminar, insertar, cambiar) #escogemos el valor minimo

        memoria[(i, j)] = mejor

        # Guardar operación elegida
        if mejor == eliminar:
            pasos[(i, j)] = "eliminar"

        elif mejor == insertar:
            pasos[(i, j)] = "insertar"

        else:
            if u[i - 1] == v[j - 1]:
                pasos[(i, j)] = "mantener"
            else:
                pasos[(i, j)] = "cambiar"

        return mejor

    # Medir tiempo
    inicio = time.time()
    distancia = resolver(m, n)
    fin = time.time()

    tiempo_ms = (fin - inicio) * 1000

    # Reconstrucción de operaciones
    operaciones = []

    i = m
    j = n

    while i > 0 or j > 0:

      if i == 0: # si la cadena base es vacia, insertamos todos los elementos hasta llegar al objetivo
        operaciones.append(f"Insertar '{v[j-1]}'")
        j -= 1 
        continue # volvemos al inicio (while)
      if j == 0: # si la cadena objetivo es vacia, elimanos 1 a 1 los elemento de la cadeba base
        operaciones.append(f"Eliminar '{u[i-1]}'")
        i -= 1
        continue #volvemos al inicio (while)
      operacion = pasos.get((i, j))

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

    return distancia, tiempo_ms, operaciones






#----------FUNCION AUXILIAR PARA ESCRIBIR--------------------------------------------------

def aux(u, v):

    distancia, tiempo_ms, operaciones = dyv(u, v)

    print("Operaciones:\n")

    for op in operaciones:
        print("-", op)

    print("\nDistancia:", distancia)
    print("Tiempo:", round(tiempo_ms, 3), "ms")




#--------------------------------------CASO PARTICULAR----------------
#en este al usar aux podemos ver el paso a paso que se realizo
aux("hola", "")








#-----------------EVALUACION DE CASOS DE PRUEBA---------------------------------------


pruebas = [
    ("gato", "gata"),

    ("abcdefghij", "jihgfedcba"),

    ("murcielago", "electroencefalografista"),

    ("", "supercalifragilisticoespialidoso"),

    ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
     "aaaaabaaaaacaaaaadaaaaaeaaaaaf"),


    ("@#&*!?/$%abcdef",
     "abcdef@#&*!?/$%"),


    ("la inteligencia artificial cambiara el mundo",
     "la inteligencia humana cambiara profundamente el futuro"),


    ("Lorem ipsum dolor sit amet consectetur adipiscing elit",
     "Dolor sit amet lorem ipsum adipiscing elit consectetur"),

    ("a" * 100,
     "a" * 99 + "b"),

    ("z" * 80,
     "x" * 80)
]

resultados = []

resultados = []

for cadena1, cadena2 in pruebas:

    distancia, tiempo_ms, _ = dyv(cadena1, cadena2)

    resultados.append({
        "u": cadena1,
        "v": cadena2,
        "distancia": distancia,
        "tiempo_ms": round(tiempo_ms, 7)
    })

print("=" * 70)
print("RESULTADOS DE PRUEBAS")
print("=" * 70)

for i, resultado in enumerate(resultados, start=1):

    print(f"\nPrueba #{i}")
    print("-" * 70)

    print(f"Cadena U   : {resultado['u']}")
    print(f"Cadena V   : {resultado['v']}")
    print(f"Distancia  : {resultado['distancia']}")
    print(f"Tiempo     : {resultado['tiempo_ms']} ms")

print("\n" + "=" * 70)