from Film import *
from json import *

class Bibliotheque(Film):
    def __init__(self):
        self.__liste_films = []

    def ajouter_films(self, film):
        self.__liste_films.append(film)
    
    def afficher_films(self):
        for film in self.__liste_films:
            print(film)

    def mostrate(self):
        max_note = 0
        nom_film = ""
        for films in self.__liste_films:
            if films.note >= max_note:
                max_note = films.note
                nom_film = films.title
        print(f"Le film avec la plus granded note est {nom_film} avec une note de {max_note}") 

    def top3(self):
        top_films = sorted(self.__liste_films, key=lambda x: x.note, reverse=True)[:3]
        print("Top 3 des films les mieux notes :")
        for film in top_films:
            print(f"- {film.title}")
    
    def lastmovie(self):
        most_recent = sorted(self.__liste_films, key=lambda x: x.date, reverse=True)[:1]
        for film in most_recent:
            print(f"Le film le plus recent est {film.title} et es sorti le {film.date}")

    def avrgnote(self):
        sum_notes = 0
        compteur = 0
        for film in self.__liste_films:
            sum_notes += film.note
            compteur += 1
        print(f"La note moyenne des films de la bibliotheque est de {sum_notes / compteur}")
    
    def to_json_file(self, filename="films.json"):
        info_all_films = []
        for film in self.__liste_films:
            info_all_films.append(film.to_json())
        with open(filename, 'w') as file:
            dump(info_all_films, file, indent=1)
 
    def fromjson(self, filename="movies.json"):
        with open(filename, 'r') as file:
            data = load(file)
            for film_data in data["films"]:
                film = Film(film_data["titre"], film_data["date"], film_data["note"], film_data["avis"])
                self.ajouter_films(film)


#rubrique de test
if __name__ == "__main__":
    bibliotheque = Bibliotheque()
    bibliotheque.ajouter_films(Film("Gladiator", "2000-05-05", 4.5, ["Epic historical drama!", "Russell Crowe delivers a powerhouse performance!"]))
    bibliotheque.ajouter_films(Film("Inception", "2010-07-16", 4.8, ["Mind-bending masterpiece!", "Leonardo DiCaprio shines!"]))
    bibliotheque.ajouter_films(Film("The Dark Knight", "2008-07-18", 4.9, ["Heath Ledger's Joker steals the show!", "Christopher Nolan's best work!"]))

    bibliotheque.afficher_films()
    bibliotheque.mostrate()
    bibliotheque.top3()
    bibliotheque.lastmovie()
    bibliotheque.avrgnote()
    bibliotheque.to_json_file()
    bibliotheque.fromjson()
    bibliotheque.afficher_films()
    bibliotheque.mostrate()
    bibliotheque.top3()
    bibliotheque.lastmovie()
    bibliotheque.avrgnote()