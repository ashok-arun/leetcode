import sys
def longestPalindrome(s):
    ret=""
    for i in range(len(s)):
        # 1 center point
        p1=palindrome(s,i,i)
        # 2 center points
        p2=palindrome(s,i,i+1)
        if len(p1)>len(ret):
            ret=p1
        if len(p2)>len(ret):
            ret=p2
    return ret

# checks if the sides are equal from the starting point.
def palindrome(s,x,y):
    while x>=0 and y<len(s) and s[x]==s[y]:
        x-=1
        y+=1
    return s[x+1:y]

print(longestPalindrome(sys.argv[1]))
