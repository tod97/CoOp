import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np

with open('log_data.csv', 'r') as file:
   reader = csv.reader(file)
   next(reader)
   data = list(reader)

names = [row[0] for row in data]
total = [int(row[1]) for row in data]
correct = [float(row[2], ) for row in data]
accuracy = [float(row[3]) for row in data]
error = [float(row[4]) for row in data]
macro_f1 = [float(row[5]) for row in data]

prefixes = {}
for i in range(len(names)):
   prefix = names[i].split("/seed")[0]
   if prefix.startswith("_"):
      prefix = prefix[1:]

   if prefix in prefixes:
      prefixes[prefix].append({'name': names[i], 'total': total[i], 'correct': correct[i], 'accuracy': accuracy[i], 'error': error[i], 'macro_f1': macro_f1[i]})
   else:
      prefixes[prefix] = [{'name': names[i], 'total': total[i], 'correct': correct[i], 'accuracy': accuracy[i], 'error': error[i], 'macro_f1': macro_f1[i]}]

width = 0.35
for key, value in prefixes.items():
   fig, axs = plt.subplots(2, 2, figsize=(8, 8))
   fig.suptitle(key)
   
   corrects_old = []
   accuracies_old = []
   errors_old = []
   macro_f1s_old = []
   names = []
   corrects = []
   accuracies = []
   errors = []
   macro_f1s = []
   
   for i in range(len(value)):
      if i % 2 == 0:
         names.append("seed_"+value[i]['name'].split("seed")[1])
         corrects_old.append(value[i]['correct'])
         accuracies_old.append(value[i]['accuracy'])
         errors_old.append(value[i]['error'])
         macro_f1s_old.append(value[i]['macro_f1'])
      else:
         corrects.append(value[i]['correct'])
         accuracies.append(value[i]['accuracy'])
         errors.append(value[i]['error'])
         macro_f1s.append(value[i]['macro_f1'])

   axs[0,0].set_title('Correct')
   axs[0,0].plot(names, corrects_old, 'b-o', label='old') 
   axs[0,0].plot(names, corrects, 'r-o', label='new')
   #axs[0,0].bar(np.arange(len(names)) - width/2, corrects_old, width, label='old')
   #axs[0,0].bar(np.arange(len(names)) + width/2, corrects, width, label='new')
   axs[0,0].legend()

   axs[0,1].set_title('Accuracy')
   axs[0,1].plot(names, accuracies_old, 'b-o', label='old')
   axs[0,1].plot(names, accuracies, 'r-o',label='new')
   axs[0,1].legend()
   axs[0,1].yaxis.set_major_formatter(PercentFormatter())

   axs[1,0].set_title('Error')
   axs[1,0].plot(names, errors_old, 'b-o', label='old')
   axs[1,0].plot(names, errors, 'r-o',label='new')
   axs[1,0].legend()
   axs[1,0].yaxis.set_major_formatter(PercentFormatter())

   axs[1,1].set_title('Macro F1')
   axs[1,1].plot(names, macro_f1s_old, 'b-o', label='old')
   axs[1,1].plot(names, macro_f1s, 'r-o',label='new')
   axs[1,1].legend()
   axs[1,1].yaxis.set_major_formatter(PercentFormatter())

plt.tight_layout()
plt.show()