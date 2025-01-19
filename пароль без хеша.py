name = input ('Введите ваш ник: ')

password = '2339'
input_password = input('Пароль: ')
if input_password == password:
    print('')
    print('Вы успешно авторизовались!') #Если верно
    print(f'Приветствуем вас {name}, продуктивного вам дня!')
else:                                   #Если не верно
    print('')
    print('Неверный пароль!')
    print('Попробуйте ещё раз')