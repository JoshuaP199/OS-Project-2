#By Joshua Perez

import random 

queue = []
numbers = [2,6,9,2,4,2,1,7,3,0,5,2,1,2,9,5,7,3,8,5] #test1
#numbers = [0,6,3,0,2,6,3,5,2,4,1,3,0,6,1,4,2,3,5,7] #test2
'''
#numbers = []

for n in range(0,22):
    numbers.append(random.randint(0, 9))
'''

print("numbers = ", numbers)
print("queue = ", queue)
print("\nStart with FIFO\n")

global i, previous, pf
i = 0
previous = False
pf = 0

for num in numbers:
    if len(queue) != 3:
        queue.append(num)
        print(queue)
        pf += 1
    else: 
        if num in queue: #NEED TO CREATE FUNCTION FOR THIS SKIPPING CRAP
            print("X")
            if previous == True:
                i -= 1
            else:
                if i == 0:
                    continue
                elif i < 2:
                    i +=1
                elif i == 2:
                    continue
                else:
                    i = 0
            previous = True


        elif i < 2:
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
print(pf, " Page Faults")