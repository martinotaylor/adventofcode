file = open('input.txt')
numbers = file.readlines()

for number1 in numbers:
    for number2 in numbers:
        for number3 in numbers:
            result = int(number1) + int(number2) + int(number3)
            if result == 2020:
                print(int(number1) * int(number2) * int(number3))