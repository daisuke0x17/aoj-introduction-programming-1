'''
以下のような、たてH cm よこ W cm の枠を描くプログラムを作成して下さい。
'''

while True:
    h,w = map(int,input().split())
    if h==0 and w==0:
        break
    for i in range(h):
        for k in range(w):
            if i==0 or i==(h-1):
                print("#",end="")
            elif k==0 or k==(w-1):
                print("#",end="")
            else:
                print(".",end="")
        print()
    print()
