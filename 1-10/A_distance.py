'''
２点 P1(x1, y1), P2(x2, y2) の距離を求めるプログラムを作成せよ。
'''
import math

x1,y1,x2,y2 = map(float,input().split())
distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print(distance)
