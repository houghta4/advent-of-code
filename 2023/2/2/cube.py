INPUT = '2023/2/2/input.txt'

def main():
    ans = 0
    with open(INPUT) as games:
        for game in games:
            game = game[game.find(':') + 2:]
            r, g, b = 0, 0, 0
            for search in game.split(';'):
                search = search.strip()
                for pull in search.split(','):
                    pull = pull.strip()
                    if 'green' in pull:
                        g = max(g, int(pull.split(' ')[0]))
                    elif 'red' in pull:
                        r = max(r, int(pull.split(' ')[0]))
                    else:
                        b = max(b, int(pull.split(' ')[0]))
    
            ans += r * g * b
    print(f'file: {INPUT} = {ans}')

if __name__ == '__main__':
    main()