"""PSCP-P06 Date of greatest price change"""

def main():
    """Main Function"""
    day = int(input())
    price = list(map(int, input().split()))
    most_change = -1
    change_day = 0

    for i in range(1, day):
        if abs(price[i - 1] - price[i]) > most_change:
            most_change = abs(price[i - 1] - price[i])
            change_day = i + 1

    print(change_day, most_change)

main()
