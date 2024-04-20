from sys import argv

with open('bakery.csv', 'r+', encoding='utf-8') as count:
    pos, val = argv[1:]
    val = round(float(val.replace(',', '.')), 3)
    for line in range(int(pos)):
        p = count.tell()
        n = count.readline().strip()
        if n == '':
            exit('Error: Строки с такой позицией в документе нет')
    if ',' in str(val) or '.' in str(val):
        if val <= 99999.999:
            count.seek(p)
            count.write(f'{val:>010}')
        else:
            print('Number must be less than 99999.999')
# unbelievably hard :(
