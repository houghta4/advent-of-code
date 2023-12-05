from collections import OrderedDict

INPUT = '2023/5/2/input.txt'

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

def main():
    result_maps = parse_input()
    seeds_map = result_maps.get('seeds')
    seeds = []
    for i in range(1, len(seeds_map), 2):
        start = seeds_map[i - 1]
        seeds.append((start, start + seeds_map[i]))
    # print(seeds)

    # each map we update seeds with ranges
    for k, v in result_maps.items():
        # print(k, seeds)
        if k != 'seeds':
            tmp = []
            # have to use while loop over seeds because unlike pt1, we can have more ranges than we started with
            while seeds:
                start, end = seeds.pop()
                # print('start, end:', start, end)
                for dest_strt, src_strt, rng_len in v:
                    # find intersections (translate_map refactor from pt1)
                    o_strt = max(start, src_strt)
                    o_end = min(end, src_strt + rng_len)
                    if o_strt < o_end:
                        # print('o_strt < o_end')
                        tmp.append((o_strt - src_strt + dest_strt, o_end - src_strt + dest_strt))
                        # if intersection start is > original start, we need to add that section back to seeds
                        if o_strt > start:
                            # print('seeds.append', start, o_strt)
                            seeds.append((start, o_strt))
                        if end > o_end:
                            # print('seeds.append', o_end, end)
                            seeds.append((o_end, end))
                        break
                # else happens if loop fully finishes without breaking. eg there is no overlap
                else:
                    # print('tmp.append', start, end)
                    tmp.append((start, end))

            seeds = tmp

    print(f'file: {INPUT} = {min(seeds)[0]}')

if __name__ == '__main__':
    main()
    # print(translate_map(82, 60, 56, 37))
    # print(translate_map(82, 56, 93, 4))
