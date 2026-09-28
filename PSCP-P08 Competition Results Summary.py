"""PSCP-P08 Competition Results Summary"""

def main():
    """Main Function"""
    amount = int(input())
    win = 0
    draw = 0
    lose = 0
    score = 0

    for _ in range(amount):
        result = input()
        if result == "WIN":
            win += 1
            score += 3
        elif result == "DRAW":
            draw += 1
            score += 1
        else:
            lose += 1

    print(win, draw, lose)
    print(score)

main()
