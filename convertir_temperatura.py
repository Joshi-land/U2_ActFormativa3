temp = float(input("Ingrese Temperatura (Celsius): "))
print (""" 
------------------
<<<< OPCIONES >>>>
1.- Fahrenheit
2.- Kelvin
------------------""")
opc = int (input("Seleccione una Opción: "))
match opc :
    case 1:
        resultado = temp * 9/5 +32
        unidad = "F"
        print (" - Temperatura dada: ", temp)
        print (" - Equivalencia: ", resultado, unidad)
    case 2:
        resultado = temp + 273.15
        unidad = "K"
        print (" - Temperatura dada: ", temp)
        print (" - Equivalencia: ", resultado, unidad)
    case _:
        print("--- ERROR ---")
       
    