import sys
from itertools import groupby

def encode(data):

    compressed_str = "".join(['{0}{1}'.format(i, sum([1 for _ in e])) for i,e in groupby(data)])
    if len(compressed_str) > len(data):
        return data
    else:
        return compressed_str

if __name__ == "__main__":
    path = sys.argv[1]
    with open(path) as file:
        data = file.read()
        print(encode(data))
