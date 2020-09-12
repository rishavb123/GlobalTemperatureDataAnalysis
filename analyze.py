import numpy as np
import matplotlib.pyplot as plt

from preprocessing import load_data
from transforms import *

data_wrapper = load_data('./data/Land_and_Ocean_complete.txt')

data = np.mean(data_wrapper.get_data_matrix(), axis=1)
print(derivative)
deg = 0
ts = (None, polyfit(deg), composite(polyfit(deg), derivative))
names = ('', 'Polyfit of ', 'Derivative of polyfit of ')

s = (2, 2)
fig, axs = plt.subplots(s[0], s[1], figsize=(16, 9))

for i in range(len(ts)):
    a = axs[i // s[0]][i % s[0]]
    a.set_xlabel("Years since " + str(data_wrapper.base_year))
    ylabel = names[i] + "Temperature in C (shifted down by 8.61)"
    a.set_ylabel(ylabel)
    d = ts[i](data) if ts[i] != None else data
    a.plot(d)
    print('Mean of', ylabel, np.mean(d))

plt.show()