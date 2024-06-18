import math

def check_condiciones(Xi, valor_vk, Xj, valor_vl):
    if (Xi == 0 and Xj == 2) or (Xi == 2 and Xj == 0):  # Restricción 1: Igualdad módulo 5: V1 ≡ V3 (mod 5)
        return valor_vk % 5 == valor_vl % 5
    elif (Xi == 0 and Xj == 1) or (Xi == 1 and Xj == 0):# Restricción 3: No primos entre sí: mcd(V1, V2) > 1
        return math.gcd(valor_vk, valor_vl) > 1
    elif (Xi == 1 and Xj == 3):  # Restricción 2: Mayor que: V4 = V2 + 1
        return valor_vk == valor_vl - 1
    elif (Xi == 3 and Xj == 1):
        return valor_vk == valor_vl + 1
    else:
        return True # No se aplican restricciones para otras variables

def ac3(variables, dominios):
    cambio = True

    while cambio:
        cambio = False

        for restriccion in restricciones:
            Xi, Xj = restriccion

            for valor_vk in dominios[Xi][:]:
                compatible = False

                for i, valor_vl in enumerate(dominios[Xj]):
                    if i+2 != valor_vk:  # No comparar si vk y vl son iguales
                        if check_condiciones(Xi, valor_vk, Xj, valor_vl):
                            compatible = True
                            break

                if not compatible:
                    dominios[Xi].remove(valor_vk)
                    cambio = True

    return dominios


variables = [0, 1, 2, 3]  # Definir las variables
dominios = {
    0: [2, 3, 4, 5, 6, 7, 8, 9],
    1: [2, 3, 4, 5, 6, 7, 8, 9],
    2: [2, 3, 4, 5, 6, 7, 8, 9],
    3: [2, 3, 4, 5, 6, 7, 8, 9]  # Se ha modificado el dominio de V4 para que solo contenga valores mayores que 2
}

restricciones = [
    (0, 2), # V1 Igualdad módulo 5: V1 ≡ V3 (mod 5)
    (0, 1), # V1 No primos entre sí: mcd(V1, V2) > 1  
    (1, 3), # V2 Mayor que: V4 = V2 + 1
    (1, 0), # V2 No primos entre sí: mcd(V1, V2) > 1
    (2, 0), # V3 Igualdad módulo 5: V1 ≡ V3 (mod 5)
    (3, 1) # V4 Mayor que: V4 = V2 + 1
    ]

# Se ejecuta el algoritmo de consistencia en arcos
dominios = ac3(variables, dominios)

# Imprimir los dominios finales
print("Dominios finales:")
for variable, dominio in dominios.items():
    print(f"Variable X{variable+1}: {dominio}")
