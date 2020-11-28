import os
import sys
import csv
import itertools
import functools
import matplotlib.pyplot as plt


time_name = "Time"


with open(os.path.join(sys.path[0], 'sim_out.csv'), 'r') as csvfile:

    datareader = csv.DictReader(csvfile)
    fulldata = [i for i in datareader]
    

    fulldata_inv = {key:[item[key] for item in fulldata]
         for key in list(functools.reduce(
             lambda x, y: x.union(y),
             (set(dicts.keys()) for dicts in fulldata)
         ))
      }
    
    keys = list(fulldata_inv.keys())

    times = fulldata_inv[time_name]
    plot_data = [(times, fulldata_inv[name]) if name is not time_name else () for name in keys ]
    plt.plot(*[i for i in itertools.chain.from_iterable(plot_data)])
    plt.show()