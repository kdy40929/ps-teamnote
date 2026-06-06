from bisect import bisect_right
def merge(l1, l2):
    i, j = 0, 0
    ans = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            ans.append(l1[i])
            i += 1
        else:
            ans.append(l2[j])
            j += 1
    if i == len(l1):
        while j < len(l2):
            ans.append(l2[j])
            j += 1
    elif j == len(l2):
        while i < len(l1):
            ans.append(l1[i])
            i += 1
    return ans

def makeseg(left, right, i):
    if left == right:
        mstree[i].append(arr[left])
        return
    mid = (left + right)//2
    makeseg(left, mid, 2*i)
    makeseg(mid+1, right, 2*i+1)
    mstree[i] = merge(mstree[2*i], mstree[2*i+1])
    return

def count(left, right, i, start, end, val):
    # the number of elements bigger than val in [left, right]
    if end < left or right < start: return 0
    if start <= left and right <= end:
        return right - left + 1 - bisect_right(mstree[i], val)
    mid = (left + right)//2
    return count(left, mid, 2*i, start, end, val) + count(mid+1, right, 2*i+1, start, end, val)