translation = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
               'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def translate(num):
    if num.istitle():
        return str(translation.get(num.lower())).title()
    return translation.get(num)


print(translate(input('Введите число: ')))
