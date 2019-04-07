def k_fib(n, k):
    kf = [1, 1]
    for i in range(n - 2):
        kf.append(kf[-1] + k * kf[-2])
    return kf[-1]


with open('rosalind_fib.txt', 'r') as in_file:
    for line in in_file.readlines():
        values = list(map(int, line.strip().split(' ')))
        n, k = values[0], values[1]
        print(k_fib(n, k))