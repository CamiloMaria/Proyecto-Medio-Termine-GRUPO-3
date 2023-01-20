import unittest

from Paises import Paises

paises = Paises()

class TestCRUD(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_insertar(self):
        actual = paises.insertar_pais("PLS", "Republica Pacheca Dominicana", "Pachequita", "RE3")
        self.assertEqual(actual, 1) 
  
    def test_delete(self):
        actual = paises.eliminar_pais(16)
        self.assertEqual(actual, 1)
        
    def test_modificar(self):
        actual = paises.modificar_pais(7, "PTS", "Pelicanos La Dominicana", "Pelicanos", "XCC")
        self.assertEqual(actual, 1) 




if __name__ == '__main__':
    unittest.main()