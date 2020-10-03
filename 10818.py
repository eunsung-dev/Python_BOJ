N = input()
N = int(N)
Array = input().split()
for i in range(N):
    Array[i] = int(Array[i])
if (len(Array) == N):
    # for i in Array:
    #     print(i, end=" ")
    Array.sort()
    print(Array[0], Array[N-1])
else:
    exit