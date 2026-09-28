"""PSCP-P07 Collapse duplicate characters"""

def main():
    """Main Function"""
    text = input()
    result = ""

    for char in text:
        if not result or char != result[-1]:
            result += char

    print(result)

main()

