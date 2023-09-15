import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook


d= []

with open("averages.txt", 'r') as f:
    for line in f.readlines():
        if not line: continue

        d.append(list(eval(line)))

d = np.array(d)

averages = d.mean(axis= 1)
stds = d.std(axis=1)
t = np.arange(len(d) * 100, step=100)

fig, ax = plt.subplots(1)


ax.stem(t, averages, label='Mean')
ax.set_xlabel('attempts')
ax.set_ylabel('score')
ax.legend(loc='lower right')
plt.show()