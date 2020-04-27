import random, math

d = 200
x = [0.0] * (d - 1)
delta = 0.1
n_trials = 2000000
n_hits = 0
old_radius_square = 0
hist_data = []
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
    
def V_sph(dim):
    return math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0)

for t in range(1, 20):
    print(t, V_sph(t))

print(f'Q({d})=', 2 * n_hits / float(n_trials))
