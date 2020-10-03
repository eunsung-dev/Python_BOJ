M = 0
sum = 0
N = int(input())
Array = input().split()
for i in range(N):
    Array[i] = int(Array[i])
    if M < Array[i]:
        M = Array[i]
for i in range(N):
    Array[i] = (Array[i]/M)*100
    sum += Array[i]
print(sum/N)