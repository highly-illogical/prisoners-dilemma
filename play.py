from prisoner import Strategy, playPD
from random import sample
import matplotlib.pyplot as plt

strats = {
    "0000": 5,
    "0101": 25,
    "1010": 5,
    "1111": 5
}

strats_table = {
    "0000": [strats["0000"]],
    "0101": [strats["0101"]],
    "1010": [strats["1010"]],
    "1111": [strats["1111"]]
}

players = []

for strat, num in strats.items():
    for i in range(num):
        players.append(Strategy(strat))

m = [[(3,3), (-1,5)], 
    [(5,-1), (0,0)]]

for r in range(200):
    for i in range(100):
        p = sample(players, 2)
        for k in range(5):
            playPD(p[0], p[1], m)
    players.sort(key=lambda x: x.points/x.games)
    strats[players[0].strategy] -= 1
    strats[players[-1].strategy] += 1

    for s in strats_table:
        strats_table[s].append(strats[s])

    players[0] = Strategy(players[-1].strategy)

for s in strats_table:
    plt.plot(strats_table[s], label=s)
plt.legend()
plt.show()