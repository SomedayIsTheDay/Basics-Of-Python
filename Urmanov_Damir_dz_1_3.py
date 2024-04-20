i = 0
for i in range(1, 101):
    if i == 1 or i == 21 or i == 31 or i == 41 or i == 51 or i == 61 or i == 71 or i == 81 or i == 91:
        print(f'{i} процент')
    elif 1 < i < 5 or 21 < i < 25 or 31 < i < 35 or 41 < i < 45 or 51 < i < 55\
            or 61 < i < 65 or 71 < i < 75 or 81 < i < 85 or 91 < i < 95:
        print(f'{i} процента')
    else:
        print(f'{i} процентов')
