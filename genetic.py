from random import randint

class Genetic:
    pool = []
    fitness = []

    # Initializes pool with n strings
    def __init__(self, num=10, length=10):     
        for i in range(num):
            self.pool.append(self.generate(length))

    # Generates a random string of length n
    def generate(self, n):
        return "".join(chr(97 + randint(0, 25)) for j in range(n))

    # Calculates fitness of each string and saves in array
    def calc_fitness(self):
        self.fitness = [self.fitness_func(s) for s in self.pool]

    # Sorts strings in pool by a given array
    def sort_pool_by(self, arr):
        self.pool = [s for _, s in sorted(zip(arr, self.pool))]

    # Replaces bottom n strings in pool with top n strings
    def select_top(self, n):
        self.pool[-n:] = self.pool[:n]

    # Fitness function
    def fitness_func(self, s):
        return sum(ord(c) for c in s)

    # Crossover between two strings in pool
    def crossover(self, m, n, i=0):
        snew = self.pool[m][:i] + self.pool[n][i:]
        tnew = self.pool[n][:i] + self.pool[m][i:]
        self.pool[m] = snew
        self.pool[n] = tnew

    # Mutates string at index j by n characters
    def mutate(self, j, n=1):
        snew = [c for c in self.pool[j]]
        for i in range(n):
            k = randint(0, len(snew) - 1)
            snew[k] = chr(97 + randint(0, 25))
        self.pool[j] = "".join(snew)

    # Allows pool to evolve for a fixed number of generations
    def evolve(self, gen=100, mutations=1, top=5):
        for i in range(gen):
            for j in range(0, len(self.pool), 4):
                self.mutate(j, mutations)
            for j in range(0, len(self.pool), 2):
                self.crossover(j, j+1, len(self.pool) // 2)
            self.calc_fitness()
            self.sort_pool_by(self.fitness)
            self.pool.reverse()
            self.select_top(top)
            r = [randint(1, 1000) for j in range(len(self.pool))]
            self.sort_pool_by(r)

alphabet = Genetic(100, 20)
alphabet.evolve(100)

print(alphabet.pool[:10])