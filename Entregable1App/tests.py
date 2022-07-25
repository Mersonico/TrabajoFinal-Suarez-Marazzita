from django.test import TestCase

from .models import Cancha

class CanchasTest(TestCase):
    
    def setUp(self):
        Cancha.objects.create(tipo="Cristian", tamaño=2)
        
    def test_cancha_nombre(self):
        chancha = Cancha.objects.get(tamaño=2)
        self.assertEqual(Cancha.nombre, "Cristian")
    
    def test_cancha_creado(self):
        cancha = Cancha.objects.get(tamaño=2)
        self.assertNotEquals(cancha, None)
        
