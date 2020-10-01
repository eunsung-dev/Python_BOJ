T = input()
T = int(T)
sum = []
for i in range(T):
    A, B = input().split()
    A = int(A)
    B = int(B)
    sum.append(A+B)
for i in range(T):
    print("Case #"+str(i+1)+":",sum[i])