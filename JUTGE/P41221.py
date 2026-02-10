numbers=input().split()
while len(numbers)<3:
    numbers2=input().split()
    if numbers2:
        numbers.append(numbers2[0])
total=0
for num in numbers:
    total+=int(num)
print(total)