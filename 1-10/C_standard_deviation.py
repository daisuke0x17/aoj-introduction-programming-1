'''
n 人の学生を含むクラスでプログラミングの試験を行った。それぞれの得点をs1, s2 ... snとしたときの、標準偏差を求めるプログラムを作成せよ。
'''
import math

while True:
    n = int(input())
    if n == 0:
        break
    score_array = list(map(int,input().split()))
    ave = sum(score_array)/n
    sum = 0
    for item in score_array:
        sum += (item - ave)**2
    dist = sum/len(score_array)

    print(math.sqrt(dist))

