'''
２つの整数 a と b を読み込んで、以下の値を計算するプログラムを作成して下さい
'''
a,b = map(int,input().split())

print(f'{a//b} {a%b} {a/b:.5f}')
