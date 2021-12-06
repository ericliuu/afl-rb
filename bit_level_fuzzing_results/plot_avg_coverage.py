
import matplotlib.pyplot as plt
import numpy as np
import argparse

import sys

parser = argparse.ArgumentParser()
parser.add_argument("--base_cov",
                    help="baseline branch_coverage.log file(s) that will be averaged and plotted",
                    nargs='+')
parser.add_argument("--bit_cov",
                    help="bit level mask branch_coverage.log file(s) that will be averaged and plotted",
                    nargs='+')
args = parser.parse_args()

fig = plt.figure(dpi=100, figsize=(14, 7))
ax = fig.add_axes([0.1,0.1,0.8,0.8])
plt.style.use('ggplot')

plot_data_baseline_x = []
plot_data_bit_x = []
plot_data_baseline_y = []
plot_data_bit_y = []
plot_data_counts = []

for filename in args.base_cov:

    plot_data_x = []
    plot_data_y = []
    
    file1 = open(filename, 'r')
    count = 0
    first = True
    base_timestamp = 0
    for line in file1.readlines():

#        print("Line {}: {}".format(count, line.strip()))
        segments = line.split(", ")
        
        if first:
            first = False
            base_timestamp = float(segments[0].strip())

        plot_data_x.append(float(segments[0].strip())-base_timestamp)
        plot_data_y.append(float(segments[1].strip()))
        
        count += 1

    plot_data_baseline_x.append(plot_data_x)
    plot_data_baseline_y.append(plot_data_y)
    plot_data_counts.append(count)

for filename in args.bit_cov:

    plot_data_x = []
    plot_data_y = []
    
    file1 = open(filename, 'r')
    count = 0
    first = True
    base_timestamp = 0
    for line in file1.readlines():

#        print("Line {}: {}".format(count, line.strip()))
        segments = line.split(", ")
        
        if first:
            first = False
            base_timestamp = float(segments[0].strip())

        plot_data_x.append(float(segments[0].strip())-base_timestamp)
        plot_data_y.append(float(segments[1].strip()))
        
        count += 1

    plot_data_bit_x.append(plot_data_x)
    plot_data_bit_y.append(plot_data_y)
    plot_data_counts.append(count)

# find the lowest common number of elements and drop all the remaining excess
min_count = np.amin(np.array(plot_data_counts))
plot_data_bit_x = [sublist[:min_count] for sublist in plot_data_bit_x]
plot_data_bit_y = [sublist[:min_count] for sublist in plot_data_bit_y]
plot_data_baseline_x = [sublist[:min_count] for sublist in plot_data_baseline_x]
plot_data_baseline_y = [sublist[:min_count] for sublist in plot_data_baseline_y]

# We dump a timestamp every 5 minutes, so lets find out how many hours to use for our x-axis
num_hours = float(min_count) / 12.0

# convert to numpy arrays, also lets just take the first element of the x-axis to normalize
plot_data_bit_x = np.array(plot_data_bit_x)[0]
plot_data_baseline_x = np.array(plot_data_baseline_x)[0]
plot_data_bit_y = np.array(plot_data_bit_y)
plot_data_baseline_y = np.array(plot_data_baseline_y)

# normalize x axis into hours
plot_data_bit_x *= (num_hours / plot_data_bit_x.max())
plot_data_baseline_x *= (num_hours / plot_data_baseline_x.max())

# Get standard deviations
plot_data_bit_y_std = plot_data_bit_y.std(axis=0)
plot_data_baseline_y_std = plot_data_baseline_y.std(axis=0)

# Average y-axis plots
plot_data_bit_y = plot_data_bit_y.mean(axis=0)
plot_data_baseline_y = plot_data_baseline_y.mean(axis=0)

# plot averages 
plt.plot(plot_data_baseline_x, plot_data_baseline_y, label='Baseline', color='Blue')
plt.plot(plot_data_bit_x, plot_data_bit_y, label='Bit level mask', color='Orange')

# plot standard deviations
plt.fill_between(plot_data_baseline_x, plot_data_baseline_y-plot_data_baseline_y_std, plot_data_baseline_y+plot_data_baseline_y_std, color='Blue', alpha=0.4)
plt.fill_between(plot_data_bit_x, plot_data_bit_y-plot_data_bit_y_std, plot_data_bit_y+plot_data_bit_y_std, color='Orange', alpha=0.4)

plt.legend(loc="upper right")
plt.title('Branch Coverage over Time')
plt.xlabel('Time (Hours)')
plt.ylabel('Basic Block Transitions Covered')
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show()
plt.savefig("coverage.png")
    
