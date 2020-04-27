import random, math
import matplotlib.pyplot as plt

def V_sph(dim):
    return math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0)

V = 2
D = 200
data = [V]
for d in range(2, D + 1):
    x = [0.0] * (d - 1)
    delta = 0.1
    n_trials = 100000
    n_hits = 0
    old_radius_square = 0
    for i in range(n_trials):
        k = random.randint(0, d - 2)
        x_old_k = x[k]
        x_new_k = x_old_k + random.uniform(-delta, delta)
        new_radius_square = old_radius_square + x_new_k ** 2 - x_old_k ** 2
        z = random.uniform(-1.0, 1.0)
        if new_radius_square < 1.0:
            x[k] = x_new_k
            old_radius_square = new_radius_square
        if old_radius_square + z ** 2 < 1:
            n_hits += 1
    V *= 2 * n_hits / float(n_trials)
    data.append(V)

print(f'V_sph({D})={V}')
print(f'V_sph_anal({D})={V_sph(D)}')

bins = range(1, len(data) + 1)
plt.plot(bins, [V_sph(r) for r in bins], color='r', label='V_sph analytical')
plt.plot(bins, data, color='b', label='V_sph monte carlo')
plt.title("C1")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc='upper right')
plt.grid(True)
plt.yscale('log')
plt.savefig(f'markov_{d}d_sphere.png') 
plt.show()