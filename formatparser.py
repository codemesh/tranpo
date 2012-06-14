import sys

def parse_pos_pair(line) :
    pairs = line.split()
#    pairs_parsed = [(token, tag) for (token, tag) in pair.split('/') [pair for pair in pairs]]
    pairs_parsed = map(lambda pair: tuple(pair.split('/')), pairs)
    return pairs_parsed

if __name__ == '__main__' :
    pairs = parse_pos_pair(sys.argv[1])
    print pairs

    
