'''
表計算を行う簡単なプログラムを作成します。
表の行数rと列数c、r × c の要素を持つ表を読み込んで、各行と列の合計を挿入した新しい表を出力するプログラムを作成して下さい。
'''

r,c = map(int,input().split())

table_lst = [list(map(int,input().split()))for _ in range(r)]

for i in range(r):
    table_lst[i].append(sum(table_lst[i]))

sum_column = [0]*(c+1)
for i in range(c+1):
    for j in range(r):
        sum_column[i] += table_lst[j][i]

for i in range(r):
    print(*table_lst[i])
print(*sum_column)
