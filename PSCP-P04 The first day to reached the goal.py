"""PSCP-P04 The first day to reached the goal"""

def main():
    """Main Function"""
    day, target = map(int, input().split())
    run = list(map(int, input().split()))
    total = 0

    for i in range(day):
        total += run[i]
        if total >= target:
            return print(i + 1)

    return print("-1")

main()
