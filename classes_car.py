from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class Vehicule(ABC):
    couleur: str
    marque: str
    modele: str
    prixht: float
    prixttc: float
    reduction_applicable: float

    @property
    @abstractmethod
    def options(self):
        pass

    def __str__(self):
        return f'{self.couleur=}, {self.marque=}, {self.modele=}, {self.prixht=}, {self.prixttc=}, {self.reduction_applicable=}'

    def __repr__(self):
        return f'{self.couleur=}, {self.marque=}, {self.modele=}, {self.prixht=}, {self.prixttc=}, {self.reduction_applicable=}'


@dataclass
class Voiture(Vehicule):
    options: list[str] = field(default_factory=list)
    options_voiture: ClassVar[list(str)] = ['option1', 'option2', 'option3']

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, option):
        if not option in self.options_voiture:
            raise ValueError("Cette option n'est pas disponible pour ce type de véhicule")
        self.options.append(option)


@dataclass
class Moto(Vehicule):
    options: list(str) = field(default_factory=list)
    options_moto: ClassVar[list(str)] = ['option1', 'option2', 'option3']

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, option):
        if not option in self.options_moto:
            raise ValueError("Cette option n'est pas disponible pour ce type de véhicule")
        self.options.append(option)


@dataclass
class Camion(Vehicule):
    options: list(str) = field(default_factory=list)
    options_camion: ClassVar[list(str)] = ['option1', 'option2', 'option3']

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, option):
        if not option in self.options_camion:
            raise ValueError("Cette option n'est pas disponible pour ce type de véhicule")
        self.options.append(option)

@dataclass
class Vendeur:

    nom: str
    senior: bool
    nombre_ventes: int = 0

    def creer_vente(self, voiture):
        self.nombre_ventes += 1
        return Vente([self], voiture)

@dataclass
class Vente:

    vendeurs: list[Vendeur]
    vehicule: Vehicule
    prix: int = vehicule.prixttc
    reduction: bool = False

    def __str__(self):
        return f'Vendeurs: {self.vendeurs}, Infos véhicule: {self.vehicule} pour {self.prix}'

    def __repr__(self):
        return f'Vendeurs: {self.vendeurs}, Infos véhicule: {self.vehicule} pour {self.prix}'

    def imprimer_en_pdf(self):
        print(f"Impression en PDF terminée: {self}")

    def appliquer_reduction(self, Vendeur):
        if not Vendeur.senior:
            raise ValueError("Ce vendeur n'est pas habilité à appliquer une réduction")
        self.reduction = True
        self.prix = self.prix*(1-self.vehicule.reduction_applicable)
        if not Vendeur in self.vendeurs:
            self.vendeurs.append(Vendeur)

@dataclass
class Concessionnaire:

    adresse: str
    siret: int
    vendeurs: list(Vendeur)
    inventaire: list(Voiture) = field(default_factory=list)

    def afficher_voiture_par_marque(self, marque):
        return len([voiture for voiture in self.inventaire if voiture.marque == marque])

    def add_inventaire(self, voiture):
        self.inventaire.append(voiture)

    def remove_inventaire(self, voiture):
        self.inventaire.remove(voiture)






    # class Voiture:
#     def __init__(self, marque, prix):
#         self.marque = marque
#         self.prix = prix
#
#     def appliquer_reduction(self, taux_reduction):
#         return taux_reduction * self.prix