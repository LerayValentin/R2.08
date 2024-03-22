if __name__ == '__main__':
    fichier = open("txt.txt", "r")

    for lines in fichier:
        fichier.close()
        fichier = open("txt.txt", "w")
        lines = lines.rstrip("\r\n")
        print(lines)
