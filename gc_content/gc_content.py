with open('rosalind_gc.txt', 'r') as in_file:
    max_percentage, max_code = -1, ''
    while True:
        name, chain = in_file.readline().strip(), in_file.readline().strip()
        if not chain:
            break
        else:
            percentage = (chain.count('G') + chain.count('C')) * 100 / len(chain)
            if percentage > max_percentage:
                max_percentage, max_code = percentage, name
    print(f'{max_code}' + "\n%.6f" % max_percentage)