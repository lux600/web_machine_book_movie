import numpy as np
from matplotlib import pyplot as plt

colors = ['b', 'c', 'y', 'm', 'r']

fig = plt.figure(figsize=(10,10))

ax = fig.add_subplot(111)
ax.scatter(np.random.random(10), np.random.random(10), marker='x' , color=colors[0])

p1 = ax.scatter(np.random.random(10), np.random.random(10), marker='x' , color=colors[0], s=50)
p2 = ax.scatter(np.random.random(10), np.random.random(10), marker='o' , color=colors[1], s=50)
p3 = ax.scatter(np.random.random(10), np.random.random(10), marker='o' , color=colors[2], s=50)

ax.legend((p1,p2,p3), ('points 1','points 2','points 3'), fontsize=20)
ax.set_xlabel('x', fontsize=40)
ax.set_ylabel('y', fontsize=40)

fig.savefig('figure_scatterplot.png')