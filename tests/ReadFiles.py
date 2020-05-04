import os

#create a list to hold all the hexadecimal and (s,l) pairs

pairs = []

#code needs to be in the same location as the trace folders
location  = input("Please enter the folder location where the Trace Files are being Kept")
for filename in os.listdir(location):
    f = open(filename, "r")
    for line in f:
        state = line[0]
        hexa = line[2:]
        pairs.append([state, hexa])
       
#storage
storage = []
i = 0
j = (len(pairs)-1)
while j != 0:
    if pairs[i][0] == 's':
        storage.append(pairs[i][1])
    i+=1
    j-=1
