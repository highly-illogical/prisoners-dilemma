from prisoner import Strategy, playPD
import random

strats = {
    "0000": 50,
    "0101": 50,
    "1010": 50,
    "1111": 50
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

mat = [[(3,3), (0,5)], 
    [(5,0), (1,1)]]

def all_against_all(n=1):
    k = len(players)
    for i in range(k):
        for j in range(i+1, k):
            playPD(players[i], players[j], mat, n)

def all_against_random(k=1, n=1):
    for p in players:
            play_new = [play for play in players]
            play_new.remove(p)
            qs = random.sample(play_new, k)
            for q in qs:
                playPD(p, q, mat, n)

def random_pairs(pairs=10, n=1):
    for pair in range(pairs):
        p = random.sample(players, 2)
        playPD(p[0], p[1], mat, n)

def selection(players, r=0.1):
    num = int(r*len(players))
    players.sort(key=lambda x: x.points/x.games)

    for i in range(num):
        strats[players[i].strategy] -= 1
        strats[players[-i-1].strategy] += 1
        players[i] = Strategy(players[-i-1].strategy)

    for s in strats_table:
        strats_table[s].append(strats[s])

    for player in players:
        player.points = 0
        player.games = 0

    return players