from itertools import zip_longest, islice
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Никита', 'Данил', 'Марина']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def my_gen():
    for i in zip_longest(tutors, classes, fillvalue=None):
        if len(tutors) > len(classes):
            yield i


gen = my_gen()
print(next(gen))
print(next(gen))
print(*islice(gen, 8))
