import math

def check_condiciones(pais_i, color_i, pais_j, color_j):
    if (pais_i, pais_j) in [('A', 'C'), ('C', 'A')]: # Restricción: Países vecinos no pueden tener el mismo color
        return color_i != color_j
    elif (pais_i, pais_j) in [('A', 'B'), ('B', 'A'), ('B', 'D'), ('D', 'B')]: # Restricción: Países vecinos no pueden tener el mismo color
        return color_i != color_j
    elif (pais_i, pais_j) in [('C', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'C'), ('C', 'E'), ('E', 'C'), ('D', 'E'), ('E', 'D')]: # Restricción: Países vecinos no pueden tener el mismo color
        return color_i != color_j
    else:
        return True

def arc_consistency(variables, dominios):
    cambio = True

    while cambio:
        cambio = False

        for restriccion in restricciones:
            pais_i, pais_j = restriccion

            for color_vi in dominios[pais_i][:]:
                compatible = False

                for color_vj in dominios[pais_j]:
                    if color_vi != color_vj:
                        if check_condiciones(pais_i, color_vi, pais_j, color_vj):
                            compatible = True
                            break

                if not compatible:
                    dominios[pais_i].remove(color_vi)
                    cambio = True

    return dominios


variables = ['A', 'B', 'C', 'D', 'E']  # Definir las variables (países)
dominios = {
    'A': ['Azul'],
    'B': ['Rojo'],
    'C': ['Rojo', 'Verde', 'Azul'],
    'D': ['Rojo', 'Verde', 'Azul'],
    'E': ['Rojo', 'Verde', 'Azul']
}

restricciones = [
    ('A', 'C'), ('C', 'A'), # Fronteras entre países
    ('A', 'B'), ('B', 'A'), ('B', 'D'), ('D', 'B'), # Fronteras entre países
    ('C', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'C'), ('C', 'E'), ('E', 'C'), ('D', 'E'), ('E', 'D') # Fronteras entre países
]

# Se ejecuta el algoritmo de consistencia en arcos
dominios = arc_consistency(variables, dominios)

# Imprimir los dominios finales
print("Dominios finales:")
for pais, colors in dominios.items():
    print(f"País {pais}: {colors}")
