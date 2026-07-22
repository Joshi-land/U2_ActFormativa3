consulta = input("Ingrese nombre de artista, canción,película o serie:  ")
match consulta:
    case "linkin park" :
        info = "Linkin Park es una banda estadounidense de rock"
        print("Consulta: ",consulta)
        print("Información: ", info)
    case "TV Girl":
        info = "TV Girl es una banda estadounidense de indie pop de San Diego, California, formada por Brad Petering, Jason Wyman y Wyatt Harmon"
        print("Consulta: ",consulta)
        print("Información: ", info)

    case "superman 2025":
        info = "Superman es una película estadounidense de superhéroes de 2025 basada en el personaje homónimo de DC Comics. Escrita y dirigida por James Gunn"
        print("Consulta: ",consulta)
        print("Información: ", info)

    case "the mentalist":
        info = "El Mentalista fue una serie de televisión estadounidense de género policíaco protagonizada por Simon Baker en el papel de Patrick Jane"
        print("Consulta: ",consulta)
        print("Información: ", info)

    case "the craving":
        info = "Canción de Twenty One pilots del álbum Clancy lanzado en 2024"
        print("Consulta: ",consulta)
        print("Información: ", info)

    case _:
        info = "Información no disponible"
        print("Consulta: ",consulta)
        print("Información: ", info)