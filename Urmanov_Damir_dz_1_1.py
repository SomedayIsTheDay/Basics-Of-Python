seconds = int(input('Введите количество секунд: '))
minutes = seconds//60
hours = minutes//60
days = hours//24
if seconds < 60:
    print(f'{seconds} сек')
elif 3600 > seconds >= 60:
    seconds = seconds % 60
    print(f'{minutes} мин {seconds} сек')
elif 86400 > seconds >= 3600:
    seconds = seconds % minutes
    minutes = minutes % 60
    print(f'{hours} час {minutes} мин {seconds} сек')
else:
    seconds = seconds % minutes
    minutes = minutes % 60
    hours = hours % 24
    print(f'{days} дн {hours} час {minutes} мин {seconds} сек')
