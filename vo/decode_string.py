"""
a is encoded as 1, b encoded as 2, ... i encoded as 9...
j isencoded as 10#, ... z is eoncoded as 26#
(#num) if there are more than 1

Example
String "abzx" --> s = "1226#24#"
String "aabccc" -->‍‌‌‌‍‌‍‍‌‌‍‌‌‌‌‍‍‍‌‍ s = "1(2)23(3)"
String "bajj" --> s = "2110#(2)"
String "wwxyzwww" -> s = "23#(2)24#25#26#23#(3)

Sample Input 0
1226#24#
Sample Output 0
1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1
"""

def check(st):
    res = [0 for _ in range(26)]
    n = len(st)
    i = n - 1

    #decode reversely
    while i >= 0:

        cnt = 0
        # num = decoded num
        num = 0

        if st[i] == ')':
            i -= 1
            digit = 0
            while st[i] != '(':
                print(st[i])
                cnt += int(st[i]) *( 10 ** digit)
                digit += 1
                i -= 1

            #remove '('
            i-=1

        # j -> z
        if st[i] == '#':
            i -= 2
            num = int(st[i]) * 10 + int(st[i+1])
        #a -> i
        if num == 0:
            num = int(st[i])


        cnt = cnt if cnt!=0 else 1
        print("add:", num,"x",cnt)
        res[num-1] += cnt
        print(res)
        i -= 1
    return " ".join(map(str,res))




#st = "abzx"
# encoded = "1226#24#"
encoded = "21(199)10#(2)"
ret=check(encoded)
print("---")
print(ret)