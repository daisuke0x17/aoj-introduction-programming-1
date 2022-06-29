'''
太郎と花子がカードゲームをする。二人はそれぞれn枚のカードを持っており、nターンの勝負を行う。各ターンではそれぞれ１枚ずつカードを出す。カードにはアルファベットからなる動物の名前が書かれており、辞書順で大きいものがそのターンの勝者となる。勝者には３ポイント、引き分けの場合にはそれぞれ１ポイントが加算される。
'''

n = int(input())
t_cnt = 0
h_cnt = 0

for _ in range(n):
    tarou, hanako = input().split()
    if tarou > hanako:
        t_cnt += 3
    if tarou < hanako:
        h_cnt += 3
    elif tarou == hanako:
        t_cnt += 1
        h_cnt += 1
    else:
        pass

print(t_cnt,h_cnt)

