from Voiture import *

mycar1 = Voiture1()
mycar2 = Voiture2("BMW", "S2", "400", "noir")
mycar3 = Voiture3()
mycar4 = Voiture4("Chevrolet", "Camaro", "450")

print(mycar1.affichage())
print(mycar2.affichage())
print(mycar3.affichage())
print(mycar4.affichage())

print(mycar1.get_marque())
mycar1.set_marque("BMW")
print(mycar1.get_marque())

print(mycar1)
mycar1.ajouter_option("Pack M")
print(mycar1)
mycar1.ajouter_option("Turbo")
print(mycar1)
mycar1.supprimer_option("Pack M")
print(mycar1)
mycar1.is_option_present("Pack M")
mycar1.is_option_present("Turbo")
