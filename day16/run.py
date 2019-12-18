import sys

pattern = [0, 1, 0, -1]

def pattern_generator(n):
    if n <= 0:
        return
    left = n - 1
    i = 0
    while True:
        while left > 0:
            left -= 1
            yield pattern[i]
        i = (i + 1) % len(pattern)
        left = n


def ftt(commands, phase):

    result = []
    itter = 1
    while itter <= phase:
        result = []
        for i in range(1, len(commands) + 1):
            g = pattern_generator(i)
            s = 0
            for command in commands:
                s += command * next(g)
            result.append(abs(s) % 10)
        commands = result
        itter += 1

    return result


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    f = open(filename)
    line = f.readline().strip()


    commands = list(map(int, list(line)))
    offset = int(''.join(str(x) for x in commands[:7]))
    print("offset {}".format(offset))

    result = ftt(commands * 10000, 100)
    print(''.join(str(x) for x in result[offset:8]))


if __name__== "__main__":
    main()
