T = int(input())
for i in range(T):
    P = []
    R, S = input().split()
    R = int(R)
    S = list(S)
    for x in range(len(S)):
        for y in range(R):
            P.append(S[x])
    for x in P:
        print(x, end="")
    print()