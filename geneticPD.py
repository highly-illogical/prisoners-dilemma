from genetic import Genetic
from prisoner import Strategy, playPD
from random import randint, random

class GeneticPD(Genetic):
    mat = [[(3,3), (0,5)], 
    [(5,0), (1,1)]]

    interactions = []
    reps = [
        Strategy("0101010101010101010101010101010101010101010101010101010101010101000000")
    ]

    def __init__(self, num, length):
        super().__init__(num, length)
            
    def generate(self, n):
        return "".join(str(randint(0, 1)) for i in range(n))

    def calc_fitness(self):
        self.string_to_strat()
        self.interactions.append([0, 0, 0, 0])

        for j in range(len(self.pool)):
            for k in range(j+1, len(self.pool)):
                outcome = playPD(self.pool[j], self.pool[k], self.mat, 64)
                self.interactions[-1] = list(map(lambda x, y: x + y, self.interactions[-1], [outcome.count(i) for i in range(4)]))
        super().calc_fitness()
        self.strat_to_string()

    def fitness_func(self, s):
        return s.points

    def strat_to_string(self):
        self.pool = [s.strategy for s in self.pool]

    def string_to_strat(self):
        self.pool = [Strategy(s) for s in self.pool]
        
    def crossover_and_mutation(self, m, n, r, mr):
        snew, tnew = "", ""
        flag = True
        for i in range(len(self.pool[m])):
            if random() < r:
                flag = not flag
            if flag:
                if random() > mr:
                    snew = snew + self.pool[m][i]
                else:
                    snew = snew + str(1 - int(self.pool[m][i]))
                if random() > mr:
                    tnew = tnew + self.pool[n][i]
                else:
                    tnew = tnew + str(1 - int(self.pool[n][i]))
            else:
                if random() > mr:
                    snew = snew + self.pool[n][i]
                else:
                    snew = snew + str(1 - int(self.pool[n][i]))
                if random() > mr:
                    tnew = tnew + self.pool[m][i]
                else:
                    tnew = tnew + str(1 - int(self.pool[m][i]))
        self.pool[m] = snew
        self.pool[n] = tnew

    def evolve(self, gen, mutations=1):
        for i in range(gen):
            for j in range(0, len(self.pool), 2):
                self.crossover_and_mutation(j, j+1, 0.03, 0.02)

            self.calc_fitness()
            self.sort_pool_by(self.fitness)
            self.pool.reverse()
            self.select_top(int(0.2 * len(self.pool)))
            r = [randint(1, 1000) for j in range(len(self.pool))]
            self.sort_pool_by(r)

generations = 200
p = GeneticPD(20, 70)
p.evolve(generations)

pool = [Strategy(s) for s in p.pool[:10]]

for k in pool:
    print(k)

from matplotlib import pyplot as plt

x = range(generations)
plt.plot(x, p.interactions)
plt.show()