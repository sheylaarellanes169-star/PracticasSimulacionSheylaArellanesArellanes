# Método del Cuadrado Medio


def cuadrado_medio(semilla, cantidad):
    numeros = []
    n = len(str(semilla))  # cantidad de dígitos de la semilla
    
    for i in range(cantidad):
        cuadrado = semilla ** 2
        cuadrado_str = str(cuadrado).zfill(2 * n)  # completa con ceros si falta
        # Tomar los dígitos del medio
        inicio = (len(cuadrado_str) - n) // 2
        fin = inicio + n
        semilla = int(cuadrado_str[inicio:fin])
        numeros.append(semilla)
        
        print(f"Iteración {i+1}: Cuadrado={cuadrado_str} -> Nuevo número={semilla}")
    
    return numeros


# Ejemplo de uso
semilla_inicial = 5731
cantidad_numeros = 5

resultado = cuadrado_medio(semilla_inicial, cantidad_numeros)

print("\ resultado: ")
for i, num in enumerate(resultado, start=1):
    print(f"{i}. {num}")