def main():
    import io, os
    input = io.BufferedReader(io.FileIO(0), 1<<18).readline
    out = []
    for _ in range(int(input())):
        a, b = map(int, input().split())
        out.append(f"{a+b}")
    os.write(1, '\n'.join(out).encode())
    os._exit(0)
main()