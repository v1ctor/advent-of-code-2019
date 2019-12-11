import sys

def get_minimum_layer(s, cols, rows):
    chunk_size = cols * rows
    result = 0
    minVal = chunk_size + 1
    for i in range(0, len(s), chunk_size):
        layer = s[i:i+chunk_size].strip()
        if len(layer) == 0:
            break
        zero = layer.count('0')
        if zero < minVal:
            minVal = zero
            result = layer.count('1') * layer.count('2')
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
