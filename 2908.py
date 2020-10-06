A, B = input().split()
A = list(map(int,list(A)))
B = list(map(int,list(B)))
A.reverse()
B.reverse()
A_int = A[0]*100 + A[1]*10 + A[2]
B_int = B[0]*100 + B[1]*10 + B[2]
if A_int > B_int:
    print(A_int)
else:
    print(B_int)