"""PSCP-P03 Password Format Check"""

def main():
    """Main Function"""
    password = input()
    up, low, num = False, False, False

    for char in password:
        if char.isupper():
            up = True
        elif char.islower():
            low = True
        elif char.isnumeric():
            num = True

    if up and low and num and len(password) >= 8:
        print("VALID")
    else:
        print("INVALID")

main()
