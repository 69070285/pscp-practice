"""PSCP-P02 Product of non-zero digits"""

def main():
    """Main Function"""
    num = input()
    result = 1

    for n in num:
        if int(n):
            result *= int(n)

    print(0 if not int(num) else result)

main()
