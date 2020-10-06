str = input()
try:
    print(ord(str))
except:
    str = int(str)
    print(chr(str))