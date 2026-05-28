def formatear_tiempo(tiempo_ms):
    if tiempo_ms < 1000:

        return f"{round(tiempo_ms, 4)} ms"

    elif tiempo_ms < 60000:
        segundos = tiempo_ms / 1000
        return f"{round(segundos, 4)} s"

    elif tiempo_ms < 3600000:
        minutos = int(tiempo_ms // 60000)
        segundos = (tiempo_ms % 60000) / 1000
        return f"{minutos} min {round(segundos, 2)} s"
    else:

        horas = int(tiempo_ms // 3600000)
        resto = tiempo_ms % 3600000
        minutos = int(resto // 60000)
        segundos = (resto % 60000) / 1000
        return (
            f"{horas} h "
            f"{minutos} min "
            f"{round(segundos, 2)} s"
        )

def test(algoritmo, pruebas):

    print("=" * 70)
    print(f"RESULTADOS - {algoritmo.__name__.upper()}")
    print("=" * 70)

    for i, (cadena1, cadena2) in enumerate(pruebas, start=1):
        inicio = time.time()
        distancia, operaciones = algoritmo(
            cadena1,
            cadena2
        )

        fin = time.time()
        tiempo_ms = (fin - inicio) * 1000
        cantidad_operaciones = len(operaciones)
        print(f"\nPrueba #{i}")
        print("-" * 70)
        print(f"Cadena U   : {cadena1}")
        print(f"Cadena V   : {cadena2}")
        print(f"Distancia  : {distancia}")
        print(f"Operaciones: {cantidad_operaciones}")
        print( f"Tiempo     : {formatear_tiempo(tiempo_ms)}")
    print("\n" + "=" * 70)
#esta 2 te sirve para testear diferentes cadenas de codigo juntas para ver cuanto demoran y tal 

pruebas = [
    ("gato", "gata"),
    ("abcdefghij", "jihgfedcba"),

    ("x"*10, "y"*10),
]

test("Nombre del algoritmos",pruebas)




#este es para solo evaluar 1 y que te retorne cuales oepraciones hizo y cuantas de cada una etc

import time

def aux(algoritmo, u, v):

    inicio = time.time()
    distancia, operaciones = algoritmo(u, v)
    tiempo_ms = (time.time() - inicio) * 1000

    insertar = sum("insertar" in op.lower() for op in operaciones)
    eliminar = sum("eliminar" in op.lower() for op in operaciones)
    cambiar  = sum("cambiar"  in op.lower() for op in operaciones)
    mantener = sum("mantener" in op.lower() for op in operaciones)

    print("=" * 50)
    print(f"Algoritmo : {algoritmo.__name__}")
    print(f"Cadena U  : {u}")
    print(f"Cadena V  : {v}")

    print("\nOperaciones:")
    for op in operaciones:
        print("-", op)

    print(f"\nDistancia : {distancia}")

    print("\nResumen:")
    print(f"Insertar : {insertar}")
    print(f"Eliminar : {eliminar}")
    print(f"Cambiar  : {cambiar}")
    print(f"Mantener : {mantener}")

    print(f"\nTiempo : {round(tiempo_ms, 3)} ms")
    print("=" * 50)
    
    
    
aux("algoritmo","hola", "hello")