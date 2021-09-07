def thesaurus_adv(*args):
    names_surnames = {}
    for n_s in args:
        names_surnames.setdefault(n_s.split()[1][0], {}).setdefault(n_s.split()[0][0], []).append(n_s)
    return names_surnames


print(thesaurus_adv('Виктория Яковлева', 'Мария Давыдова', 'Александра Маслова', 'Полина Гальцева',
                    'София Никитина', 'Сергей Носков', 'Степан Максимов', 'Илья Борисов',
                    'Матвей Максимов', 'Лев Ширяев'))
