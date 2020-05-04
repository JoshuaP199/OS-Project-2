import os

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
    

#####################
#      LRU Code     #
#####################

def LRU(numbers): 
    #"numbers" needs to be a list so idk if thats possible
    #Or make this where its called after every number in said list
    queue = []
    i = 0
    pf = 0
    capacity = 4
    

    for num in numbers:
        # if sys.getsizeof(queue) <= 4000: #4000 is the max amount of bytes
        if len(queue) != capacity:
            queue.append(num)
            print(queue)
            pf += 1
        else:
            if num in queue:
                print("X")
                if num == queue[i]:
                    if i < (capacity-1):
                        i += 1
                    else:
                        i = 0
                else:
                    continue

            elif i < (capacity-1):
                queue[i] = num
                i += 1    
                print(queue)
                pf += 1

            else:
                queue[i] = num
                i = 0
                print(queue)
                pf += 1
    print(pf, "Page Faults")
    

####################
#   Fifo Code      #
####################

def FIFO(numbers):
    #"numbers" needs to be a list so idk if thats possible
    #Or make this where its called after every number in said list
    queue = []
    i = 0
    previous = False
    pf = 0
    capacity = 4

    for num in numbers:
        if len(queue) != capacity:
            queue.append(num)
            print(queue)
            pf += 1
        else: 
            if num in queue:
                print("X")
                if previous == True:
                    i -= 1
                else:
                    continue
                ''' #I think this works better ^. I think I was overthinking it
                    if i == 0: 
                        continue
                    elif i < 2:
                        i +=1
                    elif i == 2:
                        continue
                    else:
                        i = 0
                '''
                previous = True


            elif i < (capacity-1):
                queue[i] = num
                i += 1    
                print(queue)
                previous = False
                pf += 1

            else:
                queue[i] = num
                i = 0
                print(queue)
                previous = False
                pf += 1
    print(pf, "Page Faults")

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
########################
# Implement Page Table #
########################

# Create list that will be fed to lru
LRU(lruholder)
FIFO(lruholder)
