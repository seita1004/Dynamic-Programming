"""
八百屋にて、りんご x 個が a 円で、りんご y 個が b 円で、りんご z 個が c 円で売られています。
りんごの買い方を工夫したとき、n 個のりんごを手に入れるために必要な金額の最小値はいくらでしょうか。
なお、買い方を工夫した結果、買ったりんごが n+1 個以上になってもよいものとします。
"""

n,x,a,y,b,z,c = map(int,input().split())
packs = [[x,a],[y,b],[z,c]]

# 一度に買える最大個数
# n個を少し超える場合まで考えればよいので使う
max_pack = max(count for count,price in packs)

# n個ちょうどでなく、n個以上でもよい
# 最後の1回の購入で超える最大分だけ余裕を持たせる
limit = n + max_pack

# 十分大きい数（まだ到達していない状態を表す）
INF = 10**18

#dp[i]はi個のりんごを手に入れる金額の最小値
dp = [INF] * (limit + 1)

#０個のりんごを手に入れるための金額は０円
dp[0] = 0

for i in range(limit+1):
    for count,price in packs:
        # i-count 個まで買えていれば i個にできる
        if i >= count:
            dp[i] = min(dp[i], dp[i - count] + price)


# n個以上手に入る中で最小金額を出力
print(min(dp[n:]))

    

