from sys import argv
from itertools import zip_longest

us, hob, out_f = argv[1:]

with open(us, 'r', encoding='utf-8') as users:
    with open(hob, 'r', encoding='utf-8') as hobby:
        users_hobby = zip_longest((' '.join(us.split(',')) for us in users), hobby, fillvalue=None)

        with open(out_f, 'w', encoding='utf-8') as f:
            for i in users_hobby:
                print(f'{str(i[0]).strip()}:: {str(i[1]).strip()}', file=f)
# print(argv)
# enter the name of files from the terminal
