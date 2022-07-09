'''
三角形の２辺 a, b とその間の角 C から、その三角形の面積 S、周の長さ L, a を底辺としたときの高さ h を求めるプログラムを作成して下さい。
'''
import math

a,b,c = map(int,input().split())

S = a*b*math.sin(math.radians(c))/2
L = a+b+(math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(c))))
h = 2*S/a
print(S)
print(L)
print(h)

'''
参考
print(S, L, h, sep="\n")
でまとめて出力できる
'''
