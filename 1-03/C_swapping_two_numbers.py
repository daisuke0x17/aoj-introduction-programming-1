'''
２つの整数 x, y を読み込み、それらを値が小さい順に出力するプログラムを作成して下さい。
ただし、この問題は以下に示すようにいくつかのデータセットが与えられることに注意して下さい。
'''

while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    elif x < y:
        print(x, y)
    else:
        print(y, x)
