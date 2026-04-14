N,K = map(int,input().split())

values = []

for _ in range(N):
    a = int(input())
    values.append(a)

#dp[i][j] = i番目までの数を使って、和jを作れるかどうか
#作れるときはTrue、作れないときはFalse
dp = [[False] * (K+1) for _ in range(N+1)]

dp[0][0] = True     #和０はどの数も使わないことで作れる

for i in range(N):
    a = values[i]
    for j in range(K+1):
        #前までに和jを作れているため、今回の数を使わなくてもそのまま作れる
        dp[i+1][j] = dp[i][j]

        #今回の数を使う場合、前までに和j-aを作れている必要がある
        #どちらかがTrueならば、和jを作れる
        if j >= a:
            dp[i+1][j] = dp[i+1][j] or dp[i][j-a]

    
if dp[N][K] == True:
    print("Yes")
else:
    print("No")

