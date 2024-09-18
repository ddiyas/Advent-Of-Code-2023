file = open("Day 1\input.txt")
input_txt = file.read()

numbers_key = {"zero" : "z0o", "one" : "o1e", "two" : "t2o", "three" : "t3e", "four": "f4r", "five": "f5e", "six" : "s6x", "seven": "s7n", "eight": "e8t", "nine" : "n9e" }
numbers =[]
sum = 0

input = input_txt.split()

for line in input:
    for number in numbers_key:
        line = line.replace(number, numbers_key[number])
    for c in line:
        try:
            numbers.append(int(c))
        except:
            continue
    sum += numbers[0] * 10 + numbers[len(numbers) - 1]
    numbers.clear()

print(sum)