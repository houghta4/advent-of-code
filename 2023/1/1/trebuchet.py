INPUT = '1/1/input.txt'
def main():
    ans = 0
    with open(INPUT) as calibrations:
        for l in calibrations:
            tmp = ''
            for s in l:
                if s.isdigit():
                    tmp += s
                    break
            for s in l[::-1]:
                if s.isdigit():
                    tmp += s
                    break
            ans += int(tmp)

    print(f'file: {INPUT} = {ans}')
if __name__ == '__main__':
    main()