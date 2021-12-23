class Vis:
    def __init__(self, taille, status="non vissée"):
        self.taille = taille
        self.status = status
    
    def visser(self):
        self.status = "non vissée" if self.status == "vissée" else "vissée"

class Tournevis:
    def __init__(self,marque):
        self.marque = marque

    def vissage(self,vis:Vis):
        vis.visser()

class Clou:
    def __init__(self, taille, status="non cloué"):
        self.taille = taille
        self.status = status
    
    def clouer(self):
        if self.status == "non cloué":
            self.status = "cloué"
        elif self.status == "cloué":
            print("le clou est déja cloué")


class Marteau:
    def __init__(self,marque):
        self.marque = marque

    def clouage(self,clou:Clou):
        clou.clouer()


class Toolbox:
    nb_emplacement = 5

    @classmethod
    def update(cls):
        cls.nb_emplacement +=1

    def __init__(self):
        self.contenu = []

    def add_to_toolbox(self,Tool):
        if len(self.contenu) < self.__class__.nb_emplacement:
            self.contenu.append(Tool)
        else:
            print("ma boite à outil est pleine")

    def remove_from_toolbox(self,Tool):
        if Tool in self.contenu:
            self.contenu.remove(Tool)

ma_vis = Vis(10)
mon_tournevis = Tournevis("facom")

mon_tournevis.vissage(ma_vis)
print(ma_vis.status)
mon_tournevis.vissage(ma_vis)
print(ma_vis.status)

mon_clou = Clou(13)
mon_marteau = Marteau("facom")

print(mon_clou.status)
mon_marteau.clouage(mon_clou)

mon_marteau.clouage(mon_clou)
print(mon_clou.status)

boite_outil = Toolbox()

boite_outil.add_to_toolbox(mon_marteau)
boite_outil.add_to_toolbox(mon_tournevis)
print(boite_outil.contenu)

boite_outil.remove_from_toolbox(mon_marteau)
print(boite_outil.contenu)

boite_outil.remove_from_toolbox(Tournevis("facom"))