import sys
def lengthOfLongestSubstring(s):
    slist = []
    maxLen = 1
    for item in s:
        if item in slist:
            slist=slist[slist.index(item)+1:]
        slist.append(item)
        maxLen = max(maxLen, len(slist))
    return maxLen

print(lengthOfLongestSubstring(sys.argv[1]))
