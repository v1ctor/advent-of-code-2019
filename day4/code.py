
def match(i):
    dup = False
    dec = True
   
    d = i % 10
    i = i / 10
    while i > 0:
        n = i % 10
        i = i / 10
        if n == d:
            dup = True
        if n > d:
            dec = False
        d = n
    return dup and dec


def number_of_passwords(start, end):
    counter = 0
    for i in range(start, end):
        if match(i):
            counter += 1
    return counter


def main():
    print(number_of_passwords(272091, 815432))

if __name__ == "__main__":
    main()
