str = input()
str = str.replace('c=','.')
str = str.replace('c-','.')
str = str.replace('dz=','.')
str = str.replace('d-','.')
str = str.replace('lj','.')
str = str.replace('nj','.')
str = str.replace('s=','.')
str = str.replace('z=','.')
print(len(str))

# str = list(input())
# i, cnt, tmp = 0, 0, 0
# if len(str) > 100:
#     exit()
# if len(str) == 1:
#     print("1")
# while i < len(str):
#     if i != (len(str)-1):
#         if str[i] == 'c':
#             if (str[i+1] == '=') | (str[i+1] == '-'):
#                 i += 1
#         elif (str[i] == 'l') & (str[i+1] == 'j'):
#             i += 1
#         elif (str[i] == 'n') & (str[i+1] == 'j'):
#             i += 1
#         elif (str[i] == 's') & (str[i+1] == '='):
#             i += 1
#         elif (str[i] == 'z') & (str[i+1] == '='):
#             i += 1
#         elif (str[i] == 'd') & (str[i+1] == '-'):
#             i += 1
#     if (i < (len(str)-2)) & (len(str) > 2):
#         if (str[i] == 'd') & (str[i+1] == 'z') & (str[i+2] == '='):
#             i += 2

#     cnt += 1
#     i += 1
# print(cnt)