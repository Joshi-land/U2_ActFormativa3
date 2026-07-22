precio_orig = int (input("Ingrese el precio del producto: $ "))
if precio_orig <= 100:
    descuento = 0
elif precio_orig <=200:
    descuento = 0.10
elif precio_orig <= 500:
    descuento = 0.20
elif precio_orig > 500:
    descuento = 0.25

precio_final = precio_orig - (precio_orig * descuento)    

print("Descuento: ", descuento*100, "%")
print("Precio Original: $",precio_orig)
print("Precio con Descuento: $", precio_final)
