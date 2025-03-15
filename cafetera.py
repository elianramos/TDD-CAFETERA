# cafetera.py

class Vaso:
    def __init__(self, capacidad, cantidad):
        self.capacidad = capacidad
        self.cantidad = cantidad

class Azucarero:
    def __init__(self, cantidad):
        self.cantidad = cantidad

    def usar_azucar(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            return True
        return False

class Cafetera:
    def __init__(self, cafe, vasos, azucarero):
        self.cafe = cafe
        self.vasos = vasos
        self.azucarero = azucarero

    def servir_cafe(self, tamaño, azucar):
        tamaño_vaso = {'pequeño': 3, 'mediano': 5, 'grande': 7}
        
        if tamaño not in tamaño_vaso:
            return "Tamaño de vaso inválido."
        
        if self.cafe < tamaño_vaso[tamaño]:
            return "No hay suficientes recursos para preparar el café."
        
        if self.vasos[tamaño] <= 0:
            return "No hay vasos disponibles."
        
        if not self.azucarero.usar_azucar(azucar):
            return "No hay suficientes recursos para preparar el café."
        
        self.cafe -= tamaño_vaso[tamaño]
        self.vasos[tamaño] -= 1
        
        return "Café servido correctamente."
    class Cafetera:
    def __init__(self):
        self.cafe = 0  # Asumiendo que tienes este atributo
        self.leche = 0
        self.azucar = 0
        self.vasos = {'pequeño': 0, 'grande': 0}  # Asumiendo estructura de vasos

  return "Café servido correctamente."
   def rellenar_recursos(self, cafe, azucar, vasos):
    self.cafe += cafe
    self.azucarero.cantidad += azucar
    for tamaño, cantidad in vasos.items():
        if tamaño in self.vasos:
            self.vasos[tamaño] += cantidad

