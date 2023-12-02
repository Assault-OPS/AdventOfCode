

# I know this is a very bad code but it works

with open('day2input.txt','r') as f:
    inputs = f.readlines()
lines = [rawcommand.strip('\n') for rawcommand in inputs]


di = {"one": 1,"two": 2,"three": 3,"four": 4,"five": 5,"six": 6,"seven": 7,"eight": 8,"nine": 9,"1": 1,"2": 2,"3": 3,"5": 5,"6": 6,"7": 7,"4": 4,"8": 8,"9": 9,
}
elems = [i for i in di]
result = 0
values = []
for line in lines:
    print(line)
    firstNumIndex = []
    for elem in elems:
        index = line.find(elem)
        revindex = line[::-1].find(elem[::-1])
        if index != -1:
            # firstNumIndex.append((index,line[index:index+len(elem)]))
            val = line[index:index+len(elem)]
            reval = line[::-1][revindex:revindex+len(elem)][::-1]
            firstNumIndex.append((index,di[val]))
            firstNumIndex.append((len(line)-revindex,di[reval]))
    values.append((min(firstNumIndex)[1],max(firstNumIndex)[1]))

print(values)

for val in values:
    result += val[0] * 10
    result += val[1]

print(result)
