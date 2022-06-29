'''
文字列 str に対して、与えられた命令の列を実行するプログラムを作成してください。命令は以下の操作のいずれかです：

'''

from audioop import reverse


input_str = input()

q = int(input())

for _ in range(q):
    order   = input().split()
    a,b     = map(int,order[1:3])
    if order[0]== "print":
        print(input_str[a:b+1])
    elif order[0] == "reverse":
        reverse     = input_str[a:b+1]
        input_str   = input_str[:a] + reverse[::-1] + input_str[b+1:]

    elif order[0] == "replace":
        replace     = order[3]
        input_str   = input_str[:a] + replace + input_str[b+1:]

    else:
        pass
