import numpy as np

# входные данные
a = np.random.randint(-5, 5, (3, 3))
b = np.random.randint(-5, 5, (3, 3))

# задание 1a
print((a<0).sum())

# задание 1b
print(np.allclose(a, -a.T))
print(a, '\n', -a.T)

# задание 1c
print((a==-1).sum())

# задание 1e
print(a[np.triu_indices_from(a, k=1)].sum())

# задание 3

