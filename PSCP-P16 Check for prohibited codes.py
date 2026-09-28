"""PSCP-P16 Check for prohibited codes"""

def main():
    """Main Function"""
    _, check = map(int, input().split())
    code = set(input().split())

    for _ in range(check):
        guess = input()
        if guess in code:
            print("YES")
        else:
            print("NO")

main()
