
import matplotlib.pyplot as plt
import numpy as np

import sys

fig = plt.figure(dpi=100, figsize=(14, 7))
ax = fig.add_axes([0.1,0.1,0.8,0.8])
plt.style.use('ggplot')

for filename in sys.argv[1:]:

    plot_data_x = []
    plot_data_y = []
    
    file1 = open(filename, 'r')
    count = 0
    first = True
    base_timestamp = 0
    for line in file1.readlines():

        print("Line {}: {}".format(count, line.strip()))
        segments = line.split(", ")
        
        if first:
            first = False
            base_timestamp = float(segments[0].strip())

        plot_data_x.append(float(segments[0].strip())-base_timestamp)
        plot_data_y.append(float(segments[1].strip()))
        
        count += 1
        

    plt.plot(plot_data_x, plot_data_y, label=filename)
    
plt.legend(loc="upper right")
plt.title('Path Coverage over Time')
plt.xlabel('Time')
plt.ylabel('Coverage')
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show()
plt.savefig("coverage.png")
    