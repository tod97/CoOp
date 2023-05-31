import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np

seed = 0

with open('eurosat.csv', 'r') as file:
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

y1_data = [accuracy[1], accuracy[7], accuracy[8], accuracy[16], accuracy[17], accuracy[18], accuracy[19], accuracy[31], accuracy[32], accuracy[33], accuracy[34], accuracy[35], accuracy[36], accuracy[37], accuracy[38], accuracy[58], accuracy[59], accuracy[60], accuracy[61], accuracy[62], accuracy[63], accuracy[64], accuracy[65], accuracy[66], accuracy[67], accuracy[68], accuracy[69], accuracy[70], accuracy[71], accuracy[72], accuracy[73], accuracy[109], accuracy[110], accuracy[111], accuracy[112], accuracy[113], accuracy[114], accuracy[115], accuracy[116], accuracy[117], accuracy[118], accuracy[119], accuracy[120], accuracy[121], accuracy[122], accuracy[123], accuracy[124], accuracy[125], accuracy[126], accuracy[127], accuracy[128], accuracy[129], accuracy[130], accuracy[131], accuracy[132], accuracy[133], accuracy[134], accuracy[135], accuracy[136], accuracy[137], accuracy[138], accuracy[139], accuracy[140]]
y2_data = [accuracy[0], accuracy[6], accuracy[15], accuracy[30], accuracy[57], accuracy[108]]


# Visualizzazione
#x1_data.sort()
#y1_data.sort()
#x2_data.sort()
#y2_data.sort()


plt.plot(x1_data, y1_data,'o' ,markersize=4, color = 'black')
plt.plot(x2_data, y2_data, markersize=3, color='green')

plt.grid()
plt.title('Data points')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()