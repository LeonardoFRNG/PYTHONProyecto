nombre = input("Ingrese su nombre: ")
precioComida = int(input("Ingrese el precio de su comida: "))

if precioComida < 20:
    propina = precioComida * 0.10

elif precioComida >= 20 <= 50:
    propina = precioComida * 0.15
else:
    propina = precioComida * 0.20

total = precioComida + propina

print(
    f"{nombre} debe pagar de propina {int(propina)}$, y su total es de {int(total)}$\n"
)
