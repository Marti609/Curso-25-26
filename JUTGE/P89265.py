a1, b1, a2, b2 = map(int, input().split())

if a1 == a2 and b1 == b2:
    rel = "="
elif a2 <= a1 and b1 <= b2:
    rel = "1"
elif a1 <= a2 and b2 <= b1:
    rel = "2"
else:
    rel = "?"

x = max(a1, a2)
y = min(b1, b2)
if x > y:
    inter = "[]"
else:
    inter = f"[{x},{y}]"

print(f"{rel} , {inter}")
