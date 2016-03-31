number = 23
running = True
while running:
   guess = int(input())
   
   if guess == number:
      print('Мои конгратуляции')
      running = False
      
   elif guess < number:
      print('Больше')
   else:
      print('Меньше')
else:
   ('Цикл все')

print('Пока')
