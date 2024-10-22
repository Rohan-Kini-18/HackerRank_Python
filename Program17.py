def split_and_join(line):
    # write your code here
    rk=line.split(' ')
    rk='-'.join(rk)
    return rk
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
