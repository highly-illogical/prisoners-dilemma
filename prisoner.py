class Strategy:
    strategy = None
    history = 0
    points = 0
    games = 1

    def __init__(self, strategy):
        self.strategy = strategy

    def __repr__(self):
        return "Strategy: "+self.strategy+" History: "+str(self.history)+" Avg: "+str(self.points/self.games)

    def play(self):
        return int(self.strategy[self.history])

    def set_history(self, hist):
        self.history = hist

def playPD(s1, s2, matrix, n=1):
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
        
    #s1.set_history(0)
    #s2.set_history(0)
    return outcome