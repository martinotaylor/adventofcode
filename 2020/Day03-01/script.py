file = open('input.txt')
lines = file.read().splitlines()

trees = 0
position = 3
for line in lines[1:]:
    if line[position] == '#': 
        trees = trees + 1  
    position = (position + 3) % 31

print(trees)