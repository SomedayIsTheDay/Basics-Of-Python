from requests import get, utils
from datetime import datetime

response = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))


def currency_rates(code):
    content = response.split('<Valute ID=')

    for i in content:
        if code.upper() in i:
            print(datetime.strptime(content[0].split('"')[-4], '%d.%m.%Y').date(), ", ", sep="", end="")
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))


print(currency_rates('usd'))
print(currency_rates('huf'))
