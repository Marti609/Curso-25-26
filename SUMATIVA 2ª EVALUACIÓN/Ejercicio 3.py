valores=input("Introduce valores en una linea separados por guiones: ")
lista=valores.split("-")
valores_numericos=[]
valores_no_numericos=[]

for i in lista:
    if i.isnumeric():
        valores_numericos.append(i)
    else:
        valores_no_numericos.append(i)
suma_con_duplicados=sum([int(x) for x in valores_numericos])

print(f"Suma total de los valores numericos con duplicados: {suma_con_duplicados}") 
print(f"Valores numericos antes de eliminar duplicados: {valores_numericos}")

valores_sin_duplicados=list(set(valores_numericos))
suma_sin_duplicados=sum([int(x) for x in valores_sin_duplicados])

print(f"Valores numericos despues de eliminar duplicados: {valores_sin_duplicados}")
print(f"Suma total de los valores numericos: {suma_sin_duplicados}")





print(f"Valores no numericos: {valores_no_numericos}")


