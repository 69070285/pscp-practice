"""PSCP-P01 Character Type Count"""

def main():
    """Main Function"""
    text = input()
    up_char = 0
    low_char = 0
    num = 0

    for char in text:
        if char.isupper():
            up_char += 1
        elif char.islower():
            low_char += 1
        elif char.isnumeric():
            num += 1

    print(up_char, low_char, num)

main()
