'''
１つの単語 W と文章 T が与えられます。T の中にある W の数を出力するプログラムを作成して下さい。

文章 T に含まれるスペースまたは改行で区切られた文字列を単語 Ti とします。すべての Ti において単語 W と同じになるものを数えて下さい。

なお、大文字と小文字は区別しません。
'''

word = input()
cnt = 0

while True:
    text = input()
    if text == "END_OF_TEXT":
        break
    else:
        text = text.lower().split()
        for i in text:
            if word == i:
                cnt+=1

print(cnt)

'''
別解
countメソッドを使えばスッキリ書ける

cnt += text.lower().split().count(word)

これでtext内のwordの数が求まる
'''
