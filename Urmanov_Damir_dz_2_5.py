prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34,
          98.9, 70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.8, 78, 93, 88.08]
prices = [str(i).split('.') for i in prices]
print(prices)
for i in prices:
    if len(i) == 1:
        if len(i[0]) == 1:
            print(f'0{i[0]} рублей 00 копеек')
        elif len(i[0]) > 1:
            print(f'{i[0]} рублей 00 копеек')
    elif len(i) > 1:
        if len(i[0]) == 1:
            if len(i[1]) > 1:
                print(f'{i[0]} рублей {i[1]} копеек')
            elif len(i[1]) == 1:
                print(f'{i[0]} рублей 0{i[1]} копеек')
        elif len(i[0]) > 1:
            if len(i[1]) > 1:
                print(f'{i[0]} рублей {i[1]} копеек')
            elif len(i[1]) == 1:
                print(f'{i[0]} рублей 0{i[1]} копеек')
# сортирование по возрастанию c сохранением id
prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34,
          98.9, 70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.8, 78, 93, 88.08]
print(id(prices))
prices.sort()
print(prices)
print(id(prices))
# сортирование по убыванию с созданием нового списка
decreasing_prices = sorted(prices, reverse=True)
print(decreasing_prices)
# 5 самых дорогих товаров отсортированные по возрастанию
prices.sort()
print(prices[-5:])
