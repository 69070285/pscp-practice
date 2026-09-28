"""PSCP-P09 Missing Number"""

def main():
    """Main Function"""
    amount = int(input())
    if amount == 1:
        print("1")
        return
    number = set(map(int, input().split()))

    for n in range(1, amount + 1):
        if n not in number:
            print(n)
            break

main()
