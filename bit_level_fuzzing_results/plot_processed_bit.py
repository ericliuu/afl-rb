
import matplotlib.pyplot as plt
import numpy as np

import sys

plot_data = []
plot_data_histo = []

file1 = open(sys.argv[1], 'r')
count = 0
for line in file1.readlines():
    print("Line {}: {}".format(count, line.strip()))
    segments = line.split("###")
    
    data = {} # Empty dictionary
    for segment in segments:
        temp = segment.split(":")
        data[temp[0].strip()] = float(temp[1].strip())
        
    plot_data.append((
        data["Bits"], 
        data["Overwrites"]/data["Bits"]*100, 
        data["Deletes"]/data["Bits"]*100, 
        data["Inserts"]/data["Bits"]*100, 
    ))
    
    count += 1


# 0: 000~009.99%
# 1: 010~019.99%
# 2: 020~029.99%
# 3: 030~039.99%
# 4: 040~049.99%
# 5: 050~059.99%
# 6: 060~069.99%
# 7: 070~079.99%
# 8: 080~089.99%
# 9: 090~100.00%
for x in range(10):
    plot_data_histo.append([x, 0, 0, 0])

for data in plot_data:
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
        print("Warning: Overwrite section: {}", data)
        
    
    if data[2] >= 0 and data[2] < 10:
        plot_data_histo[0][2] += 1
    elif data[2] >= 10 and data[2] < 20:
        plot_data_histo[1][2] += 1
    elif data[2] >= 20 and data[2] < 30:
        plot_data_histo[2][2] += 1
    elif data[2] >= 30 and data[2] < 40:
        plot_data_histo[3][2] += 1
    elif data[2] >= 40 and data[2] < 50:
        plot_data_histo[4][2] += 1
    elif data[2] >= 50 and data[2] < 60:
        plot_data_histo[5][2] += 1
    elif data[2] >= 60 and data[2] < 70:
        plot_data_histo[6][2] += 1
    elif data[2] >= 70 and data[2] < 80:
        plot_data_histo[7][2] += 1
    elif data[2] >= 80 and data[2] < 90:
        plot_data_histo[8][2] += 1
    elif data[2] >= 90 and data[2] <= 100:
        plot_data_histo[9][2] += 1
    else:
        print("Warning: Delete section: {}", data)
        
    
    if data[3] >= 0 and data[3] < 10:
        plot_data_histo[0][3] += 1
    elif data[3] >= 10 and data[3] < 20:
        plot_data_histo[1][3] += 1
    elif data[3] >= 20 and data[3] < 30:
        plot_data_histo[2][3] += 1
    elif data[3] >= 30 and data[3] < 40:
        plot_data_histo[3][3] += 1
    elif data[3] >= 40 and data[3] < 50:
        plot_data_histo[4][3] += 1
    elif data[3] >= 50 and data[3] < 60:
        plot_data_histo[5][3] += 1
    elif data[3] >= 60 and data[3] < 70:
        plot_data_histo[6][3] += 1
    elif data[3] >= 70 and data[3] < 80:
        plot_data_histo[7][3] += 1
    elif data[3] >= 80 and data[3] < 90:
        plot_data_histo[8][3] += 1
    elif data[3] >= 90 and data[3] <= 100:
        plot_data_histo[9][3] += 1
    else:
        print("Warning: Insert section: {}", data)
        


data_O_counts = [y[1] for y in plot_data_histo]
data_D_counts = [y[2] for y in plot_data_histo]
data_I_counts = [y[3] for y in plot_data_histo]
data_total_count = np.add(data_O_counts, data_D_counts)
data_total_count = np.add(data_total_count, data_I_counts)
X = np.arange(10)
fig = plt.figure(dpi=100, figsize=(14, 7))
ax = fig.add_axes([0.1,0.1,0.8,0.8])
plt.style.use('ggplot')

if ("-o" in sys.argv):
    ax.bar(X - 0.30, data_O_counts, width = 0.2, label="Overwrite counts")
if ("-d" in sys.argv):
    ax.bar(X - 0.10, data_D_counts, width = 0.2, label="Delete counts")
if ("-i" in sys.argv):
    ax.bar(X + 0.10, data_I_counts, width = 0.2, label="Insert counts")
if ("-total" in sys.argv):
    ax.bar(X + 0.3, data_total_count, color="black", width = 0.2, label="Total counts")

plt.legend(loc="upper right")
plt.title('Test (Approx. -hr+, - data points)')
plt.xlabel('Buckets')
plt.ylabel('Counts')
plt.xticks(np.arange(10), ['0~10%', '10~20%', '20~30%', '30~40%', '40~50%', '50~60%', '60~70%', '70~80%', '80~90%', '90~100%'])
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show()
plt.savefig("mask_percentages_bit.png")
    
