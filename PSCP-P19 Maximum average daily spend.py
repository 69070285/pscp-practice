"""PSCP-P19 Maximum average daily spend"""

def main():
    """Main Function"""
    day, lenght = map(int, input().split())
    spend = list(map(int, input().split()))
    start = sum(spend[:lenght])
    max_sum = start

    for i in range(lenght, day):
        start += spend[i] - spend[i - lenght]
        if start > max_sum:
            max_sum = start

    max_avg = max_sum / lenght
    method = int(max_avg * 100 + 0.5)
    print(f"{method // 100}.{method % 100:02d}")

main()
