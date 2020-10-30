import sys
def isPalindrome(x):
    y=str(x)
    for i in range(int(len(y)/2)):
        if y[i]!=y[len(y)-1-i]:
            return False
    return True

print(isPalindrome(sys.argv[1]))
