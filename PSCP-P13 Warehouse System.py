"""PSCP-P13 Warehouse System"""

def main():
    """Main Function"""
    amount = int(input())
    storage = {}

    for _ in range(amount):
        cmd = input().split()
        if cmd[0] == "ADD":
            item, qty = cmd[1], int(cmd[2])
            storage[item] = storage.get(item, 0) + qty
        elif cmd[0] == "SELL":
            item, qty = cmd[1], int(cmd[2])
            if item in storage and storage[item] - qty >= 0:
                storage[item] -= qty
        else:
            print(storage.get(cmd[1], 0))

main()
