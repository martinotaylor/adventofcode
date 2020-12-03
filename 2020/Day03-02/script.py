file = open('input.txt')
lines = file.read().splitlines()

# right 3 down 1
trees = 0
position = 3
for line in lines[1:]:
    if line[position] == '#': 
        trees = trees + 1
    position = (position + 3) % 31

# right 1 down 1
trees2 = 0
position = 1
for line in lines[1:]:
    if line[position] == '#': 
        trees2 = trees2 + 1
    position = (position + 1) % 31

# right 5 down 1
trees3 = 0
position = 5
for line in lines[1:]:
    if line[position] == '#': 
        trees3 = trees3 + 1
    position = (position + 5) % 31

# right 7 down 1
trees4 = 0
position = 7
for line in lines[1:]:
    if line[position] == '#': 
        trees4 = trees4 + 1
    position = (position + 7) % 31
    
# right 1 down 2
position = 1
trees5 = 0
for line in lines[2::2]:
    if line[position] == '#': 
        trees5 = trees5 + 1
    position = (position + 1) % 31

print(trees)
print(trees2)
print(trees3)
print(trees4)
print(trees5)

print(trees2 * trees * trees3 * trees4 * trees5)