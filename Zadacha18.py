#Задача 18: Требуется найти в массиве A[0..N-1] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел A[i]. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5
A=[]
N=int(input("Введите количество элементов массива "))
for i in range(N):
    print(f"Введите {i} -й элемент массива ")
    A.append(int(input()))
    i+=1
D=0
B=0
min=1000000
max=0

X=int(input("Введите элемент, относительно которого нужно подобрать близкий в массиве "))
for i in range(N):
    if A[i]==X:
        D=A[i]
        break
    if (X+1==A[i])and(D!=A[i]):
        D=A[i]
    if (X-1==A[i])and(D!=A[i]):
        B=A[i]
    if A[i]<min:
        min=A[i]
    if A[i]>max:
        max=A[i]
        i+=1
if (D==0)and(min>X):
    D=min
elif (D==0)and(max<X):
    D=max
if B==0:
    print(f'ближайшее число к {X} число {D}')
if B!=0:
    print(f'ближайшее число к {X} число {B} и {D}')
