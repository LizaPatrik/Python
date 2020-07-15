my_list = [7, 5, 3, 3, 2]
t = int(input("Введите значение."))
i = 0

my_list = my_list[::-1]
if t <= my_list[0]:
    my_list.insert(0, t)
my_list = my_list[::-1]

while i < len(my_list):
    if t > my_list[i]:
        my_list.insert(i, t)
    i += 1
print(my_list)


#где-то ошибка, но я не нашла
