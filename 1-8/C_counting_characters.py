'''
要　見直し

与えられた文字列の列に含まれる、各アルファベットの数を数えるプログラムを作成して下さい。 なお、小文字と大文字は区別しません。
'''
while True:
    try:
        str = input()
    except EOFError:
        break
str = str.lower()
cnt = [0]*26
for ch in str.lower():
    try:
        num = ord(ch) - ord('a')
        cnt[num] += 1
    except IndexError:
        pass

for i,ch in enumerate(cnt):
    print(f"{chr(ord('a')+i)} : {ch}")
