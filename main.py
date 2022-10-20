user_name = input()
name_list = user_name.split()

first_ini = name_list[0][0]
middle_ini = name_list[1][0]
last_name = name_list[-1]

if len(name_list) == 3:
    print(last_name + ',', first_ini + '.' + middle_ini + '.')

else:
    print(last_name + ',', first_ini + '.')
