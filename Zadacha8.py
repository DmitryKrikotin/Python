#Задача 8: Требуется определить, можно ли от шоколадки размером n ×m долек отломить k
#долек, если разрешается сделать один разлом по
#прямой между дольками (то есть разломить шоколадку на два прямоугольника).
#Примеры:
#Примечание: каждое считывание производится с новой строки
#3 2 4 -> yes
#3 2 1 -> no
print("Шоколадка m*n ")
n=int(input("Введите число n "))
m=int(input("Введите число m "))
k=int(input("Введите количество долек "))
a=True
a=((k%n==0)or(k%m==0))and(k<=m*n)
print(a)