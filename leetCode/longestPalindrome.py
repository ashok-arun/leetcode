import sys
def longestPalindrome(s):
    maxLen = 1
    start = 0
    end = 1
    for i in range(0,len(s)-1):
        for j in range(i+2,len(s)+1):
            if len(s[i:j])>maxLen and isPalindrome(s[i:j]):
                maxLen=len(s[i:j])
                start = i
                end = j
    return s[start:end]  

def isPalindrome(x):
    y=str(x)
    for i in range(int(len(y)/2)):
        if y[i]!=y[len(y)-1-i]:
            return False
    return True

print(longestPalindrome(sys.argv[1]))
