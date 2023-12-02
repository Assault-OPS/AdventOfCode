with open("day2input1.txt","r") as f:
    lines = f.readlines()
result = 0
for ID,line in enumerate(lines,1):
    _ = line.strip("\n").split(":")
    SET = _[1].split(";")
    stuff = [[i.split(" ")[1:] for i in triplet.split(",")] for triplet in SET]
    di = [{data[1]:data[0] for data in triplet} for triplet in stuff]
    result += ID if all([all([int(data[color]) <= {"red": 12, "green":13, "blue":14}[color] for color in data]) for data in di]) else 0

print(result)
