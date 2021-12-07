
import matplotlib.pyplot as plt
import numpy as np

import sys

plot_data_bytes = []
plot_data_bits = []
plot_data_histo = []

file1 = open('mm_p_s', 'r')
count = 0
for line in file1.readlines():
    print("Line {}: {}".format(count, line.strip()))
    segments = line.split("###")
    
    data = {} # Empty dictionary
    for segment in segments:
        temp = segment.split(":")
        data[temp[0].strip()] = float(temp[1].strip())
        
    plot_data_bytes.append((
        data["Bytes"], 
        data["Overwrites"]/data["Bytes"]*100
    ))
    
    count += 1
    
file2 = open('mm_bit_p_s', 'r')
count = 0
for line in file2.readlines():
    print("Line {}: {}".format(count, line.strip()))
    segments = line.split("###")
    
    data = {} # Empty dictionary
    for segment in segments:
        temp = segment.split(":")
        data[temp[0].strip()] = float(temp[1].strip())
        
    plot_data_bits.append((
        data["Bits"], 
        data["Overwrites"]/data["Bits"]*100
    ))
    
    count += 1


for x in range(10):
    plot_data_histo.append([x, 0, 0])

for data in plot_data_bytes:
    if data[1] >= 0 and data[1] < 10:
        plot_data_histo[0][1] += 1
    elif data[1] >= 10 and data[1] < 20:
        plot_data_histo[1][1] += 1
    elif data[1] >= 20 and data[1] < 30:
        plot_data_histo[2][1] += 1
    elif data[1] >= 30 and data[1] < 40:
        plot_data_histo[3][1] += 1
    elif data[1] >= 40 and data[1] < 50:
        plot_data_histo[4][1] += 1
    elif data[1] >= 50 and data[1] < 60:
        plot_data_histo[5][1] += 1
    elif data[1] >= 60 and data[1] < 70:
        plot_data_histo[6][1] += 1
    elif data[1] >= 70 and data[1] < 80:
        plot_data_histo[7][1] += 1
    elif data[1] >= 80 and data[1] < 90:
        plot_data_histo[8][1] += 1
    elif data[1] >= 90 and data[1] <= 100:
        plot_data_histo[9][1] += 1
    else:
        print("Warning: Overwrite (Byte) section: {}", data)
        
for data in plot_data_bits:
    if data[1] >= 0 and data[1] < 10:
        plot_data_histo[0][2] += 1
    elif data[1] >= 10 and data[1] < 20:
        plot_data_histo[1][2] += 1
    elif data[1] >= 20 and data[1] < 30:
        plot_data_histo[2][2] += 1
    elif data[1] >= 30 and data[1] < 40:
        plot_data_histo[3][2] += 1
    elif data[1] >= 40 and data[1] < 50:
        plot_data_histo[4][2] += 1
    elif data[1] >= 50 and data[1] < 60:
        plot_data_histo[5][2] += 1
    elif data[1] >= 60 and data[1] < 70:
        plot_data_histo[6][2] += 1
    elif data[1] >= 70 and data[1] < 80:
        plot_data_histo[7][2] += 1
    elif data[1] >= 80 and data[1] < 90:
        plot_data_histo[8][2] += 1
    elif data[1] >= 90 and data[1] <= 100:
        plot_data_histo[9][2] += 1
    else:
        print("Warning: Overwrite (Bit) section: {}", data)
        

data_O_counts_bytes = [y[1] for y in plot_data_histo]
data_O_counts_bits = [y[2] for y in plot_data_histo]
X = np.arange(10)
fig = plt.figure(dpi=100, figsize=(14, 7))
ax = fig.add_axes([0.1,0.1,0.8,0.8])
plt.style.use('ggplot')

ax.bar(X - 0.15, data_O_counts_bytes, width = 0.3, label="Byte Level")
ax.bar(X + 0.15, data_O_counts_bits, width = 0.3, label="Bit Level")
    
plt.legend(loc="upper left")
plt.title('Tcpdump (Approx. 13hr+, ' +str(count) + ' data points)')
plt.xlabel('Buckets')
plt.ylabel('Counts')
plt.xticks(np.arange(10), ['0~10%', '10~20%', '20~30%', '30~40%', '40~50%', '50~60%', '60~70%', '70~80%', '80~90%', '90~100%'])
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show()
plt.savefig("mask_percentages_compare.png")
    
