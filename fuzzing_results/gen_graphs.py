#!/usr/bin/python

import sys
import os
import matplotlib.pyplot as plt
import numpy as np

def main(argv):
  rb_hit_file = open(argv[0])
  rb_hit_lines = rb_hit_file.readlines()

  mutations = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11+12', '13', '14', '15', '16']
  totals = []
  hits = []

  for i in reversed(range(len(rb_hit_lines))):
    if "Finished" in rb_hit_lines[i]: 
      for j in range(17):
        if j == 12:
          continue
        hit = int(rb_hit_lines[i + j*3 + 2].split(' ')[-1])
        total = int(rb_hit_lines[i + j*3 + 3].split(' ')[-1])
        hits.append(hit)
        totals.append(total)
      break

  fig = plt.figure(dpi=100, figsize=(14, 7))
  ax = fig.add_axes([0.1,0.1,0.8,0.8])
  plt.style.use('ggplot')
  index = np.arange(16)
  ax.bar(index - 0.10, totals, width = 0.2, label="Total attempts")
  ax.bar(index + 0.10, hits, width = 0.2, label="Rare branch hits")
  plt.legend(loc="upper right")
  plt.title(argv[1] + ' (Approx. 12hr+)')
  plt.xlabel('Havoc Cases')
  plt.ylabel('Counts')
  plt.xticks(np.arange(16), mutations)
  plt.tick_params(axis='both', which='major', labelsize=10)
  plt.savefig(argv[1]+"-cases.png")

  g2_mutations = ['Bit OW', 'Byte OW', 'Word OW', 'DWord OW', 'Delete', 'Insert', 'Rand OW']
  g2_totals = [totals[0],
               totals[1]+totals[4]+totals[5]+totals[10],
               totals[2]+totals[6]+totals[7],
               totals[3]+totals[8]+totals[9],
               totals[11],
               totals[12]+totals[15],
               totals[13]+totals[14]]
  g2_hits = [hits[0],
               hits[1]+hits[4]+hits[5]+hits[10],
               hits[2]+hits[6]+hits[7],
               hits[3]+hits[8]+hits[9],
               hits[11],
               hits[12]+hits[15],
               hits[13]+hits[14]]

  fig = plt.figure(dpi=100, figsize=(14, 7))
  ax = fig.add_axes([0.1,0.1,0.8,0.8])
  plt.style.use('ggplot')
  index = np.arange(7)
  ax.bar(index - 0.10, g2_totals, width = 0.2, label="Total attempts")
  ax.bar(index + 0.10, g2_hits, width = 0.2, label="Rare branch hits")
  plt.legend(loc="upper right")
  plt.title(argv[1] + ' (Approx. 12hr+)')
  plt.xlabel('Mutations')
  plt.ylabel('Counts')
  plt.xticks(np.arange(7), g2_mutations)
  plt.tick_params(axis='both', which='major', labelsize=10)
  plt.savefig(argv[1]+"-mutations.png")


if __name__ == "__main__":
  main(sys.argv[1:])
