S = list(input())
alphabet = [x for x in range(97,123)]
for i in alphabet:
    if chr(i) in S:
        print(S.index(chr(i)))
    else:
        print(-1)