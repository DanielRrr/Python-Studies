n = input()
numbers = list(n)
numbers = [int(i) for i in numbers]
if (sum(numbers[:3]) == sum(numbers[3:])):
    print("Счастливый")
else:
    print("Обычный")
