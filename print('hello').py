while (True):
    FirstTypeTry = input('Введите пароль')
    SecondTypeTry = input('Введите пароль')
    if (FirstTypeTry == SecondTypeTry):
        break
    print("Попробуйте еще раз")
print(FirstTypeTry)