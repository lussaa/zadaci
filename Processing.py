import numpy as np
import pandas as pd
from tabulate import tabulate

fname = ("./i1.txt")
fname2 = ("./i2.txt")


def mergeSortTwoFiles(fname, fname2):
    # reading without loading file in memory
    with open(fname) as f1:
        fileOut = open("./out.txt", "w")

        f2 = open(fname2)
        line2 = f2.readline()
        e2 = line2.strip("\n").split(" ")
        num2 = e2[1]

        for line in f1:
            e1 = line.strip("\n").split(" ")
            num1 = e1[1]

            while (int(num1) > int(num2)):
                fileOut.write(e2[0] + ' ' + e2[1] + "\n")
                try:
                    line2 = f2.readline()
                    e2 = line2.strip("\n").split(" ")
                    num2 = e2[1]
                except IndexError:
                    fileOut.write(e1[0] + ' ' + e1[1])
                    return

            fileOut.write(e1[0] + ' ' + e1[1] + "\n")



def writeToFile(text, name):
    file = open("./"+ name, "w")
    file.write(text)
    file.close()

i=0
for chunk in pd.read_csv("./i1.txt", sep=' ', header=None, chunksize=512):
    chunk = pd.DataFrame.sort_values(chunk, by=[1])
    name = "./chunk_" + str(i) + '.txt'
    i = i + 1
    #print(chunk.to_string(justify='left', index=False, header=False))
    print(tabulate(chunk, showindex=False))



