import numpy as np

# входные данные
a = np.random.randint(-5, 5, (3, 3))
b = np.random.randint(-5, 5, (3, 3))
print('Matrix a: \n', a, '\n')
print('Matrix b: \n', b, '\n')

# задание 1a
print((a<0).sum())

# задание 1b
print(np.allclose(a, -a.T))
print(-a.T)

# задание 1c
print((a==-1).sum())

# задание 1e
print(a[np.triu_indices_from(a, k=1)].sum())

# задание 3
max_a = a.max()
max_b = b.max()
print('Количество максимумов в a: ', (a==max_a).sum())
print('Количество максимумов в b: ', (b==max_b).sum())
positions = set()
positions_a = np.argwhere(a == max_a)
positions_b = np.argwhere(b == max_b)
positions.update(map(tuple, positions_a))
positions.update(map(tuple, positions_b))
print('Количество позиций, на которых стоит максимум хотя бы в одной из матриц:', len(positions))

# задание 4
arr = np.arange(1, 17)
print(arr.reshape(4, 4))

# задание 5
vec = np.arange(1, 4)
matrix = np.zeros((3, 3), dtype=int)
np.fill_diagonal(matrix, vec)
np.fill_diagonal(np.fliplr(matrix), vec)
print(matrix)

# задание 6
n = 5
vector = np.arange(1, 6)
print(np.repeat(vector, n))

# задание 7
v = np.array([1, 10, 5, -10, 0, 5, 8, 9, 2])
print(v)
min_value = np.min(v)
v[v != 0] = min_value
print(v)