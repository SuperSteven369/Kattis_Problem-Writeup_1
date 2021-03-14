MAXINT = 10005
num_cases = int(input())
for i in range(num_cases):
    # number of face values
    K = int(input())
    # face values
    fv = [int(ele) for ele in input().split(' ')]
    fv.insert(0, 0)
    fv.sort()
    dp = [0] * MAXINT
    dp[0] = 1
    res = K
    for j in range(1, K + 1):
        curr = fv[j]
        if dp[curr]:
            res -= 1
            continue
        for k in range(curr, fv[K] + 1):
            dp[k] = dp[k] or dp[k - curr]
    print(res)
