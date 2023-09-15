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

# Nsteps length arrays empirical means and standard deviations of both
# populations over time
mu1 = averages
sigma1 = d.std(axis=1)

# plot it!
fig, ax = plt.subplots(1)
ax.plot(t, mu1, lw=2, label='Mean')
ax.fill_between(t, mu1+sigma1, mu1-sigma1, facecolor='C0', alpha=0.4, label='Standard Deviation')
ax.set_title(r'Mean of 10 training repetitions ')
ax.legend(loc='lower right')
ax.set_xlabel('attempts')
ax.set_ylabel('score')
ax.grid()

plt.show()
