'''
３つの整数 a、b、c を読み込み、a から b までの整数の中に、c の約数がいくつあるかを求めるプログラムを作成してください。
'''

a,b,c = map(int,input().split())

cnt = 0
while a <= b:
    if c%a==0:
        cnt+=1
    a+=1
print(cnt)

'''
別解
a,b,c = map(int,input().split())

cnt = 0
for i in range(a,b+1):
    if c%i==0:
        cnt+=1
print(cnt)
'''
