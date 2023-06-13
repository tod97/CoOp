import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np

colors = ['green', 'blue', 'red', 'yellow', 'orange']
legend = ['1-ctx 16-prompts', '2-ctx 8-prompts', '4-ctx 4-prompts', '8-ctx 2-prompts', '16-ctx 1-prompt']
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

   for i in range(0, int(len(filtered_data)/15)):
      y_data = []
      for shot in range(len(x_data)):
         index = shot*int(len(filtered_data)/5) + i*3
         avg_acc = (accuracy[index] + accuracy[index + 1] + accuracy[index + 2]) / 3
         y_data.append(avg_acc)
      #print(y_data, colors[i])
      plt.plot(x_data, y_data, markersize=3, color=colors[i])

   plt.grid()
   plt.title(dataset)
   plt.xlabel('Shots')
   plt.ylabel('Accuracy')
   plt.xticks(x_data)
   plt.legend([legend[i] for i in range(len(legend)-int(len(filtered_data)/15), len(legend))])
   plt.get_current_fig_manager().set_window_title(dataset)
   plt.show()