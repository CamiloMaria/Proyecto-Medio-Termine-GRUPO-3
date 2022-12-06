import unittest

from Paises import Paises

paises = Paises()

class TestCRUD(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_insertar(self):
        actual = paises.modificar_pais("RPD", "Republica Pacheca Dominicana", "Pachequita", "RPS")
        self.assertEqual(actual, 1) 
  
    def test_modificar(self):
        actual = paises.modificar_pais(7, "PLD", "Pelicanos La Dominicana", "Pelicanos", "PLS")
        self.assertEqual(actual, 1) 

    def test_delete(self):
        actual = paises.eliminar_pais(8)
        self.assertEqual(actual, 1)


if __name__ == '__main__':
    unittest.main()