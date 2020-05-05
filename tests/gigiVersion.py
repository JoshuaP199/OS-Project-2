#############################
# Get Data From Trace Files #
#############################

import os
import sys
from queue import Queue

#create a list to hold all the hexadecimal and (s,l) pairs

pairs = []


#code needs to be in the same location as the trace folders
#location  = input("Please enter the folder location where the Trace Files are being Kept\n")
#file = input("Please input what file you would like to run without the .trace ending\n")
#for filename in os.listdir(location):
f = open(input("Enter the path of your trace file not including .trace: "))

#path = location + "\\" + file + ".trace"
#f = open(path, "r")
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

global PageHitsIndexes
PageHitsIndexes = []

#####################
#      LRU Code     #
#####################

def LRU(numbers): #numbers is a list & capacity is the page size
    print("\nUsing LRU\n")

    counter = 0
    i = 0
    pf = 0
    help1 = [] 

    frames = []

    
    #if sys.getsizeof(queue) <= 4000: #4000 is the max amount of bytes
    for num in numbers:
        if sys.getsizeof(frames) > 4000: 
            i = 0
        if sys.getsizeof(frames) <= 4000 and num not in frames:
            frames.append(num)
            pf += 1
            help1.append(i)
            i += 1
        elif sys.getsizeof(frames) <= 4000 and num in frames: #how does this work with LRU since u skip to the next index in LRU?
            continue
        else:
            if num in frames:
                PageHitsIndexes.append(counter)
                rem = frames.index(num)
                help1.remove(rem)
                help1.insert(help1[-1], rem) 
                i = help1[0]
            else:
                frames[i] = num 
                help1.remove(i)
                help1.insert(help1[-1],i)
                i = help1[0]
                #print(set)
                pf += 1
        counter +=1
    #print(pf)
    return pf, frames[-1] 
    

####################
#   Fifo Code      #
####################

def FIFO(numbers, capacity): #numbers is a list & capacity is the page size
    print("\nFIFO\n")

    i = 0
    pf = 0

    frames = []
    indexes = Queue(maxsize = capacity)

    #if sys.getsizeof(queue) <= 4000: #4000 is the max amount of bytes
    for num in numbers:
        if i == capacity:
            i = 0
        if len(frames) < capacity and num not in frames:
            frames.append(num)
            #print(set)
            pf += 1
            indexes.put(i)
            i += 1
        elif len(set) < capacity and num in frames:
            #print("X")
            continue
        else:
            if num in frames:
                #print("X")
                continue
            else:
                frames[indexes.get()] = num
                #print(set)
                indexes.put(i)
                i += 1
                pf += 1
    return pf
    
############################
#   Simulated   Memory     #
############################
#  heads # tails #     v   #
############################

Vmemory = []
lruholder = []
i = 0
for item in pairs: 
    Vmemory.append([heads[i], tails[i], 0])
    lruholder.append(int(tails[i], 16))
    i+=1


###################################
#      Page Table                 #
###################################
#index # head # list of values # v#
###################################

# the number of entries allowed in the page table is 2^20
pagTab = [None] * (2**20)

i=0


for item in set(heads):
    vals = []
    for entry in Vmemory: 
        if entry[0] == item:
            vals.append(entry[1])
    pagTab.append([i, item, vals, 0 ])
    i+=1    
    

#####################
# Physical Memory   #
#####################

#Our Physical Memory is a List since we are not sure how to speak to the real memory of the computer
#It has been initialized to hold 24 bit address aka (2^12)
pMem = [None] * (2**12)


#This checks Physical Memories size and if it reaches capacity then it applies LRU on it's self
if pMem[-1] != None: 
    pMem = LRU(pMem)



for item in pagTab: 
    if item in PageHitsIndexes:
        PageHitsIndexes[3] == 1   

#Reads each slot in "Main Memory"
d = 0               #total main memory entry number
for c in pMem:
    d += 1


#Append each entry to a list of numbers &  do LRU on said list of numbers
LoN = []    #list of numbers containing tails 
pafa = []   #list of page faults obtained after each ^ list is full
p=0         #used to display the most recent pafr in the list 
j = 0
tpafa = 0

for l in pairs:                                         #goes through all items in pairs
    if len(LoN) > d:                                    #checks if length of LoN is less than the total number of available physical memory (dont rememeber y i set it up like this)
        print("\nFull")                                 #Displays this when LoN has reached its max
        pafa.append(LRU(LoN))                           #Appends the page faults from LoN after going through LRU 
        print("Page faults & last frame:", pafa[p])     #Displays page faults and last frame used in LRU
        tpafa += pafa[p][0]                              #Stores the page faults to gather a total
        p += 1                                          #adds one to pafr's most recent index finder
        LoN = []                                        #Empties LoN list to go through the next wave of numbers
    else:
        LoN.append(pairs[j][5:])                        #Appends tail to LoN list
        j+=1                                            #adds one to pairs index finder
print("\nTotal Page faults:", tpafa)                    #Displays Total page faults

        
#1 # Pagtab needs to be set to size 2^20
#-g # Read first item from file
#-g # append head to pagTab and set v as 0
#-g # send tail to position i (i+=1 for each rendition) of main memory until main memory is full
#-g #main memory contains a list of indexes and their corresponding tails
#1 # main memory needs to be set to size (2^12)
#1 #once the main memory is full (there have been 2^12 entries) apply lru
    #LRU modifications that need to be done
        #1 # 1. Read each entry in main memory ex. Memory[1] 
        #1 # 2. Append each entry to a list of numbers
        #1 # 3. Do LRU on this list of numbers
        #1 # 4. Return the last frame of the LRU 
        #1 # 5. update a general count of page faults that can be added to each rendition of the lru
        # 6. Change main memory to fit the LRU last frame
#-g #Page hit is everytime it is already in main memory
#Repeat


########################
#       Run Code       #
########################

#LRU(lruholder)
#FIFO(lruholder)
