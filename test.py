import unittest

from Paises import Paises

paises = Paises()

class TestCRUD(unittest.TestCase):
    def test_delete():
        # Delete an existing item and verify that it has been removed from the database
        assert paises.eliminar_pais(10)

    

