file = open('input.txt')
lines = file.readlines()

correctPassword = 0
for line in lines:
    fields = line.split(' ')
    rule = fields[0].split('-')
    character = fields[1][0]
    password = fields[2]

    print(rule)
    print(character)
    print(password)
    
    if ((character == password[int(rule[0])-1] and character != password[int(rule[1])-1]) or (character != password[int(rule[0])-1] and character == password[int(rule[1])-1])):
        correctPassword = correctPassword + 1

print(correctPassword)