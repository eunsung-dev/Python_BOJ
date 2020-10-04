number1 = [i for i in range(1,10001)]
number2 = []
def d(n):
    array = list(map(int,list(str(n))))
    sum = 0
    for i in array:
        sum += i
    number2.append(n + sum)
for i in range(1,10001):
    d(i)
temp = [x for x in number1 if x not in number2]
for i in temp:
    print(i)