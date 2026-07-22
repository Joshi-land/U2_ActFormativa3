parciales = float(input("Ingrese Calificación Parcial: "))
proyecto = float(input("Ingrese Calificación de Proyecto: "))
examfinal = float(input("Ingrese Calificación de Examen Final: "))

if (parciales < 0 or parciales > 100) or (proyecto < 0 or proyecto > 100) or (examfinal < 0 or examfinal > 100):
    print ("<<ERROR DATOS INVALIDOS>>")
else:
    calif_final = (parciales*0.40)+(proyecto*0.30)+(examfinal*0.30)
    print("Calificación Final: ", calif_final)
    print("Calificación de Parciales: ", parciales)
    print ("Calificación de Proyecto: ", proyecto)
    print ("Calificación de Examen Final: ", calif_final)