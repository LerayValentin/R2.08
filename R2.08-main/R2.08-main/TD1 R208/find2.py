import sys, os
listeFichiers = []
listeDossiers = []
chemin = sys.argv[1] + "\\"
if __name__ == '__main__':

    def recherche(dossier):
        if os.path.exists(sys.argv[1]):
            for elt in os.listdir(dossier):
                if os.path.isdir(dossier + elt):
                    listeDossiers.append(dossier + elt)
                elif os.path.isfile(dossier + elt):
                    listeFichiers.append(dossier + elt)
        else:
            print("Le répertoire n'existe pas.")

    def start_find2(arg1):
        if len(sys.argv) != 2:
            print(f"Pas assez d’arguments pour le script {sys.argv}.")
        recherche(arg1)


        print(" \n Dossier(s) : ")
        for dossier in listeDossiers:
            print(dossier)
        print("\n Fichier(s) : ")
        for fichier in listeFichiers:
            print(fichier)


start_find2(chemin)
