'''
たてH cm よこ W cm の長方形を描くプログラムを作成して下さい。
1 cm × 1cm の長方形を '#'で表します。
'''

while True:
    h,w = map(int,input().split())
    if h==0 and w==0:
        break
    for _i in range(h):
        for _j in range(w):
            print('#',end='')
        print()
    print()

'''
別解
while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    for i in range(h):
        print("#"*w)
    print()
'''

