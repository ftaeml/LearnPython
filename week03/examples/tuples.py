## [homework]
##Задание 4
##
##Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно). На вход программе передаётся положительное целое число n — столько элементов последовательности должна отобразить программа.
##
##На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
##
##Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
##
##Пример экрана вывода:
##
##>>> 7
##1 2 2 3 3 3 4
n = int(input("Введите число ")) # сколько выводить цифр
count = 1                # кол. вывденных цифр 
i = 0                    # текущая цифра
while count <= n:
    c = 0                # сколько раз выведена цифра i
    i+=1
    # for t in range(i):
    while c < i:
        print(i, end=" ") # end - разделитель между print
        c+=1              
        count += 1
        if count > n:
            break

## [print]

print("test1", end=" ")
print("test2", end=' ')
print("test3", end=' ')

## [tuples]
l = [2, 54, 7.5, 890] # список
print(type(l))
print(type(l) == list)
print("l[0] =", l[0])
l[0] = 100
print("l[0] =", l[0])
print("size of list:", l.__sizeof__())

t = (2, 54, 7.5, 890) # кортеж
print(type(t))
print(type(t) == tuple)
print("t[0] =", t[0])
#t[0] = 100
print("l[0] =", t[0])
print("size of tuple:", t.__sizeof__())

## [subcode]

n = int(input ("Введіть ціле число "))
x = list(range (n+1))
print (x[1:n+1])
i = 0
k = 0
t = []
for k in x:
    p = str(k)*k
    print (p)
    s = list(p)
    t.append(s)
    print (t)
    if len(list (t)) == n+1: break
    print (t)
    print (t[1:n+1])


