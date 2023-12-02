INPUT = '2023/2/1/input.txt'

def main():
    RED, GREEN, BLUE = 12, 13, 14
    ans = 0
    with open(INPUT) as games:
        g = games.readlines()
        ans = sum(range(len(g) + 1))
        print(ans)
        for i, game in enumerate(g):
            game = game[game.find(':') + 2:]
            for search in game.split(';'):
                r, g, b = 0, 0, 0
                search = search.strip()
                for pull in search.split(','):
                    pull = pull.strip()
                    if 'green' in pull:
                        g = int(pull.split(' ')[0])
                    elif 'red' in pull:
                        r = int(pull.split(' ')[0])
                    else:
                        b = int(pull.split(' ')[0])
                if r > RED or g > GREEN or b > BLUE:
                    ans -= i + 1
                    break
    
    print(f'file: {INPUT} = {ans}')

if __name__ == '__main__':
    main()