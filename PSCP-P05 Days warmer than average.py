"""PSCP-P05 Days warmer than average"""

def main():
    """Main Function"""
    day = int(input())
    temp = list(map(int, input().split()))
    avr = sum(temp) / day
    over = sum(1 for t in temp if t > avr)

    print(f"{avr:.2f}")
    print(over)

main()
