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