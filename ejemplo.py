import math
import random

def generar_poligono(n, rango=100):
    """
    Genera un polígono aleatorio con n vértices.
    n: número de vértices
    rango: valor máximo de las coordenadas x e y
    Retorna una lista de tuplas [(x1, y1), (x2, y2), ..., (xn, yn)]
    """
    coords = []
    for _ in range(n):
        x = random.randint(0, rango)
        y = random.randint(0, rango)
        coords.append((x, y))
    return coords

def poligono_area_perimetro(coords):
    """
    Calcula el área y perímetro de un polígono dado una lista de coordenadas.
    coords: lista de tuplas [(x1, y1), (x2, y2), ..., (xn, yn)]
    Retorna una tupla: (area, perimetro)
    """
    n = len(coords)
    area = 0
    perimetro = 0

    for i in range(n):
        x_i, y_i = coords[i]
        x_next, y_next = coords[(i + 1) % n]  # cierra el polígono

        # Área (shoelace formula)
        area += (x_i * y_next) - (x_next * y_i)

        # Perímetro (distancia euclidiana)
        perimetro += math.sqrt((x_next - x_i)**2 + (y_next - y_i)**2)

    area = abs(area) / 2
    return area, perimetro

# ----------------------------
# Ejemplo con 50 vértices
# ----------------------------

num_vertices = 50
poligono = generar_poligono(num_vertices)

# Mostrar las coordenadas del polígono
print("Coordenadas del polígono:")
for i, (x, y) in enumerate(poligono, start=1):
    print(f"Vértice {i}: ({x}, {y})")

# Calcular área y perímetro
area, perimetro = poligono_area_perimetro(poligono)

print("\nResultados:")
print(f"Área del polígono: {area}")
print(f"Perímetro del polígono: {perimetro}")
