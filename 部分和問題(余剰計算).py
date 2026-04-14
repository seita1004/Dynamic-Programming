# N: 数の個数
# K: 作りたい「1000で割った余り」
N,K = map(int,input().split())
values = [int(input()) for _ in range(N)]
mod = 1000


#dp[i][j] = 先頭からi個見たとき、いくつか選んで和を1000で割った余りをjにできるか
dp = [[False] * (mod) for _ in range(N+1)]

#何も選ばなければ和は０、余りも０
dp[0][0] = True

for i in range(N):
    a = values[i]

    # 現在作れる余りを全探索
    for j in range(mod):
        #余りｊを実際に作れる時だけ遷移する
        if dp[i][j]:
            # a を選ばない場合
            # 余り j はそのまま作れる
            dp[i+1][j] = True

            # a を選ぶ場合
            # 新しい余りは (j + a) % 1000
            dp[i+1][(j+a) % mod] = True

#N個の数を見たとき、1000で割った余りがKとなるようにできるかどうか
if dp[N][K] == True:
    print("Yes")
else:
    print("No")