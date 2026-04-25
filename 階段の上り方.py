"""
整数 n, a, b, c が与えられます。
階段を上るのに、1歩で a 段または b 段または c 段を上ることができるとき、
n 段の階段を上る方法は何通りあるでしょうか。
"""

n,a,b,c, = map(int,input().split())

def count_ways_forward(n,a,b,c):
    steps = [a,b,c]

    #dp[i]はi段目に到達する方法数
    dp = [0] * (n+1)

    #0段目に達する方法は一通り
    dp[0] = 1

    for i in range(n+1):
        for s in steps:
            if i + s <= n:
                dp[i+s] += dp[i]    #i段まで来る方法数を、i+a段、i+b段、i+c段へ配る

    print(dp[n])


def count_ways_backward(n,a,b,c):
    # dp[i] = i段目に到達する方法数
    dp = [0] * (n+1)

    # 0段目にいる方法は「何もしない」の1通り
    dp[0] = 1

    for i in range(1,n+1):

        # 最後の1歩がa段だった場合
        # その直前は i-a 段にいたはず
        if i >= a:
            dp[i] += dp[i-a]
        
        # 最後の1歩がb段だった場合
        if i >= b:
            dp[i] += dp[i-b]

        # 最後の1歩がc段だった場合
        if i >= c:
            dp[i] += dp[i-c]

    print(dp[n])







