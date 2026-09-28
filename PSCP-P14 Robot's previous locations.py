"""PSCP-P14 Robot's previous locations"""

def main():
    """Main Function"""
    cmd = input()
    spot = {(0, 0)}
    x = 0
    y = 0

    for c in cmd:
        if c == "U":
            y += 1
        elif c == "D":
            y -= 1
        elif c == "R":
            x += 1
        else:
            x -= 1
        spot.add((x, y))

    print(len(spot))

main()
