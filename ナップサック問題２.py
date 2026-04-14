#重さが非常の大きい場合のナップサック問題
#価値の合計を基準にして、動的計画法で解く

# N: 品物の個数
# W: 許容できる重さの上限
N, W = map(int, input().split())

items = []
total_value = 0 #最大でどこまで価値があり得るか

#品物の入力
for _ in range(N):
    w,v = map(int,input().split())
    items.append((w,v))
    total_value += v

INF = 10**18 #十分な大きさの値

# dp[i][j]:
# 前から i 個の品物を見たとき、
# 「価値の合計を j にするための最小重さ」
#重さがINFのときは、価値をｊにすることができないことを意味する
dp = [[INF] * (total_value + 1) for _ in range(N+1)]

dp[0][0] = 0 #価値の合計が0のとき、重さは0

for i in range(N):
    w,v = items[i]

    for j in range(total_value + 1):
        #i番目の品物を選ばない場合
        dp[i+1][j] = dp[i][j]

        #i番目の品物を選ぶ場合
        if j >= v:
            dp[i+1][j] = min(dp[i+1][j],dp[i][j-v] + w)

#重さW以下で達成できる最大価値を探す
answer = 0
for j in range(total_value + 1):
    if dp[N][j] <= W:
        answer = j

print(answer)