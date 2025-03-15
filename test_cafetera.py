# test_cafetera.py

import unittest
from cafetera import Vaso, Azucarero, Cafetera

class TestCafetera(unittest.TestCase):
    def setUp(self):
        self.vasos = {'pequeño': 3, 'mediano': 5, 'grande': 7}
        self.azucarero = Azucarero(10)
        self.cafetera = Cafetera(20, self.vasos, self.azucarero)

    def test_seleccionar_vaso_pequeño(self):
        resultado = self.cafetera.servir_cafe('pequeño', 2)
        self.assertEqual(resultado, "Café servido correctamente.")

    def test_seleccionar_vaso_mediano(self):
        resultado = self.cafetera.servir_cafe('mediano', 3)
        self.assertEqual(resultado, "Café servido correctamente.")

    def test_seleccionar_vaso_grande(self):
        resultado = self.cafetera.servir_cafe('grande', 4)
        self.assertEqual(resultado, "Café servido correctamente.")

    def test_azucar_insuficiente(self):
        self.azucarero.cantidad = 1
        resultado = self.cafetera.servir_cafe('pequeño', 2)
        self.assertEqual(resultado, "No hay suficientes recursos para preparar el café.")

    def test_cafe_insuficiente(self):
        self.cafetera.cafe = 2
        resultado = self.cafetera.servir_cafe('mediano', 1)
        self.assertEqual(resultado, "No hay suficientes recursos para preparar el café.")

    def test_vaso_invalido(self):
        resultado = self.cafetera.servir_cafe('extra grande', 2)
        self.assertEqual(resultado, "Tamaño de vaso inválido.")


    def test_rellenar_recursos(self):
        # Guardamos el estado inicial
        cafe_inicial = self.cafetera.cafe
        azucar_inicial = self.azucarero.cantidad
        vasos_iniciales = self.vasos.copy()

        # Rellenamos recursos
        self.cafetera.rellenar_recursos(10, 5, {'pequeño': 2, 'grande': 1})

        # Verificamos que los recursos se han incrementado correctamente
        self.assertEqual(self.cafetera.cafe, cafe_inicial + 10)
        self.assertEqual(self.azucarero.cantidad, azucar_inicial + 5)
        self.assertEqual(self.vasos['pequeño'], vasos_iniciales['pequeño'] + 2)
        self.assertEqual(self.vasos['grande'], vasos_iniciales['grande'] + 1)

if __name__ == '__main__':
    unittest.main()
