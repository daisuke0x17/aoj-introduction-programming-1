'''
与えられた数列を逆順に出力するプログラムを作成して下さい。
'''

n = int(input())
num_lst = list(map(int,input().split()))
num_lst.reverse()
print(*num_lst)


'''
別解
n = int(input())
num_lst = list(map(int,input().split()))
reverse_num_lst =[]

for i in range(n):
    reverse_num_lst.append(num_lst[-(i+1)])
print(*reverse_num_lst)
'''
