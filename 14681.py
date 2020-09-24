X = input()
Y = input()
X = int(X)
Y = int(Y)
if (X>0) & (Y>0):
    print(1)
elif (X>0) & (Y<0):
    print(4)
elif (X<0) & (Y>0):
    print(2)
elif (X<0) & (Y<0):
    print(3)