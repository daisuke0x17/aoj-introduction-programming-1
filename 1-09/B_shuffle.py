'''
１つのアルファベットが描かれた n 枚のカードの山をシャッフルします。
1回のシャッフルでは、下から h 枚のカードをまとめて取り出し、それを残ったカードの山の上に積み上げます。
このシャッフルを何回か繰り返します。

カードの山の最初の並び（文字列）と h の列を読み込み、最後の並び（文字列）を出力するプログラムを作成して下さい。

'''
while True:
    cards = input()
    if cards == "_":
        break

    m = int(input())

    for _ in range(m):
        h = int(input())
        previous    = cards[:h]
        following   = cards[h:]
        cards = previous + following

    print(cards)
