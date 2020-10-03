C = int(input())
for a in range(C):
    studentScore = input().split()
    sum, avg, cnt = 0, 0.0, 0
    for b in range(int(studentScore[0])+1):
        studentScore[b] = int(studentScore[b])
    studentNumber = studentScore[0]
    del(studentScore[0])
    for c in studentScore:
        sum += c
    avg = float(sum) / float(studentNumber)
    if sum == 0:
        print("0.000%")
    else:
        for d in studentScore:
            if d > avg:
                cnt += 1
        print('{:.3f}%'.format((cnt/studentNumber)*100))
    # round와 format은 다름 round는 소수점이 0이면 원하는 형식과 다르게 출력