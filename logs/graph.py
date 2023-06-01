import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np

datasets = ['caltech101', 'eurosat', 'oxford_pets']

for dataset in datasets:
    with open(dataset + '.csv', 'r') as file:
        reader = csv.reader(file, delimiter=' ')
        data = list(reader)

    names = [row[0] for row in data]
    total = [int(row[1]) if row[1] != '' else 0 for row in data]
    correct = [float(row[2]) if row[2] != '' else 0 for row in data]
    accuracy = [float(row[3]) if row[3] != '' else 0 for row in data]
    error = [float(row[4]) if row[4] != '' else 0 for row in data]
    macro_f1 = [float(row[5]) if row[5] != '' else 0 for row in data]


    x1_data = []
    for i in range(6):
        x1_data += [(2**i) * [2**i]]
    x1_data = [el for sublist in x1_data for el in sublist]
    x2_data = [1,2,4,8,16,32]

    for seed in range(0, 3):
        y1_indexes = list([1+(seed*2)] + [i+seed*2+seed for i in range(7, 9)] + [i+seed*4+seed for i in range(16, 20)] + [i+seed*8+seed for i in range(31, 39)] + [i+seed*16+seed for i in range(58, 74)] + [i+seed*32+seed for i in range(109, 141)])
        y1_data = [accuracy[i] for i in y1_indexes]
        y2_indexes = list([(seed*2)] + [6+seed*2+seed] + [15+seed*4+seed] + [30+seed*8+seed] + [57+seed*16+seed] + [108+seed*32+seed])
        y2_data = [accuracy[i] for i in y2_indexes]

        plt.plot(x1_data, y1_data,'o' ,markersize=4, color = 'blue')
        plt.plot(x2_data, y2_data, markersize=3, color='green')

        plt.grid()
        plt.title(dataset + ' - Seed ' + str(seed+1))
        plt.xlabel('Prompts')
        plt.xticks(x2_data, x2_data)
        plt.ylabel('Accuracy')
        plt.show()