my_list = input("Введите ФИО, разделяя пробелами, без запятых.")
age = int(input("Введите возраст, разделяя пробелами, без запятых."))
height = int(input("Введите рост(см), разделяя пробелами, без запятых."))
weight = float(input("Введите вес(кг), разделяя пробелами, без запятых."))
i = 0

my_list = my_list.split()#объединение всех введенных параметров в список
my_list.append(age)
my_list.append(height)
my_list.append(weight)


if len(my_list) != 6:
    print("Возможно Вы что-то забыли указать, попробуйте ввести ещё раз.")#проверка введения всех данных
elif (age <= 0) or (height <= 0) or (weight <= 0):
    print("Возможно Вы что-то забыли указать, попробуйте ввести ещё раз.")
else:
    print("В списке:", my_list)#вывод типов
    while i < len(my_list):
       print("Тип", i+1,"-го элемента", type(my_list[i]))
       i += 1

#__________________________________________________

#my_list = ['dh', 'hdfhdg', 'dhdghf', 1, 1, 1.0, 'fgdfg'] - для проверки списков с нечетной длинной
i = 0
if len(my_list) == 0:
    print("Вы ввели пустой список, попробуйте ещё раз.")
elif len(my_list) == 1:
    print("В вашем списке всего один пункт:", my_list)
else:
    while i < (len(my_list) - 1):
        t = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = t
        i += 2
print(my_list)
