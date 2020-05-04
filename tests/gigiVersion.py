#############################
# Get Data From Trace Files #
#############################

import os
from queue import Queue

#create a list to hold all the hexadecimal and (s,l) pairs

pairs = []


#code needs to be in the same location as the trace folders
location  = input("Please enter the folder location where the Trace Files are being kept.\n")
file = input("Please input what file you would like to run without the .trace ending.\n")
#for filename in os.listdir(location):

path = location + "\\" + file + ".trace"
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
#      LRU Code     #
#####################

def LRU(numbers, capacity): #numbers is a list & capacity is the page size
    print("\nLRU\n")

    i = 0
    pf = 0
    help1 = [] 

    set = []

    #if sys.getsizeof(queue) <= 4000: #4000 is the max amount of bytes
    for num in numbers:
        if i == capacity:
            i = 0
        if len(set) < capacity and num not in set:
            set.append(num)
            #print(set)
            pf += 1
            help1.append(i)
            i += 1
        elif len(set) < capacity and num in set: #how does this work with LRU since u skip to the next index in LRU?
            #print("X")
            continue
        else:
            if num in set:
                #print("X")
                rem = set.index(num)
                help1.remove(rem)
                help1.insert(capacity-1, rem)
                i = help1[0]
            else:
                set[i] = num 
                help1.remove(i)
                help1.insert(capacity-1,i)
                i = help1[0]
                #print(set)
                pf += 1
    return pf
    

####################
#   Fifo Code      #
####################

def FIFO(numbers, capacity): #numbers is a list & capacity is the page size
    print("\nFIFO\n")

    i = 0
    pf = 0

    set = []
    indexes = Queue(maxsize = capacity)

    #if sys.getsizeof(queue) <= 4000: #4000 is the max amount of bytes
    for num in numbers:
        if i == capacity:
            i = 0
        if len(set) < capacity and num not in set:
            set.append(num)
            #print(set)
            pf += 1
            indexes.put(i)
            i += 1
        elif len(set) < capacity and num in set:
            #print("X")
            continue
        else:
            if num in set:
                #print("X")
                continue
            else:
                set[indexes.get()] = num
                #print(set)
                indexes.put(i)
                i += 1
                pf += 1
    return pf

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
lruholder = []
i = 0
for item in pairs: 
    pageTable.append([heads[i], tails[i], 0])
    lruholder.append(int(tails[i], 16))
    i+=1
    
############################
# Implement Virtual Memory #
############################

########################
# Implement Physical Memory #
########################

########################
#       Run Code       #
########################

print(LRU(lruholder, 4), "page faults for", file + ".trace")
print(FIFO(lruholder, 4), "page faults for", file + ".trace")