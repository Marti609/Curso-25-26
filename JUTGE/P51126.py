a1, b1, a2, b2 = map(int, input().split())

x = max(a1, a2)
y = min(b1, b2)

if x > y:
    print("[]")
else:
    print("[{},{}]".format(x, y))
