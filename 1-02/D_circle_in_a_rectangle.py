'''
長方形の中に円が含まれるかを判定するプログラムを作成してください。
次のように、長方形は左下の頂点を原点とし、右上の頂点の座標 (W,H) が与えられます。
また、円はその中心の座標 (x,y) と半径 r で与えられます。
'''

w,h,x,y,r = map(int,input().split())

if (x+r)>w or (x-r)<0:
    print('No')
elif (y+r)>h or (y-r)<0:
    print('No')
else:
    print('Yes')
