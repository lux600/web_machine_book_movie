import numpy as np
from matplotlib import pyplot as plt

fig = plt.figure( figsize=(10,10) )
ax = fig.add_subplot(111)
r = np.arange(0., 10., 0.3)
p1, = ax.plot(r, r, 'r--', label='line 1', linewidth=10)  # 문자포맷 r-- 빨간색 사각형
p2, = ax.plot(r, r**0.5, 'bs', label='line 2', linewidth=10) # bs 파란색 정사각형
p3, = ax.plot(r, np.sin(r), 'g^', label='line 3', markersize =10) # g^ 녹색 삼각형

handeles, labels = ax.get_legend_handles_labels()
ax.legend(handeles, labels, fontsize =40)
ax.set_xlabel('x', fontsize =40)
ax.set_ylabel('y', fontsize =40)

fig.suptitle('figure 1', fontsize =40)
fig.savefig('figure_multiplelines.png')