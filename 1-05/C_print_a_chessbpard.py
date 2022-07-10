'''
以下のような、たてH cm よこ W cm のチェック柄の長方形を描くプログラムを作成して下さい。

#.#.#.#.#.
.#.#.#.#.#
#.#.#.#.#.
.#.#.#.#.#
#.#.#.#.#.
.#.#.#.#.#
'''

while True:
    h,w = map(int,input().split())
    if h==0 and w==0:
        break
    for i in range(h):
        for k in range(w):
            if (i+k)%2==0:
                print("#",end="")
            else:
                print(".",end="")
        print()
    print()
