class Citron:
    def __init__(self):
        self.couleur = "jaune"

    def affichage(self):
        return f"La couleur est {self.couleur}"

citron1 = Citron()
print(citron1)