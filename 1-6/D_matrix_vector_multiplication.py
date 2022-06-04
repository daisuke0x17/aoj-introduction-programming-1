'''
n×m  の行列 A と、m×1 の列ベクトルb を読み込み、A と b の積を出力するプログラムを作成してください。
'''

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [int(input()) for _ in range(m)]

for i in range(n):
    sum = 0
    for k in range(m):
        sum += a[i][k] * b[k]
    print(sum)

'''
自分で書いたコードがかなり汚かったので
https://tysonblog-whitelabel.com/aizu-online-judge-itp1_6_d
こちらを参考にしました．
すごくきれい．．．すごい！！！
'''
