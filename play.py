from prisoner import Strategy, playPD
from players import mat, strats, strats_table, players, selection, all_against_all, all_against_random, random_pairs
import matplotlib.pyplot as plt

for r in range(50):
    all_against_all(5)
    players = selection(players, 0.2)

for s in strats_table:
    plt.plot(strats_table[s], label=s)
plt.legend()
plt.show()