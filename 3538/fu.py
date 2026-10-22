"""fu"""
def main():
    """fu"""
    s = input().strip()
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    unpaired = []
    for char in freq:
        if freq[char] % 2:
            unpaired.append(char)

    if not unpaired:
        print("fully paired")
    else:
        print("".join(unpaired))

main()
