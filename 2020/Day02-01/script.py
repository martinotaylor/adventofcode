file = open('input.txt')
lines = file.readlines()

correctPassword = 0
for line in lines:
    fields = line.split(' ')
    rule = fields[0].split('-')
    character = fields[1][0]
    password = fields[2]
    count = 0

    print(rule)
    print(character)
    print(password)
    
    for passwordChar in password:
      if passwordChar == character:
        count = count + 1
    if (count >= int(rule[0]) and count <= int(rule[1])):
        print(count)
        correctPassword = correctPassword + 1

print(correctPassword)