cantidad = float(input("Ingrese cantidad de dinero (MXN): "))
print ("""Cambio a:
1.- Dólar USD
2.- Euro EUR 
3.- Bath THB 
4.- Yen JPY 
5.- Won KRW
6.- Dólar Australiano AUD
7.- Sol PEN
8.- Dólar Canadiense CAD
9.- Bolívar VES
10.- Peso Argentino ARS
""")
opc = int(input("Ingrese opción: "))
match opc:
    case 1:
        cambio = cantidad /16.5
        moneda = "USD"
        print ("Cambio realizado")
        print ("$", cantidad, "MXN  ->  $", cambio,moneda)
    case 2:
        cambio = cantidad /18.0
        moneda = "EUR"
        print ("Cambio realizado")
        print ("$", cantidad, "MXN  ->  $", cambio,moneda)
    case 3:
        cambio = cantidad /0.45
        moneda = "THB"
        print ("Cambio realizado")
        print ("$", cantidad, "MXN  ->  $", cambio,moneda)
    case 4:
        cambio = cantidad /0.12
        moneda = "JPY"
        print ("Cambio realizado")
        print ("$", cantidad, "MXN  ->  $", cambio,moneda)
    case 5:
        cambio = cantidad /0.013
        moneda = "KRW"
        print ("Cambio realizado")
        print ("$", cantidad, "MXN  ->  $", cambio,moneda)
    case 6:
        cambio = cantidad /11.5
        moneda = "AUD"
        print ("Cambio realizado")
        print ("$", cantidad, "MXN  ->  $", cambio,moneda)
    case 7:
        cambio = cantidad /2.8
        moneda = "PEN"
        print ("Cambio realizado")
        print ("$", cantidad, "MXN  ->  $", cambio,moneda)
    case 8:
        cambio = cantidad /8.2
        moneda = "CAD"
        print ("Cambio realizado")
        print ("$", cantidad, "MXN  ->  $", cambio,moneda)
    case 9:
        cambio = cantidad /0.0023
        moneda = "VES"
        print ("Cambio realizado")
        print ("$", cantidad, "MXN  ->  $", cambio,moneda)
    case 10:
        cambio = cantidad /0.046
        moneda = "ARS"
        print ("Cambio realizado")
        print ("$", cantidad, "MXN  ->  $", cambio,moneda)
    case _ :
        print("Opción inválida")
        resultado = none

    