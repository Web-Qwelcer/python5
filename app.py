from modules.module import GetInfo
from modules.module import write_json

x = GetInfo(
    'https://api.privatbank.ua/p24api/exchange_rates?json&date=01.01.2021')
vb = x.get_info()
# print(vb)

g = write_json('gg.json', vb)
