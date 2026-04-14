#Nは品物の個数、重さの総和はW以下でなければいけない
N,W = map(int,input().split())

items = []

for _ in range(N):
    #wは重さ、vは価値
    w,v = map(int,input().split())
    #(重さ、価値) 「変更しないペアのデータ」だからタプルにしている
    items.append((w,v))

# dp[i][j]:
# 前からi個の品物を見たとき、重さj以下で得られる最大価値
#品物はN個だが、i = 0、つまり「まだ何も見ていない状態」が必要なのでN+1
dp = [[0] *(W+1) for _ in range(N+1) ]

for i in range(N):
    w,v = items[i]
    for j in range(W+1):
        #i番目の品物を選ばない場合
        dp[i+1][j] = dp[i][j]

        if j >= w:
            dp[i+1][j] = max(dp[i+1][j],dp[i+1][j-w] + v)

print(dp[N][W])




