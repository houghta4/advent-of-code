INPUT = '2023/4/1/input.txt'

def main():
    ans = 0
    with open(INPUT) as scratchcards:
        for card in scratchcards:
            points = 0
            card = card[card.find(':') + 2:].strip()
            delim_idx = card.find('|')
            winning = card[:delim_idx].split(' ')
            nums = card[delim_idx + 1:].split(' ')
            for n in nums:
                if n and n in winning:
                    if points == 0:
                        points = 1
                    else:
                        # print(f'{n} is present in the winning numbers')
                        points *= 2
            ans += points
    print(f'file: {INPUT} = {ans}')

if __name__ == '__main__':
    main()