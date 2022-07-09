'''
２つのデータがどれだけ似ているかを、それらの距離で測る手法は、クラスタリングや分類など、様々なところで使われています。ここでは、２つの n 次元ベクトル x={x1,x2,...,xn} と y={y1,y2,...,yn} の距離を計算してみましょう。
'''

n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))

p1 = 0
for i in range(n):
   p1 += abs(x[i]-y[i])

p2_sum = 0
for i in range(n):
    p2_sum += (abs(x[i]-y[i]))**2
p2 = p2_sum**0.5

p3_sum = 0
for i in range(n):
    p3_sum += (abs(x[i]-y[i]))**3
p3 = p3_sum**(1/3)

p_max = 0
for i in range(n):
    if p_max < abs(x[i]-y[i]):
        p_max = abs(x[i]-y[i])

print(p1, p2, p3, p_max, sep='\n')

'''
リスト内包表記だとスマートに書けるみたいです！
# 1から3までのループ処理を行う
for p in range(1, 4):
    # zip関数でX, Yから1要素ずつa, bに取り出す → abs関数で絶対値をとりp乗 → sum関数で総数を算出 → 1/p乗する
    print("{0:.6f}".format(sum([abs(a-b)**p for a, b in zip(X, Y)])**(1/p)))
# zip関数でX, Yから1要素ずつa, bに取り出す → abs関数で絶対値をとる → max関数で最大値を求める
print("{0:.6f}".format(max([abs(a-b) for a, b in zip(X, Y)])))

参考：https://tysonblog-whitelabel.com/aizu-online-judge-itp1_10_d#link_4

'''
