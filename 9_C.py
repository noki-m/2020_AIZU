#カードゲーム
#https://onlinejudge.u-aizu.ac.jp/problems/ITP1_9_C

#太郎と花子の手持ちのカードの情報を読み込み、ゲーム終了後のそれぞれの得点を出力するプログラムを作成せよ。

# Sample Input
#3
#cat dog
#fish fish
#lion tiger
# Sample Output
#1 7




n=int(input())          #n枚のカード,nターンの勝負
taro=0
hanako=0

for i in range(n):                  #nターン繰り返す
    card1,card2=input().split()     #カード取得
    
    if  card1 < card2:              #勝者には３ポイント、引き分けの場合にはそれぞれ１ポイント
        hanako+=3                   #文字列の大小関係（順番）
    elif card1 == card2:
        taro+=1
        hanako+=1
    else:
        taro+=3
        
print(taro,hanako)

