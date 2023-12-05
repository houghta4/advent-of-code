from collections import OrderedDict

INPUT = '2023/5/1/input.txt'

def parse_input():
    result_maps = OrderedDict()
    current_map = None
    with open(INPUT) as file:
        for line in file:
            line = line.strip()
            # seeds is on the same line so special case
            if 'seeds: ' in line:
                current_map = 'seeds'
                result_maps[current_map] = []
                values = [int(value) for value in line.split()[1:]]
                if values:
                    result_maps[current_map] += values
            # new map
            elif ':' in line:    
                current_map = line[:-1]
                result_maps[current_map] = []
            elif current_map:
                values = [int(value) for value in line.split()]
                if values:
                    result_maps[current_map].append(values)
    return result_maps

# need to check each line in every map
def translate_map(src, dest_strt, src_strt):
    offset = src - src_strt
    return dest_strt + offset

def main():
    result_maps = parse_input()
    # modify in place for ans
    seeds_map = result_maps.get('seeds')
    # print(result_maps)

    for k, v in result_maps.items():
        if k != 'seeds':
            for i in range(len(seeds_map)):
                seed = seeds_map[i]
                # print(k, seed)
                tmp = seed
                for line in v:
                    # print(line)
                    src_rng = range(line[1], line[1] + line[2])
                    if seed in src_rng:
                        tmp = translate_map(seed, *line[:-1])
                seeds_map[i] = tmp
            # print(f'ans: {seeds_map}')
    

    print(f'file: {INPUT} = {min(seeds_map)}')

if __name__ == '__main__':
    main()
    # print(translate_map(82, 60, 56, 37))
    # print(translate_map(82, 56, 93, 4))
