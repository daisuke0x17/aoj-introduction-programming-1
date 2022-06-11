'''
1 から n までの数の中から、重複無しで３つの数を選びそれらの合計が x となる組み合わせの数を求めるプログラムを作成して下さい。
'''
while True:
    n,x = map(int,input().split())
    if n==x==0:
        break

    cnt = 0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            for k in range(j+1,n+1):
                if i+j+k == x:
                    cnt += 1
    print(cnt)

