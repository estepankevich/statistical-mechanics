import random, math
import matplotlib.pyplot as plt
import numpy as np

d = 20
x = [0.0] * d
delta = 0.1
n_trials = 1000000
n_hits = 0
old_radius_square = 0
hist_data = []
for i in range(n_trials):
    k = random.randint(0, d - 1)
    x_old_k = x[k]
    x_new_k = x_old_k + random.uniform(-delta, delta)
    new_radius_square = old_radius_square + x_new_k ** 2 - x_old_k ** 2
    if new_radius_square < 1.0:
        x[k] = x_new_k
        old_radius_square = new_radius_square

    hist_data.append(math.sqrt(old_radius_square))

bins = np.linspace(0.0, 1.0, 1000)
plt.hist(hist_data, bins = 1000, density=True, label='hist')
plt.plot(bins, [20 * r**19 for r in bins], label='20r^19')
plt.title("B1")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc='upper left')
plt.grid(True)
plt.savefig(f'markov_{d}d_sphere.png') 
plt.show()