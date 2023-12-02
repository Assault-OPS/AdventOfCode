def prod(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

with open("day2input2.txt", "r") as f:
    lines = f.readlines()
result = 0
for ID,line in enumerate(lines,1):
    _ = line.strip("\n").split(":")
    SET = _[1].split(";")
    stuff = [[i.split(" ")[1:] for i in triplet.split(",")] for triplet in SET]
    di = [{data[1]:data[0] for data in triplet} for triplet in stuff]
    result += prod([max([int(i.get(color,0)) for i in di]) for color in ("red","blue","green")])

print(result)