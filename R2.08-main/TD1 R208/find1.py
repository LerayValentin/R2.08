import sys, os
if __name__ == '__main__':
    def start_find1():
        if len(sys.argv) != 2:
            print(f"Pas assez d’arguments pour le script {sys.argv}.")
        elif os.path.exists(sys.argv[1]):
            for elt in os.listdir(sys.argv[1]):
                print(elt)
        else:
            print("Le répertoire n'existe pas.")



start_find1()