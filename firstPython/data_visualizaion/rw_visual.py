import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

print(rw.num_points)

point_numbers = range(rw.num_points)
print(point_numbers)

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)

ax.scatter(0, 0, c='green', edgecolor='none', s=20)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=20)
plt.show()