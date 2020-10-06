import operator
str = input().upper()
if len(str) == 1:
    print(str)
    exit()
dic = {}
for i in set(str):
    dic[i] = 0
for i in str:
    dic[i] += 1
dic = sorted(dic.items(),reverse = True, key=operator.itemgetter(1))
if dic[0][1] == dic[1][1]:
    print("?")
else:
    print(dic[0][0])
# import sys
# array = sys.stdin.readline()
# array = list(array.upper())
# del array[len(array)-1]
# max, tmp, check = 0, 0, 0
# for i in range(len(array)):
#     value = array.count(array[i])
#     if value > max:
#         max = value
#         tmp = i
#         check = 0
#     elif (value == max) & (array[tmp] != array[i]):
#         check = 1
# if check:
#     print("?")
# else:
#     print(array[tmp])