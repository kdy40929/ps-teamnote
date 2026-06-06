def hashing(left, right):
    return (hashlst[right] - powlst[right-left+1] * hashlst[left-1]) % mod

mod = 10**18 + 9; p = 31
s = input().rstrip()
hashlst = [0 for _ in range(len(s)+1)]
powlst = [1 for _ in range(len(s)+1)]
for i in range(1, len(s)+1):
    powlst[i] = powlst[i-1] * p % mod
hashlst[0] = ord(s[0]) - 97
for i in range(1, len(s)):
    hashlst[i] = (hashlst[i-1]*p + ord(s[i])-97)%mod