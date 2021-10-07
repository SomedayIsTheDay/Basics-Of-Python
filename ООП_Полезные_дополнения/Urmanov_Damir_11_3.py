class OnlyInt(ValueError):
    def __init__(self, txt):
        self.txt = txt


nums_list = []
while True:
    try:
        num = input('Enter a number: ')
        if num.isdigit():
            nums_list.append(num)
        elif num == 'stop':
            print(nums_list)
            break
        else:
            raise OnlyInt('Must be int!')
    except OnlyInt as err:
        print(err)
