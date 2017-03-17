import sys

def decode(data):
    if not data:
        return ''

    lastseen = ''
    decompressed_list = []
    for c in data:
        if not c.isdigit():
            lastseen = c
            decompressed_list.append(c)
        else:
            n = int(c)
            for i in range(n-1):
                decompressed_list.append(lastseen)

    return ''.join(decompressed_list)


if __name__ == "__main__":
    path = sys.argv[1]
    with open(path) as file:
        data = file.read()
        print(decode(data))
