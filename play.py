from prisoner import Strategy
from random import sample

def playPD(s1, s2, matrix):
    outcome = matrix[s1.play()][s2.play()]
    s1.points += outcome[0]
    s2.points += outcome[1]
    s1.history = s1.play()*2+s2.play()
    s2.history = s2.play()*2+s1.play()
    s1.games += 1
    s2.games += 1
    return outcome

strats = ["0000", "0000", "0000", "0101", "0101", "0101", "0101", "1111"]
players = [Strategy(s) for s in strats]

m = [[(3,3), (-2,5)], 
    [(5,-2), (-1,-1)]]

for r in range(50):
    for i in range(100):
        p = sample(players, 2)
        for k in range(5):
            playPD(p[0], p[1], m)
    players.sort(key=lambda x: x.points/x.games)
    players[0] = Strategy(players[-1].strategy)

for p in players:
    print(p)