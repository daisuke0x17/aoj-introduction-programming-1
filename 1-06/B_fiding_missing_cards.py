'''
太郎が花子と一緒にトランプ遊びをしようとしたところ、52枚あるはずのカードが n 枚のカードしか手元にありません。これらの n 枚のカードを入力として、足りないカードを出力するプログラムを作成して下さい。
'''

all_cards = [(s, n) for s in ['S', 'H', 'C', 'D'] for n in range(1, 14)]
n = int(input())
my_cards =[]
for _ in range(n):
    simbol,rank = input().split()
    rank = int(rank)
    my_cards.append((simbol,rank))

for card in all_cards:
    if card not in my_cards:
        print(*card)
