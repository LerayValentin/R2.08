class Film():
    def __init__(self, title, date, note, liste_avis):
        self.__title = title
        self.__date = date
        self.__note = note
        self.__liste_avis = liste_avis
    
    def __str__(self):
        avis_str = "\n".join(["- " + avis for avis in self.__liste_avis])
        return f"Le film {self.__title} est sorti le {self.__date}, il a la note {self.__note} et voici les avis du public l'ayant vu :\n{avis_str}"
    
#property title
    def get_title(self):
        return self.__title
    def set_title(self, title):
        self.__title = title
        return self.__title
    title = property(fget=get_title, fset=set_title)
#property date
    def get_date(self):
        return self.__date
    def set_date(self, date):
        self.__date = date
        return self.__date
    date = property(fget=get_date, fset=set_date)
#property note
    def get_note(self):
        return self.__note
    def set_note(self, note):
        self.__note = note
        return self.__note
    note = property(fget=get_note, fset=set_note)
#property liste_avis
    def get_liste_avis(self):
        return self.__liste_avis
    def set_liste_avis(self, liste_avis):
        self.__liste_avis = liste_avis
        return self.__liste_avis
    liste_avis = property(fget=get_liste_avis, fset=set_liste_avis)




#rubrique de test
if __name__ == "__main__":
    film1 = Film("Nom du film", "10-10-2020", 4, ["Mind-bending masterpiece!", "Leonardo DiCaprio shines!"])
    print(film1)
    film1.title = "Gladiator"
    film1.date = "2000-05-05"
    film1.note = "4.5"
    film1.liste_avis = ["Epic historical drama!", "Russell Crowe delivers a powerhouse performance!"]
    print(film1)
    
    