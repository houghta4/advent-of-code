INPUT = '2023/4/2/test.txt'
    
class ScratchCard:
    def __init__(self, n, pts):
        self.card = n
        self.instances = 1
        self.points = pts

    def __repr__(self):
        return f'Card: {self.card} - points: {self.points}' if self.instances == 1 else f'Card: {self.card} ({self.instances}) - points: {self.points}'

def main():
    ans = 0
    cards = []
    with open(INPUT) as scratchcards:
        for i, card in enumerate(scratchcards):
            points = 0
            card = card[card.find(':') + 2:].strip()
            delim_idx = card.find('|')
            winning = card[:delim_idx].split(' ')
            nums = card[delim_idx + 1:].split(' ')
            for n in nums:
                if n and n in winning:
                    points += 1
            cards.append(ScratchCard(i + 1, points))

        for c in cards:
            for j in range(c.card, c.card + c.points):
                cards[j].instances += c.instances
            ans += c.instances
        
    # print(cards)

    print(f'file: {INPUT} = {ans}')

if __name__ == '__main__':
    main()