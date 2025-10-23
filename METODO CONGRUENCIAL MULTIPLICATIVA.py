# MÉTODO CONGRUENCIAL MULTIPLICATIVO

def congruencial_multiplicativo(seed, a, m, cantidad):
    numeros = []
    x = seed
    for _ in range(cantidad):
        x = (a * x) % m
        numeros.append(x / m)  # Normalizar entre 0 y 1
    return numeros

# Solicitar datos al usuario
print("== MÉTODO CONGRUENCIAL MULTIPLICATIVO ==")
seed = int(input("Ingresa la semilla (X0): "))
a = int(input("Ingresa el valor de 'a' (multiplicador): "))
m = int(input("Ingresa el valor de 'm' (módulo): "))
cantidad = int(input("¿Cuántos números deseas generar?: "))

# Generar números
numeros = congruencial_multiplicativo(seed, a, m, cantidad)

# Mostrar resultados
print("\n--- Números generados ---")
for i, num in enumerate(numeros):
    print(f"X{i+1} = {num}")