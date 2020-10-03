A = input()
A = int(A)
B = input()
B = int(B)
C = input()
C = int(C)
multi = A * B * C
length = len(str(multi))
Array = []
for i in range(length):
    Array.append(multi // (10**(length-i-1)))
    multi = multi % (10**(length-i-1))
# print(Array)
for i in range(10):
    print(Array.count(i))