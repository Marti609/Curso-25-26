a1, b1, a2, b2 = map(int, input().split())

if a1 == a2 and b1 == b2:
    print("=")
elif a2 <= a1 and b1 <= b2:
    print("1")
elif a1 <= a2 and b2 <= b1:
    print("2")
else:
    print("?")
