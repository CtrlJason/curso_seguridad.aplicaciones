import unittest
from ..mi_proyecto.dominio import Tarea

class TestTarea(unittest.TestCase):
    def test_crear_tarea(self):
        tarea = Tarea("Comprar pan", "Ir ala tienda a comprar pan")
        self.assertEqual(tarea.nombre, "Comprar pan")
        self.assertEqual(tarea.descripcion, "Ir a la tienda a comprar pan")

if __name__ == "__main__":
    unittest.main()