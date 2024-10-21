if __name__ == '__main__':
    stud = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        stud.append([name, score])
low = sorted(set([score for name, score in stud]))[1]
print('\n'.join(sorted([name for name, score in stud if score == low])))
