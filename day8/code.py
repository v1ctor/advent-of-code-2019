import sys

def get_minimum_layer(s, cols, rows):
    chunk_size = cols * rows
    result = 0
    minVal = chunk_size + 1
    image = list('2' * chunk_size)
    for i in range(0, len(s), chunk_size):
        layer = s[i:i+chunk_size].strip()
        if len(layer) == 0:
            break
        for j in range(chunk_size):
            if image[j] != '2':
                continue
            else:
                image[j] = layer[j]
        zero = layer.count('0')
        if zero < minVal:
            minVal = zero
            result = layer.count('1') * layer.count('2')
    for k in range(0, len(image), cols):
        print(''.join(image[k:k+cols]))

    return result
    



def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    f = open(filename)
    s = f.readline()

    print(get_minimum_layer(s, 25, 6))

if __name__== "__main__":
    main()
