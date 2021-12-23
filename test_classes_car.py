from classes_car import Vehicule, Voiture, Moto, Camion, Concessionnaire, Vendeur, Vente
import pytest


class TestVehicule():
   def test_print(self):
      # Cette ligne permet de supprimer toutes les abstactmethod
      Vehicule.__abstractmethods__ = set()
      # On peut donc instatancier un vehicule
      my_vehicule = Vehicule('rouge', 'toyota', 'yaris', 19000, 20000, 0.1)
      # Et tester ses méthodes qui ne sont pas des abstractmethod
      assert str(my_vehicule) == 'couleur=rouge, marque=toyota, model=yaris, prixht=19000, prixttc=20000, reduction_applicable=0.1'


@pytest.fixture
def voiture_test():
   return Voiture('rouge', 'toyota', 'yaris', 19000, 20000, 0.1)

@pytest.fixture
def camion_test():
   return Camion('rouge', 'cam', 'ion', 19000, 20000, 0.1)

@pytest.fixture
def moto_test():
   return Voiture('rouge', 'mo', 'to', 19000, 20000, 0.1)

@pytest.fixture
def junior_test():
   return Vendeur('junior', False)

@pytest.fixture
def senior_test():
   return Vendeur('senior', True)

@pytest.fixture
def vente_test():
   return Vente([senior_test], voiture_test)



class TestVoiture():
   def test_options(self):
      with pytest.raises(ValueError):
         voiture_test.options('Mauvaise option')
      voiture_test.options('option1')
      assert len(voiture_test.options) == 1


class TestVendeur():
   def test_creer_vente(self):
      senior_test.creer_vente(voiture_test)
      assert senior_test.nombre_ventes == 1

class TestVente():
   print(vente_test)

   def test_imprimer_en_pdf(self):
      print(vente_test.imprimer_en_pdf())

   def test_appliquer_reduction(self):
      with pytest.raises(ValueError):
         vente_test.appliquer_reduction(junior_test)
      vente_test.appliquer_reduction(senior_test)
      assert len(vente_test.vendeurs == 1)
      assert vente_test.prix == 18000

