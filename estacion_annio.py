mes = int (input("Ingrese un Mes (Número): "))
match mes :
    case 12 | 1 | 2:
        estacion = "Invierno"
        print ("MES: ", mes,)
        print ("ESTACION: ", estacion)
    case 3 | 4 | 5 :
        estacion = "Primavera"
        print ("MES: ", mes,)
        print ("ESTACION: ", estacion)
    case 6 | 7 | 8: 
        estacion = "Verano"
        print ("MES: ", mes,)
        print ("ESTACION: ", estacion)
    case 9 | 10 | 11 :
        estacion = "Otoño"
        print ("MES: ", mes,)
        print ("ESTACION: ", estacion)