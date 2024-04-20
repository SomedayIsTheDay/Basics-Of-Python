import collections
with open('parsed_logs', 'w', encoding='utf-8') as w:
    with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
        content = (f'{line.split()[0]} {line.split()[5][1:]} {line.split()[6]}' for line in f)
        for i in content:
            print(i, file=w)
            # print(i) <-- task 1
with open('parsed_logs', 'r', encoding='utf-8') as w:
    my_dict = collections.Counter()
    for i in w:
        i = i.split()[0]
        my_dict[i] += 1
    ip, count = my_dict.most_common()[0][0], my_dict.most_common()[0][1]
    print(f'Spammer {ip} - {count} times')  # <-- task 2
