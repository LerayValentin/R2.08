import sys, os
listeFichiers = []
listeDossiers = []
dossier = sys.argv[1] + "\\"
if __name__ == '__main__':
    def start_find2():
        if len(sys.argv) != 2:
            print(f"Pas assez d’arguments pour le script {sys.argv}.")
        recherche()
        print(listeDossiers, "\n", listeFichiers)

    def recherche():
        if os.path.exists(sys.argv[1]):
            for elt in os.listdir(sys.argv[1]):
                if os.path.isdir(dossier + elt):
                    listeDossiers.append(dossier + elt)
                elif os.path.isfile(dossier + elt):
                    listeFichiers.append(dossier + elt)
        else:
            print("Le répertoire n'existe pas.")



start_find2()