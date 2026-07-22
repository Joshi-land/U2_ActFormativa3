calif = float(input("Ingrese una calificación: "))
if calif >= 90:
    letra ="A"
elif calif >= 80:
    letra ="B"
elif calif >= 70:
    letra = "C"
elif calif >= 60:
    letra = "D"
else:
    letra = "F"

print ("Calificación Ingresada: ", calif)
print ("Clasificación correspondiente: ", letra)


