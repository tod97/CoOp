import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np

colors = ['green', 'blue', 'red', 'yellow', 'orange']
#datasets = ['caltech101', 'dtd', 'eurosat', 'fgvc_aircraft', 'food101', 'oxford_flowers', 'oxford_pets', 'stanford_cars', 'sun397', 'ucf101']
datasets = ['caltech101']

with open('full.csv', 'r') as file:
   reader = csv.reader(file, delimiter=' ')
   data = list(reader)

for dataset in datasets:

   filtered_data = [item for item in data if dataset in item[0]]

   names = [row[0] for row in filtered_data]
   total = [int(row[1]) if row[1] != '' else 0 for row in filtered_data]
   correct = [float(row[2]) if row[2] != '' else 0 for row in filtered_data]
   accuracy = [float(row[3]) if row[3] != '' else 0 for row in filtered_data]
   error = [float(row[4]) if row[4] != '' else 0 for row in filtered_data]
   macro_f1 = [float(row[5]) if row[5] != '' else 0 for row in filtered_data]

   x_data = [1, 2, 4, 8, 16]
   for i in range(0, 5):
      y_data = []
      for shot in range(len(x_data)):
         index = shot*15 + i*3
         avg_acc = (accuracy[index] + accuracy[index + 1] + accuracy[index + 2]) / 3
         y_data.append(avg_acc)
      plt.plot(x_data, y_data, markersize=3, color=colors[i])

   plt.grid()
   plt.title(dataset)
   plt.xlabel('Prompts')
   plt.ylabel('Accuracy')
   plt.xticks(x_data)
   plt.show()