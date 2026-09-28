"""PSCP-P12 Latest Student Scores"""

def main():
    """Main Function"""
    data = {}
    score, student = map(int, input().split())
    for _ in range(score):
        st, sc = input().split()
        data[st] = sc

    for _ in range(student):
        st = input()
        if st not in data:
            print("NOT FOUND")
        else:
            print(data[st])

main()
