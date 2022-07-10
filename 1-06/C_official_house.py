'''
Ａ大学は１フロア１０部屋、３階建ての公舎４棟を管理しています。公舎の入居・退去の情報を読み込み、各部屋の入居者数を出力するプログラムを作成して下さい。
'''
all_rooms = [[[0 for i in range(10)]for j in range(3)]for k in range(4)]

n = int(input())

for _ in range(n):
    b,f,r,v = map(int,input().split())
    all_rooms[b-1][f-1][r-1] += v

for i in range(4):
    for room in all_rooms[i]:
        print(*room)
    if i != 3:
        print('#'*20)
