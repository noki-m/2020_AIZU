#単語の検索
#https://onlinejudge.u-aizu.ac.jp/problems/ITP1_9_A

#１つの単語 W と文章 T が与えられます。T の中にある W の数を出力するプログラムを作成して下さい。

# Sample Input 1
#computer
#Nurtures computer scientists and highly-skilled computer engineers
#who will create and exploit "knowledge" for the new era.
#Provides an outstanding computer environment.
#END_OF_TEXT

# Sample Output
#3



count=0
W=str(input())	#単語Wを取得
while(True):
    T = str(input())        #文章Tを取得※1行ずつ
    if T=="END_OF_TEXT":    #END_OF_TEXTが来たら終わる
        break
    count += T.lower().split().count(W)     #countする(Tを小文字にしたものを小文字に、区切り文字で分割、各要素の個数（要素ごとの出現回数）をカウント)
print(count) 
