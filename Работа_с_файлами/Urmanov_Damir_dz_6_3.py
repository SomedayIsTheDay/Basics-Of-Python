import json
from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        if len(users.readlines()) >= len(hobby.readlines()):
            users.seek(0)
            hobby.seek(0)
            with open('users_hobby.json', 'w', encoding='utf-8') as f:
                users_hobby = zip_longest((' '.join(us.split(',')) for us in users), hobby, fillvalue=None)
                users_hobby_dict = dict(users_hobby)
                a = {str(i[0]).strip(): str(i[1]).strip() for i in users_hobby_dict.items()}
                json.dump(a, f, ensure_ascii=False, indent=1)
        else:
            exit(1)
