class Voiture1:
    def __init__(self):
        self.__marque = "féfé"
        self.__modele = "F40"
        self.__puiss = "beaucoup"
        self.__couleur = "rouge"
        self.__options = []

    def __str__(self):
        return f"Voici les caractéristiques de cette voiture:\n- Marque: {self.__marque}\n- Modele: {self.__modele}\n- Couleur: {self.__couleur}\n- Puissance: {self.__puiss}\n- Option(s): {self.__options}"


    def affichage(self):
        return f"La voiture est un(e) {self.__marque} {self.__modele} de puissance {self.__puiss} et de couleur {self.__couleur}."

#       Accesseurs
    def get_marque(self):
        return self.__marque
    def get_modele(self):
        return self.__modele
    def get_puiss(self):
        return self.__puiss
    def get_couleur(self):
        return self.__couleur
    def get_options(self):
        return self.__options

#       Accesseurs en écriture
    def set_marque(self, marque):
        self.__marque = marque
    def set_modele(self, modele):
        self.__modele = modele
    def set_puiss(self, puiss):
        self.__puiss = puiss
    def set_couleur(self, couleur):
        self.__couleur = couleur

    def ajouter_option(self, opts):
        self.__options.append(opts)
    def supprimer_option(self, opt):
        self.__options.remove(opt)
    def is_option_present(self, opt):
        if opt in self.__options:
            print(f"L'option {opt} est présente.")
        else:
            print(f"L'option {opt} n'est pas présente.")



















class Voiture2:
    def __init__(self, marque, modele, puissance, couleur):
        self.__marque = marque
        self.__modele = modele
        self.__puiss = puissance
        self.__couleur = couleur

    def affichage(self):
        return f"La voiture est un(e) {self.__marque} {self.__modele} de puissance {self.__puiss} et de couleur {self.__couleur}."

#       Accesseurs
    def get_marque(self):
        return self.__marque
    def get_modele(self):
        return self.__modele
    def get_puiss(self):
        return self.__puiss
    def get_couleur(self):
        return self.__couleur

#       Accesseurs en écriture
    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_puiss(self, puiss):
        self.__puiss = puiss

    def set_couleur(self, couleur):
        self.__couleur = couleur







class Voiture3:
    def __init__(self, marque="Peugeot", modele="407SW", puissance="140", couleur="noir"):
        self.__marque = marque
        self.__modele = modele
        self.__puiss = puissance
        self.__couleur = couleur

    def affichage(self):
        return f"La voiture est un(e) {self.__marque} {self.__modele} de puissance {self.__puiss} et de couleur {self.__couleur}."

#       Accesseurs
    def get_marque(self):
        return self.__marque
    def get_modele(self):
        return self.__modele
    def get_puiss(self):
        return self.__puiss
    def get_couleur(self):
        return self.__couleur

#       Accesseurs en écriture
    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_puiss(self, puiss):
        self.__puiss = puiss

    def set_couleur(self, couleur):
        self.__couleur = couleur









class Voiture4:
    def __init__(self, marque, modele, puissance, couleur="jaune"):
        self.__marque = marque
        self.__modele = modele
        self.__puiss = puissance
        self.__couleur = couleur

    def affichage(self):
        return f"La voiture est un(e) {self.__marque} {self.__modele} de puissance {self.__puiss} et de couleur {self.__couleur}."

#       Accesseurs
    def get_marque(self):
        return self.__marque
    def get_modele(self):
        return self.__modele
    def get_puiss(self):
        return self.__puiss
    def get_couleur(self):
        return self.__couleur

#       Accesseurs en écriture
    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_puiss(self, puiss):
        self.__puiss = puiss

    def set_couleur(self, couleur):
        self.__couleur = couleur