


with open("day4input.txt","r") as f:
    cards = [line[10:].strip("\n") for line in f.readlines()]


result = 0

for card in cards:
    set1,set2 = card.split("|")
    winning_nums = [int(i) for i in set1.split(" ") if i != ""]
    yomama_nums = [int(i) for i in set2.split(" ") if i != ""]

    result += int(pow(2,len([i for i in yomama_nums if i in winning_nums]))/2)

print(result)