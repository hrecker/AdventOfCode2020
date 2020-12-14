mask = 0
memory = [0] * 100000


def setMemoryAtIndex(index, val):
    global memory
    #print("binary before: " + bin(val))
    #print("setting memory at index " + str(index) + " to " + str(val))
    for idx, bit in enumerate(mask):
        if bit == '0':
            tempMask = ~(1 << (len(mask) - idx - 1))
            val = val & tempMask
        elif bit == '1':
            tempMask = 1 << (len(mask) - idx - 1)
            val = val | tempMask
    #print("setting memory at index " + str(index) + " to " + bin(val))
    memory[index] = val

with open("input.txt") as input:
    for line in input:
        pieces = line.split(" = ")
        if "mask" in pieces[0]:
            #print("setting mask")
            mask = pieces[1].strip('\n')
            #print(mask)
        else:
            index = int(line.split("[")[1].split("]")[0])
            val = int(pieces[1])
            setMemoryAtIndex(index, val)

#for index, val in enumerate(memory):
#    if val != 0:
#        print("value " + str(val) + " at index " + str(index))

print(sum(memory))
    