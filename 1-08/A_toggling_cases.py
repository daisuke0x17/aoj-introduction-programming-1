'''
与えられた文字列の小文字と大文字を入れ替えるプログラムを作成してください。
'''

str = input()
print(str.swapcase())


'''
別解（swapcaseだとあまりにもあっさりしているので笑）
words = input()
swapcase_words = ""

for i in range(len(words)):
    if words[i].islower():
        swapcase_words += words[i].upper()
    elif words[i].isupper():
        swapcase_words += words[i].lower()
    else:
        swapcase_words += words[i]

print(swapcase_words)
'''
