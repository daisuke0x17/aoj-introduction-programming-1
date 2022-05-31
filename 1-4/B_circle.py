'''
半径 r の円の面積と円周の長さを求めるプログラムを作成して下さい。
'''
from math import pi
r = float(input())

print(f'{pi*(r**2):.6f} {2*pi*r:.6f}')
