import math

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

        # Fórmula del área (shoelace)
        area += (x_i * y_next) - (x_next * y_i)

        # Distancia euclidiana para el perímetro
        perimetro += math.sqrt((x_next - x_i)**2 + (y_next - y_i)**2)

    area = abs(area) / 2
    return area, perimetro

# Ejemplo de uso:
vertices = [(1, 2), (4, 5), (7, 1)]
area, perimetro = poligono_area_perimetro(vertices)
print(f"Área: {area}")
print(f"Perímetro: {perimetro}")
