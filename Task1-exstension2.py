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

#input: ./imena.txt' ./prezimena.txt'
#output: result.txt

import pandas as pd
import os

def writeToFile(text, name):
    file = open( name, "w")
    file.write(text)
    file.close()


def divideFileToChunks(path1, chunkSize):
    files = []
    i = 0
    for chunk in pd.read_csv(path1, sep=' ', header=None, chunksize=chunkSize):
        chunk = pd.DataFrame.sort_values(chunk, by=[1])

        name = "./chunk_" + str(i) + '.txt'
        i = i+1
        fileOut= open(name, 'w')
        str_chunk = chunk.to_string(index=False, header=False)
        # isprika na ruznom strippanju, bilo mi je dosta ovog :)
        str_chunk = str_chunk.replace("      "," ").replace("    "," ").replace("   "," ").replace("  "," ").replace("\n ", "\n")
        writeToFile(str_chunk, name)
        files.append(name)
    return files


def mergeSortTwoChunks(fname, fname2):
    #Merging smaller sorted chunk files into one bigger sorted file
    # reading without loading file in memory
    with open(fname, 'r') as f1:
        fileOut = open("./temp.txt", "w")

        f2 = open(fname2, 'r')
        line2 = f2.readline()
        e2 = line2.strip("\n").replace("  "," ").split(" ")
        num2 = e2[1]

        for line in f1:
            e1 = line.strip("\n").replace("   "," ").replace("  "," ").split(" ")
            num1 = e1[1]

            while (int(num1) > int(num2)):
                fileOut.write(e2[0] + ' ' + e2[1] + "\n")
                try:
                    line2 = f2.readline()
                    e2 = line2.strip("\n").replace("   "," ").replace("  "," ").split(" ")
                    num2 = e2[1]
                except IndexError:
                    fileOut.write(e1[0] + ' ' + e1[1])
                    return

            fileOut.write(e1[0] + ' ' + e1[1] + "\n")



def combineSortedChunkFiles(list, resultFileName):
    # combines ALL chunks to big result-output-file -> resultFileName
    i=1
    #copy first chunk to results.txt for further comparison
    with open(list[0]) as file0:
        fileResult = open(resultFileName, "w")
        for line in file0:
            fileResult.write(line)
        fileResult.close()
        os.remove(list[0])
    while i < len(list):

        mergeSortTwoChunks(resultFileName, list[i]) # writes sorted and combined 2 chunks into ./temp.txt
        os.remove(list[i])
        i = i + 1
        #clear result.txt and copy new temp.txt to result.txt for further comparison
        with open("./temp.txt", 'r') as fileTemp:
            fileResult = open(resultFileName, "w")
            for line in fileTemp:
                fileResult.write(line)
    try:
        os.remove("./temp.txt")
    except:
        print("")



def mergeSortedFiles(first_names_file, last_names_file):
    #merges two input files - one with first names and one with last names into final result
    with open(first_names_file, 'r') as f1:
        fileOut = open("./result.txt", "w")
        f2 = open(last_names_file, 'r')
        line2 = f2.readline()
        for line1 in f1:
            e1 = line1.strip("\n").replace("   "," ").replace("  "," ").split(" ")
            ime = e1[0]
            id = e1[1]
            e2 = line2.strip("\n").replace("   "," ").replace("  "," ").split(" ")
            prezime = e2[0]
            fileOut.write(ime + " " +prezime + " "  + id + "\n")
            try:
                line2 = f2.readline()
            except IndexError:
                return
    os.remove(first_names_file)
    os.remove(last_names_file)




#___________________________MAIN______________________________

first_names_file = './firstNames.txt'
last_names_file = './lastNames.txt'
chunkSize = 126

#Divide files to chunks, get the list of chunk files:
list_chunks_firstname = divideFileToChunks('./imena.txt', chunkSize)
combineSortedChunkFiles(list_chunks_firstname, first_names_file)

list_chunks_lastname = divideFileToChunks('./prezimena.txt', chunkSize)
combineSortedChunkFiles(list_chunks_lastname, last_names_file)

mergeSortedFiles(first_names_file, last_names_file)

