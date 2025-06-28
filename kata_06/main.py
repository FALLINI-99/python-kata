print('Сколько вам полных лет ')
age = int(input())
def get_age_status(age):
    if age < 18:
        return 'Доступ запрещен'
    elif age == 18:
        return('Поздравляем с совершеннолетием!')
    elif age <= 65:
        return('Доступ разрешен')
    else:
        return('Желаем приятного отдыха на пенсии!')
status = get_age_status(age)
print(status)