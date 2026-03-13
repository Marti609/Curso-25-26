variables=input("Introduce 6 numeros separados por guiones: ")
lista=variables.split("-")

lista=[int(x) for x in lista]

valor_max=max(lista)
valor_min=min(lista)

media=sum(lista)/len(lista)
media_buena=round(media,4)

nueva_lista=[int(x) for x in lista if int(x) > media]

print(f"Valor máximo: {valor_max}")
print(f"Valor mínimo: {valor_min}")
print(f"Media: {media_buena}")
print(f"Nueva lista: {nueva_lista}")
