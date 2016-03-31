number = 23
guess = int(input('Введите число : '))

if guess == number:
   print('Вы угадали!')
   print('Вы выиграли ничего!')
   
elif guess < number:
   print('Нет, больше')

else:
   print('Нет, меньше')
   
print('Пока')
