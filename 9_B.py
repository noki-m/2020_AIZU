#シャッフル
#https://onlinejudge.u-aizu.ac.jp/problems/ITP1_9_B

#カードの山の最初の並び（文字列）と h の列を読み込み、最後の並び（文字列）を出力するプログラムを作成して下さい。

# Sample Input 1
#aabc
#3
#1
#2
#1
#vwxyz
#2
#3
#4
#-
# Sample Output
#aabc
#xyzvw


while True:
    str = input()    #最初の並びを表す文字列
    if str == '-':
        break

    m = int(input())        #シャッフル回数 m
    
    for i in range(m):      #シャッフルの動作
        h = int(input())    #下から h 枚のカードをまとめて取り出し、残ったカードの山の上に積み上げ
        left = str[0:h]       #最初のh文字         開始インデックスから終了インデックスの手前までの要素を取得
        right = str[h:]       #残りのh文字         開始インデックスを省略すると最初の要素から取得
        str = right+left         #riの末尾に連結   終了インデックスを省略すると最後の要素まで取得
    print(str)


