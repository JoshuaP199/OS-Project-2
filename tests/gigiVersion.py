import os

#create a list to hold all the hexadecimal and (s,l) pairs

pairs = []


#code needs to be in the same location as the trace folders
location  = input("Please enter the folder location where the Trace Files are being Kept")
for filename in os.listdir(location):
    path = location + "\\" + filename
    f = open(path, "r")
    for line in f:
        hexa = line[4:12]
        pairs.append(hexa)

#This is splitting it by the head and the tail
tails = []
heads = []
i=0
for item in pairs: 
    heads.append(pairs[i][0:5])
    tails.append(pairs[i][5:])
    i+=1

#####################
#    Page Table    #
#####################
#  heads # tails # v#
#####################

# the number of entries allowed in the page table is 2^20

page_table_capacity = 2**20
page_table_capacity

#Page Table will be a List of Lists each entry will be as such [head, tail, v]
pageTable = []

#creates the pageTable and initializes v to all 0's
i = 0
for item in pairs: 
    pageTable.append([heads[i], tails[i], 0])
    i+=1
