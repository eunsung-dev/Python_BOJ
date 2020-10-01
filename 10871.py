N, X = input().split()
N = int(N)
X = int(X)
A = []
str = input()
A=str.split()
for i in range(N):
    if int(A[i]) < X:
        print(A[i], end=' ')