"""PSCP-P10 Unique Courses"""

def main():
    """Main Function"""
    amount = int(input())
    subject = [input() for _ in range(amount)]
    result = []

    for s in subject:
        if s in result:
            continue
        result.append(s)

    print(len(result))
    print(*sorted(result), sep="\n")

main()
