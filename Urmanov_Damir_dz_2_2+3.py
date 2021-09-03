my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(my_list)
my_list.insert(1, '"')
my_list.insert(3, '"')
my_list.insert(5, '"')
my_list.insert(7, '"')
my_list.insert(12, '"')
my_list.insert(14, '"')
my_list[2] = '0' + '5'
my_list[13] = '+' + '0' + '5'
print(my_list)
print(' '.join(my_list).replace('" 05 "', '"05"').replace('" 17 "', '"17"').replace('" +05 "', '"+05"'))
