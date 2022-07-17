import csv
with open('departments.csv', newline='') as csvfile:
    data = csv.reader(csvfile,delimiter=' ', quotechar='|')
    for row in data:
        print(' '.join(row))

import matplotlib.pyplot as plt
plt.plot(csvfile)
plt.show()


