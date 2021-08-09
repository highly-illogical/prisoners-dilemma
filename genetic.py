from random import randint

pool = []
f = []

for i in range(100):
    pool.append("".join(chr(97 + randint(0, 25)) for j in range(20)))

def fitness(s):
    return sum(ord(c) for c in s)

def crossover(s, t, i):
    snew = s[:i] + t[i:]
    tnew = t[:i] + s[i:]
    return [snew, tnew]

def mutate(s, n):
    snew = [c for c in s]
    for i in range(n):
        k = randint(0, len(snew) - 1)
        snew[k] = chr(97 + randint(0, 25))
    return "".join(snew)

def calc_fitness(pool):
    return [fitness(s) for s in pool]

def sort_by(a, b):
    return [s for _, s in sorted(zip(a, b))]

for i in range(5000):
    f = calc_fitness(pool)
    pool = sort_by(f, pool)
    pool[-5:] = pool[:5]
    r = [randint(1, 1000) for j in range(100)]
    pool = sort_by(r, pool)
    for j in range(0, 100, 2):
        pool[j] = mutate(pool[j], 1)
        pool[j], pool[j+1] = crossover(pool[j], pool[j+1], 10)

print(pool[:10])