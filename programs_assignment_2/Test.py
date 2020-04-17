def f1(p, q, r):
    return (q or r if p else True) or (q if p else True)

print('p    q    r    F')
for p in [True, False]:
    for q in [True, False]:
        for r in [True, False]:
            print(p, q, r, f1(p, q, r))

def f2(p, q):
    return (p if q else True) if p else True


print('p    q    F')
for p in [True, False]:
    for q in [True, False]:
            print(p, q, f2(p, q))

def f3(p, q, r):
    return ((r if p else True) if (q if p else True) else True) if ((r if q else True) if p else True) else True

print('p    q    r    F')
for p in [True, False]:
    for q in [True, False]:
        for r in [True, False]:
            print(p, q, r, f3(p, q, r))