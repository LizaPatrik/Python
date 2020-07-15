mounth = int(input("Введите номер месяца."))
my_tuple = ('зиме', 'весне', 'лету', 'осени')
if (mounth <= 0) or (mounth > 12):
    print("Вы неправильно указали номер месяца. Попробуйте снова")
elif (mounth < 3) or (mounth == 12):
    season = my_tuple[0]
elif (mounth < 6):
    season = my_tuple[1]
elif (mounth < 9):
    season = my_tuple[2]
else:
    season = my_tuple[3]

print("Месяц под номером", mounth, "относится к", season)
