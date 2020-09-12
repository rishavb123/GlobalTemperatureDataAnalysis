import numpy as np
import matplotlib.pyplot as plt

from preprocessing import load_data
from transforms import *

data = load_data('./data/Land_and_Ocean_complete.txt')

means = np.mean(data.get_data_matrix(), axis=1)

t = composite(shift(2), derivative, rec_remove_outliers)
d = t(means)
print(np.mean(d))

plt.plot(d)
# plt.plot(means)
plt.show()