#3 В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
#from random import*
#n=round(randint(1,100))
#max_n=100
#print("Попробуй отгадать число,у тебя 10 попыток:")

#for i in range(10):
#	m=int(input(f"Попытка  №{i+1},Введи число:"))
#	if m<n and i<9:
#		print("Загадай число больше:")
#	elif m>n and i<9:
#		print("Загадай число меньше:")
#	elif m==n:
#		print("Ты угадал!!!!!!")
#else:
#	print("Ты истратил все попытки,Было загадано число",n) 
#5 Найти сумму и произведение цифр, введенного целого числа. Например, если введено число 325, то сумма его цифр равна 10 (3+2+5), а произведение 30 (3*2*5).
#print("Введи целое число:")
#n = int(input())
#s = 0
#m = 1
#while n>0:
#    s += n%10
#    m *= n%10
#    n = n//10
#print("Сумма:", s)
#print("Произведение:", m)
#2Посчитать сумму числового ряда от 0 до L (например, 14) включительно. Например, 0+1+2+3+…+14;
#sum=0
#for i in range(1,15):
#        sum = sum+ i
#print(sum)
#1Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n зайцев. Mежду двумя соседними зайцами также имеется пустой (из пробелов) столбец. Разрешается вывести пустой столбец после последнего зайца. Для упрощения рисования скопируйте зайца  в среду разработки.
#for rjady in range (1,9):
#	for stroka in range(1,9):
#		if rjady==1:
#			print("(\_/)",end=" ")
#		elif rjady==2:
#			print("(o o)",end=" ")
#		elif rjady==3:
#			print(" / | \*",end=" ")
#4Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
a = int(input("Введите целое число: "))
b = 0
 
while a > 0:
    # находим остаток - последнюю цифру
    number = a % 10
    a = a // 10
    b = b * 10
    # добавляем цифру
    b = b + number  
 
print('"Обратное" ему число:', b)
