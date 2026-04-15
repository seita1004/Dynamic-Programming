#a_1, a_2, ..., a_N から M 個以下の整数を選んでその和を K とすることはできるか
N,M,K = map(int,input().split())

a_list = [int(input()) for _ in range(N)]

INF = 10**9

#dp[i][j] = 先頭からi個見て、和jを作るのに必要な最小個数
dp = [[INF] * (K+1) for _ in range(N+1)]

dp[0][0] = 0 #0は0個の整数で作れる    

for i in range(N):
    a = a_list[i]
    for j in range(K+1):
        if dp[i][j] == INF:
            continue

        #aを選ばない
        dp[i+1][j] = min(dp[i+1][j],dp[i][j])

        #aを選ぶ
        if j + a <= K:
            #min(今まで見つかった最良, 新候補)
            dp[i+1][j + a] = min(dp[i+1][j+a], dp[i][j] + 1)

if dp[N][K] <= M:
    print("Yes")
else:
    print("No")



