import sys
T = sys.stdin.readline().rstrip()
T = int(T)
sum = []
for i in range(T):
    A, B = sys.stdin.readline().rstrip().split()
    A = int(A)
    B = int(B)
    sum.append(A+B)
for i in range(T):
    print(sum[i])