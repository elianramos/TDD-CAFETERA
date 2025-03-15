class Cafetera:
    def __init__(self, cafe, vasos, azucarero):
        self.cafe = cafe
        self.vasos = vasos  # Atributo de la cafetera
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

    def rellenar_recursos(self, cafe, azucar, vasos):
        self.cafe += cafe
        self.azucarero.cantidad += azucar
        for tamaño, cantidad in vasos.items():
            if tamaño in self.vasos:  # Usa el atributo de la cafetera
                self.vasos[tamaño] += cantidad
