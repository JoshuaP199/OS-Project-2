'''
REQUIREMENTS:
    32-bit Logical Address
    24-bit Physical Address
    Page(Frame) Size: 4KB
    Page Replacement Algorithm: LRU
    Assuming that the page table is stored in a separated space 
        (not in the 24-bit Physical address space)
    Only the functional behavior is simulated. No latency 
        simulation is required.
'''

#READ https://stackoverflow.com/questions/40292822/translate-virtual-address-to-physical-address

def append(stuff, n):
    if n == "l":
        l_list.append(stuff.strip('l 0x').strip('\n'))
    elif n == "s":
        s_list.append(stuff.strip('s 0x').strip('\n'))
    else:
        print("ERROR at " + stuff)


def LRU(numbers): 
    #"numbers" needs to be a list so idk if thats possible
    #Or make this where its called after every number in said list
    queue = []
    i = 0
    pf = 0

    for num in numbers:
        if len(queue) != 3:
            queue.append(num)
            print(queue)
            pf += 1
        else:
            if num in queue:
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
    print(pf, "Page Faults")


def FIFO(numbers):
    #"numbers" needs to be a list so idk if thats possible
    #Or make this where its called after every number in said list
    queue = []
    i = 0
    previous = False
    pf = 0

    for num in numbers:
        if len(queue) != 3:
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
    print(pf, "Page Faults")


#START OF PROGRAM

trace = input("Enter the trace file name you want to read through: (don't include .trace)\n")

files = open(trace + ".trace", "r")

s_count = 0
l_count = 0
s_list = []
l_list = []

for i in files:
    if i[0] == "s":
        s_count += 1
        append(i, "s")
    elif i[0] == "l":
        l_count += 1
        append(i, "l")
    else:
        print("skipped")

print("\nInformation from " + trace + ".trace:")
print("Save =", s_count)
print("Load =", l_count)

#REQUIREMENTS 
print("Number of page faults: ")
print("Page table hit rate: ")