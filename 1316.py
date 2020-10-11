N = int(input())
array = list(0 for i in range(N))
sum = 0
for i in range(N):
    array[i] = list(input())
    if len(array[i]) == 1:
        sum += 1
    else:
        cnt = 0
        for j in array[i]:
            temp = [i for i, value in enumerate(array[i]) if value == j]
            if (len(temp) > 1):
                for x in range(len(temp)-1):
                    if ((temp[x+1] - temp[x]) != 1):
                        cnt += 1
                        break
        if cnt == 0:
            sum += 1
print(sum)