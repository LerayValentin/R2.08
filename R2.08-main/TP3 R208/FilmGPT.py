class Film:
    def __init__(self, titre, date_sortie, note, liste_avis):
        self._titre = titre
        self._date_sortie = date_sortie
        self._note = note
        self._liste_avis = liste_avis

    @property
    def titre(self):
        return self._titre

    @titre.setter
    def titre(self, value):
        self._titre = value

    @property
    def date_sortie(self):
        return self._date_sortie

    @date_sortie.setter
    def date_sortie(self, value):
        self._date_sortie = value

    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, value):
        self._note = value

    @property
    def liste_avis(self):
        return self._liste_avis

    @liste_avis.setter
    def liste_avis(self, value):
        self._liste_avis = value

    def __str__(self):
        avis_str = "\n".join(["- " + avis for avis in self._liste_avis])
        return f"Le film {self._titre} est sorti le {self._date_sortie}, il a la note {self._note} et voici les avis du public l'ayant vu :\n{avis_str}"


