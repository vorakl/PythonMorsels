import re

def parse_ranges(ranges):
    for mult, single in re.findall(r'(\d+-\d+)|(\d+)', ranges):
        if single:
            mult = '-'.join((single, single))
        low, high = mult.split('-')
        yield from range(int(low), int(high)+1)
