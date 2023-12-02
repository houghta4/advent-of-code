INPUT = '2023/1/2/input.txt'

digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def main():
    ans = 0
    with open(INPUT) as calibrations:
        for line in calibrations:
            first, first_idx = '', float('inf')
            last, last_idx = '', -1

            # flatten dict into list of keys and values
            for d in list(sum(digits.items(), ())):
                idx = line.find(d)
                if idx != -1 and idx < first_idx:
                    first_idx = idx
                    if d.isdigit():
                        first = d
                    else:
                        first = digits[d]
                idx = line.rfind(d)
                if idx != -1 and idx > last_idx:
                    last_idx = idx
                    if d.isdigit():
                        last = d
                    else:
                        last = digits[d]
            ans += int(first + last)

    print(f'file: {INPUT} = {ans}')


if __name__ == '__main__':
    main()