'''
与えられた数の各桁の和を計算するプログラムを作成して下さい。
'''

while True:
    number = int(input())
    if number == 0:
        break

    sum = 0
    while number > 0:
        sum += number%10
        number //= 10
    print(sum)

'''
別解（inputを文字列として扱う）
while True:
    str_x = input()
    if str_x == "0":
        break

    ans = 0
    for n in str_x:
        ans += int(n)
    print(ans)

参考
https://tysonblog-whitelabel.com/aizu-online-judge-itp1_8_b
'''
