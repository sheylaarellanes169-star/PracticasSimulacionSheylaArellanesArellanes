def congruencial_lineal(seed, a, c, m, cantidad):
    numeros = []
    x = seed
    for _ in range(cantidad):
        x = (a * x + c) % m
        numeros.append(x / m)  # Normalizado entre 0 y 1
    return numeros

# Pedir datos al usuario
print("== MÉTODO CONGRUENCIAL LINEAL ==")
seed = int(input("Ingrese la semilla (X0): "))
a = int(input("Ingrese el multiplicador (a): "))
c = int(input("Ingrese el incremento (c): "))
m = int(input("Ingrese el módulo (m): "))
cantidad = int(input("¿Cuántos números desea generar?: "))

# Generar números
numeros_generados = congruencial_lineal(seed, a, c, m, cantidad)

# Mostrar resultados
print("\nNúmeros generados (normalizados entre 0 y 1):")
for i, num in enumerate(numeros_generados, 1):
    print(f"{i}: {num}")
