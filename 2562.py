Array = [0 for i in range(9)]
Max = 0
place = 0
for i in range(9):
    Array[i] = input()
    Array[i] = int(Array[i])
    if Array[i] > Max:
        Max = Array[i]
        place = i
Array.sort()
print(Array[8])
print(place+1)