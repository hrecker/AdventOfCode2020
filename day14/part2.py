mask = 0
memory = {}

def getAllAddresses(currentAddress, floating):
    #print("getalladdresses " + str(len(floating)))
    addresses = [currentAddress]
    if len(floating) == 0:
        return addresses

    zeroMask = ~(1 << (len(mask) - floating[0] - 1))
    zeroAddress = currentAddress & zeroMask
    oneMask = 1 << (len(mask) - floating[0] - 1)
    oneAddress = currentAddress | oneMask
    #print("zero " + bin(zeroAddress) + ", one " + bin(oneAddress))
    addresses += getAllAddresses(zeroAddress, floating[1:])
    addresses += getAllAddresses(oneAddress, floating[1:])
    #print("bottom")
    return addresses

def setMemoryAtIndex(index, val):
    global memory
    #print("binary before: " + bin(val))
    #print("setting memory at index " + str(index) + " to " + str(val))
    #print(" dec before: " + str(index) + " bin before " + bin(index))
    floating = []
    for idx, bit in enumerate(mask):
        if bit == '1':
            tempMask = 1 << (len(mask) - idx - 1)
            index = index | tempMask
        elif bit == 'X':
            floating.append(idx)
    
    #print("original " + bin(index) + " dec: " + str(index))
    #print("floating " + str(floating))
    addresses = getAllAddresses(index, floating)

    for address in set(addresses):
        #print("setting memory at index " + str(address) + " to " + bin(val))
        memory[str(address)] = val

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

sum = 0
for val in memory:
    sum += memory[val]

print(sum)
    