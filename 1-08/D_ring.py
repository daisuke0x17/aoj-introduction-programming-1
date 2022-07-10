'''
図のようなリング状の文字列 s の任意の位置から、時計回りに連続した文字をいくつか選んで、文字列 p が作れるかを判定するプログラムを作成してください。
'''

s = input()
p = input()
s += s

if p in s:
    print("Yes")
else:
    print("No")
