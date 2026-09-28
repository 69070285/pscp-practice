"""PSCP-P17 Same Number"""

def main():
    """Main Function"""
    f, s = map(int, input().split())
    if not f or not s:
        print("0")
        return
    first = set(input().split())
    second = set(input().split())

    print(len(first & second))

main()
