"""PSCP-P15 Product Ranking"""

def main():
    """Main Function"""
    amount = int(input())
    product = [input().split() for _ in range(amount)]
    product.sort(key=lambda p: (-int(p[1]), float(p[2]), p[0]))

    for p in product:
        print(p[0])

main()
