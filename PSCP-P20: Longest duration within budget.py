"""PSCP-P20: Longest duration within budget"""

def main():
    """Main Function"""
    day, budget = map(int, input().split())
    spend = list(map(int, input().split()))
    start = 0
    total = 0
    max_len = 0

    for stop in range(day):
        total += spend[stop]

        while total > budget:
            total -= spend[start]
            start += 1

        current_len = stop - start + 1
        if current_len > max_len:
            max_len = current_len

    print(max_len)

main()
