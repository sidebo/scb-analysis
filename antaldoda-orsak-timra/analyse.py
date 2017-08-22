#!/usr/bin/env python3

''' This script reads SCB death cause data in Timraa municipality in csv format
    and analyses it.

    Example use:
      simply do "python analyse.py"


    Prerequisities: none except python


    @ Edvin Sidebo, edvin.sidebo@cern.ch

    '''

import argparse
import sys
import pprint
# import numpy
# import glob
# import random
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd

g_DEBUG = True
g_inputFile = "HS0301A1.csv"
g_nCategories = 3 # nr of categories (cause of death, age category, sex...)
g_nColumnsDescriptive = g_nCategories+1 # nr of columns which holds text and no data (first column is 'region')
g_years = []


def DEBUG(info, msg):
  print("*** DEBUG :: {}".format(info))
  pprint.pprint(msg)

def getDataDict():
  nDeathsPerYear = list()

  for i_row,row in enumerate(inputLines):
    # pprint.pprint(row)
    if i_row == 0:
      # first line is header...
      continue
    else:
      if i_row == 1:
        # ... second line has column headers and all the years
        g_years = row[g_nCategories+1:] # years, as strings
        g_years = [int(year) for year in g_years]
        if g_DEBUG:
          DEBUG("years: ", g_years)
      else:
        # data rows
        nDeathsPerYear = row[g_nCategories+1:]
  pass

def main(args):
  #inputLines = None

  # read with panda library
  # dataFrame = pd.read_csv(g_inputFile, sep=',',header=None) # df = dataFrame
  # print("dataFrame:")
  # print(dataFrame)
  # print()
  #
  # print("first row:")
  # print(dataFrame.iloc[[0]])
  #
  # years = dataFrame.iloc[[0]]
  #
  #
  # # print("data in panda array:")
  # # print(dataFrame.values)
  # #
  # # # print(input_data_panda)
  # # print(dataFrame.keys())
  #
  # # plot
  # plt.figure();
  # dataFrame.plot(x=years, y=years)

  # years = input_data_panda.values[0][4:]
  # print("Years:")
  # print(years)

  # read with genfromtext
  # get lines of input data from SCB table (CSV format)
  # first open the file to know how many columns we have
  nColumns=None
  with open(g_inputFile, 'r') as inp_f:
    nColumns = len(inp_f.readline().split(","))
  # inp_data = np.genfromtxt((",".join(line.split()[g_nColumnsDescriptive:]) for line in g_inputFile), delimiter=',', dtype=None)
  if not nColumns:
    print("*** ERROR :: couldn't successfully get the nr of columns!")
    sys.exit(0)
  print("nColumns = {}".format(nColumns))
  # get the data, ignore the first columns with descriptive data
  # inp_data will have
  inp_data = np.genfromtxt( g_inputFile, delimiter=',', dtype=float, usecols=range(g_nColumnsDescriptive,nColumns), skip_header=1)

  # some hacking to get the years (couldn't get the quotation marks to be ignored in a neat way)
  years = np.genfromtxt( g_inputFile, delimiter=',', dtype=str, usecols=range(g_nColumnsDescriptive, nColumns), skip_footer=len(inp_data))
  years = np.array([float(year.replace('"', '')) for year in years])
  print("years = {}".format(years))

  categories = np.genfromtxt( g_inputFile, delimiter=',', dtype=None, usecols=range(g_nColumnsDescriptive), skip_header=1)


  print("inp_data = {}".format(inp_data))
  pprint.pprint(categories)



  # print("len(inp_data) = {}".format(len(inp_data)))
  # print("len(categories) = {}".format(len(categories)))

  yvalues = inp_data[:,1] # first category
  yvalues = inp_data[1,:]
  print("yvalues = {}".format(yvalues))
  print("len(yvalues) = {}, len(years) = {}".format(len(yvalues), len(years)))
  plt.plot(years, yvalues, 'g^')
  plt.show()

  # #pprint.pprint(input_data)

  # inp_data = np.genfromtxt( g_inputFile, delimiter=',', dtype=None) #, usecols=range(g_nColumnsDescriptive,nColumns), skip_header=1)
  # print(inp_data)

  #
  #
  # # number of data points
  # nColumns = input_data.shape[1]
  #
  # # first row, holding the years
  # pprint.pprint(input_data[0,g_nColumnsDescriptive:nColumns])
  #
  # xvalues = input_data[0, g_nColumnsDescriptive:nColumns].astype(np.float)
  #
  # yvalues = input_data[24, g_nColumnsDescriptive:nColumns].astype(np.float)
  # print(xvalues.shape)
  # print(yvalues.shape)
  # plt.plot(xvalues, yvalues, 'g^')
  # plt.show()

  # with open(g_inputFile, 'r', encoding="utf8") as inp_csvfile:

    # inputLines = csv.reader(inp_csvfile, delimiter = ",") #[line.split("\n") for line in inp_f]
    # reader = csv.DictReader(inp_csvfile)

    #data_dict = {}


  # if g_DEBUG:
  #   # DEBUG("input data lines: ", inputLines)
  #   for row in inputLines:
  #     DEBUG("row: ", row)
  # make data on dictionary format: {"dodsorsak": {"alderskategori": {"kon": [dodaAr0, dodaAr1, ...]}}}
  # inpData = {}
  # counter_line = 0
  # for line in inputLines:
  #   if g_DEBUG:
  #     # DEBUG("line split by comma: ", line.split(","))
  #     pass

  #
  #   counter_line+=1


if __name__ == "__main__":

  # Get the command line arguments, if given
  parser = argparse.ArgumentParser(description="Process SCB data")

  parser.add_argument('--save', help='save output plot')

  args = parser.parse_args()

  main(args)

  # print(args.accumulate())
