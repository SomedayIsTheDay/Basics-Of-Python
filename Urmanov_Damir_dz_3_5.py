import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def jokes_f(i):
    """
    really hard for me :(
    :param i:
    :return:
    """
    list_of_jokes = []
    while i <= 10:
        jokes = (random.sample(nouns, 1) + random.sample(adverbs, 1) + random.sample(adjectives, 1))
        i += 1
        list_of_jokes.append(jokes)
    return list_of_jokes


print(jokes_f(i=0))
