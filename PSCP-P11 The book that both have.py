"""PSCP-P11 The book that both have"""

def main():
    """Main Function"""
    try:
        _ = input()
        first = set(input().split())
        second = set(input().split())
        print(len(list(first & second)))
    except EOFError:
        print("0")

main()
