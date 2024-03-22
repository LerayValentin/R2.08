class Film:
    def __init__(self, title, date, note, liste_avis):
        self.__title = title
        self.__date = date
        self.__note = note
        self.__liste_avis = liste_avis
    def __str__(self):
        return f"Le film {self.__title} est sorti le {self.__date}, il a une note de {self.__note}, et voici les avis du public l'ayant vu : \n\t{self.__liste_avis}"
    @property
    def title(self):
        print(self.__title)
    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def date(self):
        print(self.__date)
    @date.setter
    def title(self, date):
        self.__date = date

    @property
    def note(self):
        print(self.__note)
    @note.setter
    def title(self, note):
        self.__note = note

    @property
    def liste_avis(self):
        print(self.__liste_avis)
    @liste_avis.setter
    def title(self, liste_avis):
        self.__liste_avis = liste_avis

class Bibliotheque:
    def __init__(self, liste_films):
        self.__liste_films = liste_films
