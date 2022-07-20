import numpy as np
import matplotlib.pyplot as plt

total_walks = []
for t in range(10):
    rand_walks = [0]
    for s in range(100):
        step = rand_walks[-1]
        dice = np.random.randint(1,7)
        if dice <=2:
            step = max(0,step-1)
        elif dice <=5:
            step += 1
        else:
            step = step+np.random.randint(1,7)
        if np.random.rand() <= 0.001:
            step = 0
        rand_walks.append(step)
    total_walks.append(rand_walks)

plt.plot(total_walks)
plt.show()