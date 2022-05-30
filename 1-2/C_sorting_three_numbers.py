'''
３つの整数を読み込み、それらを値が小さい順に並べて出力するプログラムを作成して下さい。
'''

a,b,c = [int(x) for x in input().split()]

if a<b<c:
    print(a,b,c)
elif a<c and c<b:
    print(a,c,b)
elif b<a and a<c:
    print(b,a,c)
elif c<a and a<b:
    print(c,a,b)
elif b<c and c<a:
    print(b,c,a)
elif c<b and b<a:
    print(c,b,a)
else:
    pass


'''
別解
num_list = list(map(int,input().split()))
num_list.sort()
print(*num_list)
'''
