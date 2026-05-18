#Problema IV subpunto C y B

import itertools

def max_tiempo_ocupacion_voraz(reuniones):
    reuniones_ord = sorted(reuniones, key=lambda x: x[1]-x[0], reverse=True)
    ocupados = []
    seleccionadas = []
    for ini, fin in reuniones_ord:
        if all(fin <= a or b <= ini for a, b in ocupados):
            seleccionadas.append((ini, fin))
            ocupados.append((ini, fin))
    tiempo = sum(f - s for s, f in seleccionadas)
    return seleccionadas, tiempo

def tiempo_optimo(reuniones):
    n = len(reuniones)
    mejor = 0
    for r in range(1, n+1):
        for comb in itertools.combinations(reuniones, r):
            ordenado = sorted(comb, key=lambda x: x[0])
            compatible = True
            for i in range(len(ordenado)-1):
                if ordenado[i][1] > ordenado[i+1][0]:
                    compatible = False
                    break
            if compatible:
                tiempo = sum(f-s for s, f in comb)
                if tiempo > mejor:
                    mejor = tiempo
    return mejor

reuniones_prueba = [(0,10), (0,4), (4,8), (8,12), (12,16)]

# Ejecutar algoritmo voraz
sel_voraz, t_voraz = max_tiempo_ocupacion_voraz(reuniones_prueba)
# Calcular óptimo
t_optimo = tiempo_optimo(reuniones_prueba)

print("Reuniones disponibles:", reuniones_prueba)
print("Solución voraz (mayor duración primero):")
print("  Seleccionadas:", sel_voraz)
print("  Tiempo total:", t_voraz)
print("Tiempo óptimo (fuerza bruta):", t_optimo)
print("¿Es óptimo el voraz?:", t_voraz == t_optimo)