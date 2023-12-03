INPUT = '2023/3/2/input.txt'
class Part:
    def __init__(self, val: str):
        self.val = val
        self.gear_loc = None
        self.parts = 0

    def __repr__(self):
        return str(self.val)

def main():
    ans = 0
    with open(INPUT) as schematic:
        grid = [[Part(part) for part in line.strip()] for line in schematic]
        def check_neighbors(i, j):
            dir_map = [
                [-1, -1], [-1, 0], [-1, 1],
                [0, -1],          [0, 1],
                [1, -1], [1, 0] , [1, 1]
            ]
            part = grid[i][j]
            for dir in dir_map:
                y = i + dir[0]
                x = j + dir[1]
                if part.val.isdigit() and 0 <= y < len(grid) and 0 <= x < len(grid[i]):
                    n = grid[y][x]
                    if n.val == '*':
                        part.gear_loc = grid[y][x]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                check_neighbors(i, j)
        
        d = {}
        for i in range(len(grid)):
            j = 0
            while j < len(grid[i]):
                gear = grid[i][j].gear_loc
                if gear:
                    parts += grid[i][j].val
                    # add all numbers connecting to the left
                    k = j - 1
                    while k >= 0 and grid[i][k].val.isdigit():
                        parts = grid[i][k].val + parts
                        k -= 1
                    # add all numbers connecting to the right
                    k = j + 1
                    while k < len(grid[i]) and grid[i][k].val.isdigit():
                        parts += grid[i][k].val
                        k += 1
                    if k != j and k < len(grid[i]):
                        j = k
                    if gear in d:
                        d[gear] *= int(parts)
                    else:
                        d[gear] = int(parts)
                    gear.parts += 1
                parts = ''
                j += 1

    for (p, i) in d.items():
        if p.parts == 2:
            ans += i
            # print(i)
            
        # else:
        #     print(f'{i} is not included beacuse it has {p.parts} parts')
    print(f'file: {INPUT} = {ans}')

if __name__ == '__main__':
    main()