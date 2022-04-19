st = input("Введите имя и возраст через запятую. Пример:Никита, 2\n").split(', ')
name = st[0]
age = int(st[1])

answer = 'Привет, ' + name + '! Тебе ' + str(age) + ' лет.'
additional = ''
if age < 14:
    answer = 'Ошибка: Минимальный возраст — 14 лет.'
elif len(name) < 3:
    if len(name) == 0:
        answer = 'Ошибка: пустое имя.'
    else:
        answer = 'Ошибка: В имени должно быть минимум 3 символа.'
elif age <= 0:
    answer = 'Ошибка: Возраст не может быть равен числу ' + str(age)
else:
    if 16 <= age <= 17:
        additional = ' Не забудь получить ваш первый паспорт!'
    elif 25 <= age <= 26:
        additional = ' Не забудь заменить паспорт по достижении 25 лет!'
    elif 45 <= age <= 46:
        additional = ' Не забудь заменить паспорт по достижении 45 лет!'
print(answer + additional)
