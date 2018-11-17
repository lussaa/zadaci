#Input data is contained in two disk files. Both files contain multiple entries separated by a
#newline character. The first file is of the following form:
#<first name> <ID number>  -> input1.txt
#The other file contains entries of the following format:
#<last name> <ID number>  -> input2.txt
#Write a program that, based on the information contained in input files, creates an output file
#with the format:
#<first name> <last name> <ID number>
#Extension #1: sort output entries by the ID number
#Extension #2: input data is too big to fit into main memory.

#input: ./input1.txt' ./input2.txt'
#output: ./result.txt

import pandas as pd

def mergeChunks(path1, path2):
    #Loading data:
    data1 = pd.read_csv(path1, sep=" ", header=None)
    data2 = pd.read_csv(path2, sep=" ", header=None)
    data1.columns = ['ime', 'id']
    data2.columns = ['prezime', 'id']
    #merging and sorting:
    data = pd.merge_ordered(data1, data2)
    novi = pd.DataFrame.sort_values(data, by=['id'])
    novi2 = novi[['ime', 'prezime', 'id']]

    return novi2.to_string(index=False, header=False)

def saveToFile(text):
    file = open("./result.txt", "w")
    file.write(text)
    file.close()


outputText= mergeChunks("./input1.txt", "./input2.txt")
saveToFile(outputText)




