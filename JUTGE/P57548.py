num=input("")
lista=num.split()

if len(num)==1:
    num2=input("")
    print(int(num)+int(num2))
else:
    print(int(lista[0])+int(lista[1]))
