class ZeroDivisionErr(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt


while True:
    try:
        num = int(input('Enter a non-zero number: '))
        if num == 0:
            raise ZeroDivisionErr('You must enter a non-zero number')
    except (ValueError, ZeroDivisionErr) as err:
        print(err)
    else:
        print(num)
        break
