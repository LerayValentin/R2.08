import sys
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(f"Pas assez d’arguments pour le script {sys.argv}")
    else:
       for i in range(len(sys.argv)):
           print(sys.argv[i])
       for elt in sys.argv:
           print(elt)
