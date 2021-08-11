class Strategy:
    strategy = ""
    history = [0, 0, 0]
    points = 0
    games = 1

    def __init__(self, strategy):
        self.strategy = strategy
        self.set_history(int(strategy[-6])*2 + int(strategy[-5]))
        self.set_history(int(strategy[-4])*2 + int(strategy[-3]))
        self.set_history(int(strategy[-2])*2 + int(strategy[-1]))

    def __repr__(self):
        return " ".join(self.strategy[i:i+4] for i in range(0, len(self.strategy)-1, 4))

    def play(self):
        index = self.history[0] * 16 + self.history[1] * 4 + self.history[2]
        return int(self.strategy[index])

    def set_history(self, hist):
        self.history = [self.history[1], self.history[2], hist]

def playPD(s1, s2, matrix, n=1):
    oc = []
    for i in range(n):
        p1 = s1.play()
        p2 = s2.play()

        outcome = matrix[p1][p2]
        s1.points += outcome[0]
        s2.points += outcome[1]
        s1.set_history(p1*2+p2)
        s2.set_history(p2*2+p1)
        s1.games += 1
        s2.games += 1
        oc.append(p1*2 + p2)
    return oc

if __name__ == '__main__':
    from random import randint 

    s = Strategy("".join(str(randint(0, 1)) for i in range(64)))
    t = Strategy("".join(str(randint(0, 1)) for i in range(64)))
    mat = [[(3,3), (0,5)], 
    [(5,0), (1,1)]]

    print(s.strategy, t.strategy)
    playPD(s, t, mat, 100)
    print(s.points, t.points)