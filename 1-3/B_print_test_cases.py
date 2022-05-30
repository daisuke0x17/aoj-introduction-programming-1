'''
１つの整数 x を読み込み、それをそのまま出力するプログラムを作成して下さい。
ただし、この問題は以下に示すようにいくつかのデータセットが与えられることに注意して下さい。
'''

num_lst = []

while True:
    x = int(input())
    if x == 0:
        break
    else:
        num_lst.append(x)

for i,num in enumerate(num_lst):
    print(f'Case {i+1}: {num}')
