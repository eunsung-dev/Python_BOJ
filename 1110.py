N = input()
N = int(N)
tmp = N
cnt = 0
while True:
    if tmp >= 10 :
        A = tmp // 10
    else:
        A = 0
    B = tmp % 10
    C = A + B
    if C >= 10:
        tmp = (B * 10) + (C % 10) # 새로운 수 tmp
    else:
        tmp = (B * 10) + C # 새로운 수 tmp
    cnt +=1
    if N == tmp:
        print(cnt)
        break