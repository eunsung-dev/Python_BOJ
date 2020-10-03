N = int(input())
for i in range(N):
    str = list(input())
    score = 0
    add = 1
    for j in range(len(str)):
        if str[j] == "O":
            score += add
            add += 1
        else:
            add = 1
    print(score)