"""PSCP-P18 Passengers after passing the sign"""

def main():
    """Main Function"""
    bstop, check = map(int, input().split())
    passenger = [0]
    total = 0

    for _ in range(bstop):
        go_in, go_out = map(int, input().split())
        total += go_in - go_out
        passenger.append(total)

    for _ in range(check):
        place = int(input())
        print(passenger[place])

main()
