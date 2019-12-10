
def match(i):
    dup = False
    dec = True
   
    d = i % 10
    i = i / 10
    group = 1
    while i > 0:
        n = i % 10
        i = i / 10
        if n == d:
            group += 1
        elif group == 2:
            dup = True
            group = 1
        else:
            group = 1
            
        if n > d:
            dec = False
        d = n
    return (dup or group == 2) and dec


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
