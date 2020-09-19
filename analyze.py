import numpy as np
import matplotlib.pyplot as plt

from preprocessing import load_data
from transforms import *

data_file = './data/Land_and_Ocean_complete.txt'
# data_file = './data/georgia-(state)-TAVG-Trend.txt'
# data_file = './data/southern-hemisphere-TAVG-Trend.txt'

data_wrapper = load_data(data_file)

time = 'Years'
data = np.mean(data_wrapper.get_data_matrix(), axis=1)

# time = 'Months'
# data = data_wrapper.get_data_matrix().flatten()

data = [d for d in data if not np.isnan(d)]
deg = 5
l = 15
ts = (None, smooth, running_average_with_custom_length(l), polyfit(1), polyfit(deg), composite(shift(2), safe_log, polyfit(deg)), composite(shift(2), ratios, remove_outliers), composite(shift(2), polyfit(deg), ratios, remove_outliers))
names = ("Temperature in C (shifted down by 8.61)", 'Smoothed', 'Running Average with Length ' + str(l), 'Linear Regression', 'Polyfit of Degree ' + str(deg), 'Polyfit of Log', 'Ratios', 'Ratios on Polyfit')

s = (3, 3)
fig, axs = plt.subplots(s[0], s[1])

for i in range(len(ts)):
    a = axs[i // s[1]][i % s[1]]
    a.set_xlabel(time + " since " + str(data_wrapper.base_year))
    try:
        ylabel = names[i] if names[i] is not None else 'No Label'
    except IndexError:
        ylabel = 'No Label'
    a.set_ylabel(ylabel)
    d = ts[i](data) if ts[i] != None else data
    a.plot(d)
    print('Mean of', ylabel, np.mean(d))

best_fit_degree = deg
ys = data
p = np.polyfit(list(range(len(ys))), ys, best_fit_degree)
i = len(ts)
a = axs[i // s[1]][i % s[1]]
a.plot([sum([(i ** j) * p[best_fit_degree - j] for j in range(best_fit_degree + 1)]) for i in range(2*len(ys))])
a.set_xlabel(time + " since " + str(data_wrapper.base_year))
a.set_ylabel("Polyfit with Predictions")

mng = plt.get_current_fig_manager()
mng.window.state("zoomed")

plt.show()
