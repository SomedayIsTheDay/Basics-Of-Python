import re


def email_parse(email_address):
    try:
        email = re.match(r'(?P<username>\w+)@(?P<domain>\w.+)', email_address)
        return email.groupdict()
    except Exception:
        raise ValueError(f'wrong email: {email_address}')


try:
    print(email_parse(input('Введите email: ')))
except ValueError as e:
    print(e)
