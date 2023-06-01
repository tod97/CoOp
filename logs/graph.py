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


    fig, axs = plt.subplots(1, 3)

    x1_data = []
    for i in range(6):
        x1_data += [(2**i) * [2**i]]
    x1_data = [el for sublist in x1_data for el in sublist]
    x2_data = [1, 2, 4, 8, 16, 32]

    for seed in range(0, 3):
        y1_indexes = list([1+(seed*2)] + [i+seed*2+seed for i in range(7, 9)] + [i+seed*4+seed for i in range(16, 20)] + [i+seed*8+seed for i in range(31, 39)] + [i+seed*16+seed for i in range(58, 74)] + [i+seed*32+seed for i in range(109, 141)])
        y1_data = [accuracy[i] for i in y1_indexes if accuracy[i] != 0]
        y2_indexes = list([(seed*2)] + [6+seed*2+seed] + [15+seed*4+seed] + [30+seed*8+seed] + [57+seed*16+seed] + [108+seed*32+seed])
        y2_data = [accuracy[i] for i in y2_indexes if accuracy[i] != 0]

        x1_data = [x1_data[i] for i in range(len(y1_data))]
        x2_data = [x2_data[i] for i in range(len(y2_data))]

        # Aggiungi i grafici agli assi corrispondenti
        axs[seed].plot(x1_data, y1_data, 'o', markersize=4, color='blue')
        axs[seed].plot(x2_data, y2_data, markersize=3, color='green')

        axs[seed].grid()
        axs[seed].set_title(dataset + ' - Seed ' + str(seed+1))
        axs[seed].set_xlabel('Prompts')
        axs[seed].set_xticks(x2_data)
        axs[seed].set_ylabel('Accuracy')

    # Mostra la figura con tutti i grafici
    plt.tight_layout()
    plt.show()
