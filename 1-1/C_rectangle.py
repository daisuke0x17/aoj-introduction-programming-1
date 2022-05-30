'''
たて a cm よこ b cm の長方形の面積と周の長さを求めるプログラムを作成して下さい。
'''

a,b = map(int,input().split())
print(a*b,2*a+2*b)

'''
別解
input = input()
a,b = [int(x) for x in input.split()]
print(a * b, a * 2 + b * 2)
'''
