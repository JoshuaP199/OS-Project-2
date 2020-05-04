#############################
# Get Data From Trace Files #
#############################

import os
import sys

#create a list to hold all the hexadecimal and (s,l) pairs

pairs = []


#code needs to be in the same location as the trace folders
location  = input("Please enter the folder location where the Trace Files are being Kept")
file = input("Please input what file you would like to run without the .trace ending")
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

global PageHitsIndexes
PageHitsIndexes = []

#####################
#      LRU Code     #
#####################

def LRU(numbers): #numbers is a list & capacity is the page size
    print("\nLRU\n")

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
    print(pf)
    

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
    pMem = LRU(PMem)



for item in pagTab: 
    if item[0] in PageHitsIndexes:
        item[3] == 1    
        
#1 # Pagtab needs to be set to size 2^20
-g # Read first item from file
-g # append head to pagTab and set v as 0
-g # send tail to position i (i+=1 for each rendition) of main memory until main memory is full
-g #main memory contains a list of indexes and their corresponding tails
#1 # main memory needs to be set to size (2^12)
#1 #once the main memory is full (there have been 2^12 entries) apply lru
    #LRU modifications that need to be done
        # 1. Read each entry in main memory ex. Memory[1] 
        # 2. Append each entry to a list of numbers
        # 3. Do LRU on this list of numbers
        # 4. Return the last frame of the LRU 
        # 5. update a general count of page faults that can be added to each rendition of the lru
        # 6. Change main memory to fit the LRU last frame
-g #Page hit is everytime it is already in main memory
#Repeat


########################
#       Run Code       #
########################

#LRU(lruholder)
#FIFO(lruholder)
