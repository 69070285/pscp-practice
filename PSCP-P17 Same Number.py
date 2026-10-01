"""PSCP-P17 Same Number"""

def main():
    """Main Function"""
    f, s = map(int, input().split())
    if not f or not s:
        print("0")
        return
    first = set(input().split())
    count = 0

    for n in input().split():
        if n in first:
            count += 1
            first.remove(n)

    print(count)

main()
