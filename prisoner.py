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

def playPD(s1, s2, matrix):
    outcome = matrix[s1.play()][s2.play()]
    s1.points += outcome[0]
    s2.points += outcome[1]
    s1.history = s1.play()*2+s2.play()
    s2.history = s2.play()*2+s1.play()
    s1.games += 1
    s2.games += 1
    return outcome