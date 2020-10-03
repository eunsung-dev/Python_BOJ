Array = []
for i in range(10):
    Array.append(int(input()) % 42)
for i in Array:
    if Array.count(i) != 1:
        Array.remove(i)
print(len(Array))