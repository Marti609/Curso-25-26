variable=input("introduce valores: ")
lista=variable.split(",")                       

lista=[int(x) for x in lista]
print(lista)

valormax=max(lista)
valormin=min(lista)

lista.remove(valormax)
lista.remove(valormin)

print(lista)

suma_numeros=sum(lista)
media_numeros=suma_numeros/len(lista)
media_numeros=round(media_numeros,2)

print(f"la media de los numeros es: {media_numeros}")

if media_numeros>10:
    print("Rendimiento alto")
elif media_numeros<5:
    print("Rendimiento bajo")
else:
    print("Rendimiento medio")