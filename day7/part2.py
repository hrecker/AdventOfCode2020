count = 0
lastCount = 0
lines = []
bagTree = {}
currentNodes = ["shiny gold"]

with open('input.txt') as input:
    for line in input:
        lines.append(line)
    while True:
        lastCount = len(bagTree.keys())
        nextNodes = []
        for line in lines:
            pieces = line.split("contain")
            contents = pieces[1].strip()
            contents = contents[:len(contents) - 1]
            bagName = pieces[0].split(" bags")[0]
            if "no other bags" in contents:
                continue

            bagContents = {}
            if bagName in currentNodes:
                bagTree[bagName] = {}
                for bag in contents.split(", "):
                    bagPieces = bag.split(' ')
                    bagCount = bagPieces[0]
                    innerBagName = bagPieces[1] + " " + bagPieces[2]
                    nextNodes.append(innerBagName)
                    bagTree[bagName][innerBagName] = int(bagCount)

        if len(bagTree.keys()) == lastCount:
            break

        currentNodes = nextNodes

def countBagsRequired(bagTree, bagName):
    total = 0
    if bagName in bagTree:
        for child in bagTree[bagName].keys():
            total += bagTree[bagName][child] * countBagsRequired(bagTree, child)
            if child in bagTree:
                total += bagTree[bagName][child]
    else:
        total = 1
            

    return total
    
print(str(bagTree))
print(str(countBagsRequired(bagTree, "shiny gold")))