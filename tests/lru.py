import random 

queue = []
#numbers = [2,6,9,2,4,2,1,7,3,0,5,2,1,2,9,5,7,3,8,5] #test1
numbers = [0,6,3,0,2,6,3,5,2,4,1,3,0,6,1,4,2,3,5,7] #test2
'''
for n in range(0,22):
    numbers.append(random.randint(0, 9))
'''

print("numbers = ", numbers)
print("queue = ", queue)
print("\nStart with LRU\n")

global i, pf
i = 0
pf = 0

for num in numbers:
    if len(queue) != 3:
        queue.append(num)
        print(queue)
        pf += 1
    else:
        if num in queue: #NEED TO CREATE FUNCTION FOR THIS SKIPPING CRAP
            print("X")
            if num == queue[i]:
                if i < 2:
                    i += 1
                else:
                    i = 0
            else:
                continue

        elif i < 2:
            queue[i] = num
            i += 1    
            print(queue)
            pf += 1

        else:
            queue[i] = num
            i = 0
            print(queue)
            pf += 1
print(pf, " Page Faults")