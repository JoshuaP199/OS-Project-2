#By Joshua Perez

import random 
from queue import Queue

queue = []
#numbers = [2,6,9,2,4,2,1,7,3,0,5,2,1,2,9,5,7,3,8,5] #test1
#numbers = [0,6,3,0,2,6,3,5,2,4,1,3,0,6,1,4,2,3,5,7] #test2

numbers = []

for n in range(0,100):
    numbers.append(random.randint(0, 9))

capacity = int(input("Please enter the page size in KB: (dont include KB)\n"))

#print("numbers = ", numbers)
#print("queue = ", queue)
print("\nStart with FIFO\n")

global i, pf#, previous
i = 0
pf = 0
#previous = False


#capacity = 4 #number of pages that memory can hold
set = []
indexes = Queue(maxsize = capacity)

#if sys.getsizeof(queue) <= 4000: #4000 is the max amount of bytes
for num in numbers:
    if i == capacity:
        i = 0
    if len(set) < capacity and num not in set:
        set.append(num)
        print(set)
        pf += 1
        indexes.put(i)
        i += 1
    elif len(set) < capacity and num in set:
        print("X")
        continue
    else:
        if num in set:
            print("X")
            continue
        else:
            #print(indexes.get())
            set[indexes.get()] = num
            print(set)
            indexes.put(i)
            #print(indexes)
            i += 1
            pf += 1

'''
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
'''
'''
                #I think this works better ^. I think I was overthinking it
                    if i == 0: 
                        continue
                    elif i < 2:
                        i +=1
                    elif i == 2:
                        continue
                    else:
                        i = 0
'''
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
'''
print(pf, "Page Faults")