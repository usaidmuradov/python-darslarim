# import datetime as dt # datetime moduli
from datetime import datetime, date, time, timedelta # datetime modulidan aynan datetime obyektini import qilib olyapman
# print(f'Bugungi sana: {datetime.now()}')
# print(f'30 kundan keyingi sana: {(datetime.now()+timedelta(days=30)).date()}')
# print(f'Yil: {date.today().year}')
# print(f'Yil: {date.today().month}')
# print(f'Yil: {date.today().day}')
# print(f'2025-07-20 sanasini Yakshanbaga({datetime(2025, 7, 20).isoweekday()}) ga togri keladi')
# sana1 = datetime(2025, 3, 6)
# sana2 = datetime(2024, 12, 25)
# print(sana1 - sana2)
####################

import math
pi = math.pi
natural_logorifm = math.e
# print(math.degrees(pi))
from math import sqrt
# print(sqrt(9))

import re
word1 = 'umar'
word2 = 'davron'
word3 = 'farrux'
word4 = 'ayyub'
# andoza = '^d....n$'
# print(re.match(andoza, word1))
# print(re.match(andoza, word2))

andoza = '^[a-z0-9_-]{3,15}$'
sozlar = [
    "olma", "kitob", "dastur", "qalam", "uy", "dost", "musiqa", "kocha", "choy", "tog",
    "dengiz", "qish", "bahor", "yoz", "kuz", "oyin", "muhabbat", "xayol", "galaba", "ormon",
    "yulduz", "quyosh", "oy", "bulut", "shamol", "yomgir", "hayot", "havo", "vaqt", "tarix",
    "mehnat", "tashvish", "orzu", "umid", "sevinch", "hayajon", "tofon", "ishonch", "dono", "chiroq",
    "kecha", "bugun", "ertaga", "qiziqish", "shirin", "achchiq", "tuz", "koz", "quloq", "burun", "oyoq",
    "qol", "barmoq", "yurak", "jigar", "chiroy", "ovoz", "jannat", "daryo", "kema", "sahro", "yer",
    "suv", "oziq", "issiq", "sovuq", "toza", "chang", "yurish", "yotish", "otirish", "organish", "oqish",
    "yozish", "chizish", "harakat", "mashina", "velosiped", "yol", "koprik", "qizil", "moviy", "yashil", "oq",
    "qora", "sariq", "yashash", "olim", "ogriq", "kuch", "odam", "ona", "ota", "bola", "aka", "uka", "opa",
    "singil", "sogliq", "baxt"
]

for soz in sozlar:
    username = re.match(andoza, soz)
    # print(username)

matn  = """
Salom, Aziz! Mening yangi email manzilim azizbek1995@gmail.com, agar muhim narsa bo‘lsa shu yerga yoz.  
Shuningdek, ish uchun bizning kompaniya support@company.uz email manzilidan foydalanishing mumkin.  
Agar IT bo‘yicha savollaring bo‘lsa, mentorimiz alisher.dev@tech.io bilan bog‘lan.  

Bundan tashqari, bizning jamoamiz a'zolari bilan quyidagi email manzillar orqali bog‘lanishing mumkin:  
- Mahmud: mahrn@business.com  
- Laylo: laylo_qa@soft.uz  
- Sherzod: sherzod95@developer.net  

Agar qo‘shimcha ma'lumot kerak bo‘lsa, admin@website.org orqali bog‘lanishing mumkin.
"""
# andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
# email = re.findall(andoza, matn)
# # print(email)

# andoza = '^(?=.*?[AZ])(?=.*?[az])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
# while True:
#     msg = input('Yangi parol kiriting: ') 
#     if re.match(andoza, msg):
#         print('parol qabul qilindi')
#         break
#     else:
#         print('xato')

############################
bugun = date.today()
fishka = 0
while fishka<10:
    bugun1 = bugun + fishka * timedelta(weeks=2)
    # print(bugun1)
    fishka += 1
bugun = date.today().day
hayit = datetime(2025, 3, 31).date().day
# print(f'Hayitgacha {hayit - bugun} kun qoldi')

# from datetime import date, timedelta







