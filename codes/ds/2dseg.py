import sys
input = sys.stdin.readline
def makey(lx, rx, ix, ly, ry, iy):
    if ly == ry:
        if lx == rx:
            seg[ix][iy] = board[lx][ly]
        else:
            seg[ix][iy] = seg[2*ix][iy] + seg[2*ix+1][iy]
        return
    my = (ly + ry)//2
    makey(lx, rx, ix, ly, my, 2*iy)
    makey(lx, rx, ix, my+1, ry, 2*iy+1)
    seg[ix][iy] = seg[ix][2*iy] + seg[ix][2*iy+1]
    return

def makex(lx, rx, ix):
    if lx == rx:
        makey(lx, rx, ix, 0, n-1, 1)
        return
    mx = (lx + rx)//2
    makex(lx, mx, 2*ix)
    makex(mx+1, rx, 2*ix+1)
    makey(lx, rx, ix, 0, n-1, 1)
    return

def updatey(lx, rx, ix, ly, ry, iy, x, y, val):
    if y > ry or y < ly: return
    if ly == ry:
        if lx == rx:
            seg[ix][iy] = val
        else:
            seg[ix][iy] = seg[2*ix][iy] + seg[2*ix+1][iy]
        return
    my = (ly + ry)//2
    updatey(lx, rx, ix, ly, my, 2*iy, x, y, val)
    updatey(lx, rx, ix, my+1, ry, 2*iy+1, x, y, val)
    seg[ix][iy] = seg[ix][2*iy] + seg[ix][2*iy+1]
    return

def updatex(lx, rx, ix, x, y, val):
    if x < lx or x > rx: return
    if lx == rx:
        updatey(lx, rx, ix, 0, n-1, 1, x, y, val)
        return
    mx = (lx + rx)//2
    updatex(lx, mx, 2*ix, x, y, val)
    updatex(mx+1, rx, 2*ix+1, x, y, val)
    updatey(lx, rx, ix, 0, n-1, 1, x, y, val)

def getsumy(ix, ly, ry, iy, y1, y2):
    if y2 < ly or ry < y1: return 0
    if y1 <= ly and ry <= y2: return seg[ix][iy]
    my = (ly + ry)//2
    return getsumy(ix, ly, my, 2*iy, y1, y2) + getsumy(ix, my+1, ry, 2*iy+1, y1, y2)

def getsumx(lx, rx, ix, x1, x2, y1, y2):
    if x2 < lx or rx < x1: return 0
    if x1 <= lx and rx <= x2:
        return getsumy(ix, 0, n-1, 1, y1, y2)
    mx = (lx + rx)//2
    return getsumx(lx, mx, 2*ix, x1, x2, y1, y2) + getsumx(mx+1, rx, 2*ix+1, x1, x2, y1, y2)

n, m = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(n)]
size = 2<<n.bit_length()
seg = [[0] * size for _ in range(size)]
makex(0, n-1, 1)
for _ in range(m):
    query = [*map(int, input().split())]
    if query[0] == 0:
        x, y, c = query[1:]
        updatex(0, n-1, 1, x-1, y-1, c)
    else:
        x1, y1, x2, y2 = map(lambda x: int(x)-1, query[1:])
        print(getsumx(0, n-1, 1, x1, x2, y1, y2))