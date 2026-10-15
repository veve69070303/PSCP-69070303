"""flower"""

def main():
    """flower"""
    L, N = map(int, input().split())
    diag = 1
    while N > 0:
        N = N - diag
        if N <= 0:
            break
        diag = diag + 1
    band = (diag - 1) // L + 1
    print(band)
main()
