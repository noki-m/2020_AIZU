#文字列変換
#https://onlinejudge.u-aizu.ac.jp/problems/ITP1_9_D

#文字列 str に対して、与えられた命令の列を実行するプログラムを作成してください。

# Sample Input 1
#abcde
#3
#replace 1 3 xyz
#reverse 0 2
#print 1 4
# Sample Output 1
#xaze



str = list(input())     #文字列str
q = int(input())        #命令の数q
 
for i in range(q):      #命令分繰り返す
    
    cmd, a, b, *c = input().split()     #左から順に代入を終えたあと、余った要素がcに放り込まれる。
    
    a = int(a)
    b = int(b)
    
    if cmd == "print":      #a 文字目から b 文字目までを出力する。
        print(*str[a:b+1], sep='')              # * は「アンパック」、引数としてリストやタプルなどを分解して渡すことを意味する。＝print(str[0], str[1],…と同じ。
        
    elif cmd == "reverse":  #a 文字目から b 文字目までを逆順にする。
        str[a:b+1] = reversed(str[a:b+1])        #要素を逆順に取り出すイテレータを返す。元のリストは変更されない

    else:                   #replace a 文字目から b 文字目までを p に置き換える。
        str[a:b+1] = c[0]
