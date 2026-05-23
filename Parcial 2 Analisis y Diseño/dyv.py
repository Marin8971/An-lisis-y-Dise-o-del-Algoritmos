import time

import time

def dyv(u, v):
    # u = cadena base
    # v = cadena objetivo
    def resolver(pos_u, pos_v):

        if pos_u == 0: # si la cadena base es vacia, insetamos los valores faltantes
            operaciones = [f"Insertar '{v[k]}'"for k in range(pos_v)]
            return pos_v, operaciones


        if pos_v == 0: # si la cadena objetivo es vacia, eliminamos todos los caracteres de la cadeba base
            operaciones = [ f"Eliminar '{u[k]}'" for k in range(pos_u)]
            return pos_u, operaciones

        # eliminacion de caracteres
        costo_eliminar, operaciones_eliminar = resolver(pos_u - 1, pos_v)
        costo_eliminar += 1
        operaciones_eliminar = (operaciones_eliminar + [f"Eliminar '{u[pos_u - 1]}'"])

        # Insertacion de Caracteres
        costo_insertar, operaciones_insertar = resolver(pos_u, pos_v - 1)
        costo_insertar += 1
        operaciones_insertar = (operaciones_insertar+ [f"Insertar '{v[pos_v - 1]}'"])

        # Cambio o mantenimiento de caracteres
        costo_cambiar, operaciones_cambiar = resolver(pos_u - 1, pos_v - 1)

        if u[pos_u - 1] != v[pos_v - 1]: # si los caracteres son diferentes se realiza un cambio
          costo_cambiar += 1
          operaciones_cambiar = ( operaciones_cambiar + [f"Se cambio "f"'{u[pos_u - 1]}' "f"por "f"'{v[pos_v - 1]}'"])

        else: # si son iguales se mantiene el cambio y continua
          operaciones_cambiar = ( operaciones_cambiar + [f"Mantener '{u[pos_u - 1]}'"])

        # elecion de la mejor opcion
        if (costo_eliminar <= costo_insertar and costo_eliminar <= costo_cambiar):
            return costo_eliminar, operaciones_eliminar

        elif (costo_insertar <= costo_eliminar and costo_insertar <= costo_cambiar):
            return costo_insertar, operaciones_insertar

        else:
            return costo_cambiar, operaciones_cambiar



    inicio = time.time()
    distancia, operaciones = resolver(len(u),len(v))
    fin = time.time()
    tiempo_ms = (fin - inicio) * 1000

    return distancia, tiempo_ms, operaciones











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
aux(dyv,"hola", "")










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

    # Caso pequeño simple
    ("gato", "gata"),

    # Caracteres invertidos
    ("abcdefghij", "jihgfedcba"),

    # Palabras medianas con muchos cambios
    ("murcielago", "electroencefalografista"),

    # Frases con inserciones y reemplazos
    (
        "la inteligencia artificial cambiara el mundo",
        "la inteligencia humana cambiara profundamente el futuro"
    ),

    # Caracteres especiales y reordenamiento
    (
        "@#&*!?/$%abcdef",
        "abcdef@#&*!?/$%"
    )
]

test(dyv,pruebas)