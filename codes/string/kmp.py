def makefail(s):
    failf = [0] * len(s)
    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = failf[j-1]
        if s[i] == s[j]:
            j += 1
            failf[i] = j
    return failf

def kmp_search(s1, s2):
    # find s2 in s1
    failf = makefail(s2)
    result = []
    j = 0
    for i in range(len(s1)):
        while j > 0 and s1[i] != s2[j]:
            j = failf[j-1]
        if s1[i] == s2[j]:
            j += 1
            if j == len(s2):
                result.append(i-j+2)
                j = failf[j-1]
    return result