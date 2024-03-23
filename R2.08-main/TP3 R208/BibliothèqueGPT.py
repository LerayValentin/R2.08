from FilmGPT import *

class Bibliothèque:
    def __init__(self):
        self._films = []

    def ajouter_film(self, film):
        self._films.append(film)

    def afficher_films(self):
        for film in self._films:
            print(film)

    def mostrate(self):
        max_note = max([film.note for film in self._films])
        max_films = [film for film in self._films if film.note == max_note]
        for film in max_films:
            print(f"Le film avec la note la plus élevée est : {film.titre} avec une note de {film.note}")

    def top3(self):
        top_films = sorted(self._films, key=lambda x: x.note, reverse=True)[:3]
        print("Top 3 des films les mieux notés :")
        for film in top_films:
            print(film.titre)

    def lastmovie(self):
        sorted_films = sorted(self._films, key=lambda x: x.date_sortie, reverse=True)
        print(f"Le film le plus récent est : {sorted_films[0].titre}")

    def avrgnote(self):
        total_note = sum([film.note for film in self._films])
        avrg_note = total_note / len(self._films)
        print(f"La note moyenne des films dans la bibliothèque est de : {avrg_note}")


# Test de l'implémentation
if __name__ == "__main__":
    bibliotheque = Bibliothèque()

    # Ajout de quelques films à la bibliothèque
    bibliotheque.ajouter_film(Film("Gladiator", "2000-05-05", 4.5, ["Epic historical drama!", "Russell Crowe delivers a powerhouse performance!"]))
    bibliotheque.ajouter_film(Film("Inception", "2010-07-16", 4.8, ["Mind-bending masterpiece!", "Leonardo DiCaprio shines!"]))
    bibliotheque.ajouter_film(Film("The Dark Knight", "2008-07-18", 4.9, ["Heath Ledger's Joker steals the show!", "Christopher Nolan's best work!"]))

    # Affichage des films dans la bibliothèque
    bibliotheque.afficher_films()

    # Trouver le film avec la note la plus élevée
    bibliotheque.mostrate()

    # Afficher le top 3 des films les mieux notés
    bibliotheque.top3()

    # Trouver le film le plus récent
    bibliotheque.lastmovie()

    # Calculer la note moyenne des films dans la bibliothèque
    bibliotheque.avrgnote()
