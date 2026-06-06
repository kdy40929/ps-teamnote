def make_xor_basis(arr):
    n = len(arr)
    basis = [0]*60
    for i in range(n):
        for j in range(59, -1, -1):
            if (arr[i]>>j) & 1:
                if basis[j]: arr[i] ^= basis[j]
                else: basis[j] = arr[i]; break
    return basis