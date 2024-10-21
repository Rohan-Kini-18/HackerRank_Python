if __name__ == '__main__':
    n = int(input())
    Tuple1 = map(int, input().split())
    rk = tuple(Tuple1)
    print(hash(rk))
