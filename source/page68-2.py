# $ cd ~/.matplotlib
# $ nano matplotlibrc
# backend : TkAgg

from matplotlib import pyplot as plt

plt.plot([10,5,2,4], color='green', label='line 1', linewidth=5)

plt.ylabel('y', fontsize=40)
plt.xlabel('x', fontsize=40)

plt.axis([0, 3, 0, 15])

plt.show()

# figure 객체로 초기화하고, axis 객체를 추가한다
fig = plt.figure(figsize=(10,10) )
ax = fig.add_subplot(111)
ax.set_xlabel('x', fontsize=40 )
ax.set_ylabel('y', fontsize=40 )
fig.suptitle('figure', fontsize=40 )
ax.plot( [10,5,2,4], color='green', label='line 1', linewidth=5)

fig.savefig('figure.png')  # 파일 저장


