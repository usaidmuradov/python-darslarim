# #1. Oʻzgaruvchilar va maʼlumot turlari

# #1-masala
# ism = input('ismingizni kiriting: ')
# familiya = input('familiyangizni kiriting: ')
# yosh = int(input('yoshingizni kiriting: '))
# tugilgan_yil = 2024 - yosh
# print(f'\nSizning ismingiz {ism}, familiyangiz {familiya}, va siz {tugilgan_yil}-yilda tugilgansiz')
# #2-malasa
# a = int(input('a soninizni kiriting: '))
# print(a)
# b = int(input('siz ishlayotgan dasturlash tilini kiriting: '))
# print(f'{b} dasturi')

# #2. Matn bilan ishlash

# # 1-masala
# # 2-masala

# #3. Roʻyxatlar va ularning metodlari
# # 1-masala
# mevalar = ["olma", "banan", "uzum"]
# mevalar.append('anjir')
# mevalar.remove('uzum')
# print(mevalar)
# # 2-masala
# sonlar = []
# while True:
#     son = int(input('sonni kiriting: '))
#     sonlar.append(son)
#     takrorlash = input('yana son qoshishni istaysizmi(ha/yoq)? ')
#     if takrorlash == 'yoq':
#         break
#     else:
#         continue
# print(f'kiritilgan sonlarning eng kichigi: {min(sonlar)}')
# print(f'kiritilgan sonlarning eng kattasi: {max(sonlar)}')

# #4. Shart operatorlari

# # 1-masala
# son = int(input('sonni kiriting: '))
# if son > 0:
#     print(f'{son} soni musbat')
# elif son < 0:
#     print(f'{son} soni manfiy')
# else:
#     print(f'{son} soni, manfiy ham emas, musbat ham emas')
# # 2-masala
# yosh = int(input('Yoshingizni kiriting: '))
# if yosh > 18:
#     print('Siz voyaga yetgansiz')
# else:
#     print('Siz voyaga yetmagansiz')

# # 5. Takrorlanish operatorlari

# # 1-masala
# min = int(input('oraliq boshini kiriting: '))
# max = int(input('oraliq oxirini kiriting: '))
# for i in range(min, max+1):
#     print(i)
# # 2-masala
# while True:
#     son = int(input('sonni kiriting: '))
#     print(son**2)
#     takrorlash = input('yana son qoshishni istaysizmi(ha/yoq)? ')
#     if takrorlash == 'yoq':
#         break

# # sinov savollari
# #1-savol: Python-da list va tuple oʻrtasidagi farqlarni tushuntiring.
# #javob: list ustida biz xohlagancha amallar bajarishimiz mumkin, unga elemnt qoshish, element olib tashla va hokozo, tuple esa ozgarmasdir, agar uni ozgartirmoqchi bolsak ham oldin uning type ni list ga ozgartirishimiz kerak
# #2-savol: Quyidagi kod nima chiqadi?
# #javob: Katta

# matn = " Python Python python pytHon"
# print(matn.count("Python"))  # 2

# Topshiriq 1: Matndan so‘zlar sonini hisoblash
# soz = input('gap kiriting: ')
# print(len(soz.split()))

# # Topshiriq 2: Belgilarni hisoblash
# soz = input('sozni kiriting: ')
# if soz.isalpha() == True:
#     print(len(soz))
# else:
#     print('Bu soz harflardan iborat emas')

# # Topshiriq 3: Matnni teskari o‘girish
# matn = input('matn kiriting: ')
# print(matn[::-1])

# # Topshiriq 4: Gapni so‘zlarga ajratish va qayta birlashtirish
# matn = input('matn kiriting: ')
# matn1 = matn.split()
# matn2 = " ".join(matn1)
# print(matn2.title())

# # Topshiriq 5: Belgi sanash
# matn = input('matn kiriting: ')
# takror = input('takror sozni kiriting: ')
# print(f'"{takror}" sozi matnda {matn.count(takror)} marta qatnashgan')

# talabalar = []

# def talaba_qosh():
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     yosh = int(input("Yoshi: "))
#     fakultet = input("Fakulteti: ")
#     bosqich = int(input("Bosqichi: "))
#     baholar = {}
#     while True:
#         fan = input("Fan nomini kiriting (yoki 'stop' yozib tugating): ")
#         if fan.lower() == 'stop':
#             break
#         baho = int(input(f"{fan} fanidan baho: "))
#         baholar[fan] = baho
#     talaba = {
#         "ism": ism,
#         "familiya": familiya,
#         "yosh": yosh,
#         "fakultet": fakultet,
#         "bosqich": bosqich,
#         "baholar": baholar
#     }
#     talabalar.append(talaba)

# def talaba_korish():
#     for talaba in talabalar:
#         print(f"\nTalaba: {talaba['ism']} {talaba['familiya']}")
#         print(f"Yoshi: {talaba['yosh']}, Fakulteti: {talaba['fakultet']}, Bosqichi: {talaba['bosqich']}")
#         print("Baholar:")
#         for fan, baho in talaba['baholar'].items():
#             print(f"  {fan}: {baho}")

# def baholar_tahlili():
#     for talaba in talabalar:
#         print(f"\n{talaba['ism']} {talaba['familiya']}ning qayta topshirishi kerak bo‘lgan fanlari:")
#         qayta_topshirish = [fan for fan, baho in talaba['baholar'].items() if baho < 3]
#         if qayta_topshirish:
#             print(", ".join(qayta_topshirish))
#         else:
#             print("Hamma baholari yaxshi!")

# def boshqaruv():
#     while True:
#         print("\n[1] Talaba qo‘shish")
#         print("[2] Talabalarni ko‘rish")
#         print("[3] Baholarni tahlil qilish")
#         print("[4] Chiqish")
#         tanlov = input("Tanlovni kiriting: ")
#         if tanlov == '1':
#             talaba_qosh()
#         elif tanlov == '2':
#             talaba_korish()
#         elif tanlov == '3':
#             baholar_tahlili()
#         elif tanlov == '4':
#             break
#         else:
#             print("Noto‘g‘ri tanlov, qayta urinib ko‘ring!")

# boshqaruv()

# talabalar = []
# ism = input('ismingizni kiriting: ')
# familiya  = input('familiyangizni kiriting: ')
# yosh = input('yoshingizni kiriting: ')
# fakultet = input('Fakultetingizni kiriting: ')
# fan = input('baholnishi kerak bolgan fan nomini kiriting: ')
# baxo = input(f'{fan}dan baxosini kiriting: ')




############################
#noldan takrorlash
# print(type(3.13))
# print(type(12))
# print(type('qwert'))
ismim = 'umar'
# print('men ' + ismim +'man')

taomlar = ['garoh', 'honim', 'grechrxa', 'mosh']
sonlar = (1, 2, 3, 4)
# type(sonlar) = 'list'
# print(type(sonlar))
son = list(sonlar)
son.append(4)
# print(son)

friends = []
friends.append('diyor')
friends.append('farrux')
friends.append('avazbek')
friends.append('samandar')
friends.append('ayyub')
friends.append('abror')
# print(friends)
friends.remove('abror')
# print(friends)
mehmonlar = []
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(2))
# print(mehmonlar)

mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
# print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
# print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)

son = [1]
sonlar = son[:]
sonlar.append(2)
sonlar.append(3)
# print(son)
# print(sonlar)
s=0
ismlar = ['farrux', 'ayyub', 'oysha', 'nux', 'davron']
for ism in ismlar:
    # print(f'Xush kelibsan {ism}')
    s += 1
# print(f'kod {s} marta takrorlandi')

# toqSonlar = list(range(11, 101, 2))
# print(toqSonlar)
# for son in range(11, 100, 2):
    # print(son**3)

# kinolar = []
# for k in range(5):
#     kinolar.append(input(f'{k+1}-kino nomini kiriting: '))
# print(kinolar)

# soni = int(input('Bugun nechta odam bilan suhbatlashdingiz: '))
# odamlar = []
# for son in range(soni):
#     odamlar.append(input(f'{son+1}-insonning ismini kiriting: '))
# print(odamlar)

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm':
#         print(car)
#     else:
#         print(car.upper())

# ism = input('Ismingizni kiriting: ')
# if ism == 'admin':
#     print('Xush kelibsiz, Admin. Foydalanuvchilar ro\'yxatini ko\'rasizmi?')
# else:
#     print(f'Xush kelibsan {ism}')

# yosh = int(input('Yoshingizni kiriting: '))
# if yosh < 4 or yosh > 60:
#     print('sizga kirish bepul')
# else:
#     print('sizga kirish narxi 5000 so\'m')

# mahsulotlar = ['olma', 'guruch', 'garoh', 'kartoshka', 'piyoz', 'sabzi', 'xurmo', 'somsa', 'shashlik', 'grechexa']
# savat = []
# bor_mahsulotlar = []
# yoq_mahsulotlar = []
# for i in range(5):
#     savat.append(input('olinishi kerak bolgan mahsulotlarni kiriting: '))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else: 
#         yoq_mahsulotlar.append(mahsulot)
# if yoq_mahsulotlar:
#     print(f'quyidagi mahsulotlar dokonimizda yoq: {yoq_mahsulotlar}')
# else:
#     print('bizda barcha mahsulotlar bor')

# sevimli = {
#     'dadam':'osh',
#     'onam':'shorva', 
#     ' ukam':'garoh'
# }

# for ism, taom in sevimli.items():
#     print(f'{ism}ning sevimli taomlari: {taom}')
# ism = input('ismni kiriting: ').lower()
# print(sevimli.get(ism, 'mavjud emas'))


talaba = {
    'ism': 'umar',
    'familiya': 'saidmuradov',
    'yosh': 19,
    'universitet': 'NamDU',
    'fakultet': 'Matematika',
    'kurs': 4
}

# for kalit, qiymat in talaba.items():
#     print(f'{kalit}: {qiymat}')

# print(talaba.keys())

# for key in talaba.keys():
#     print(key)


bozorlik = ['anjir', 'kartoshka', 'salat', 'olma']

mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }

# for mahsulot in bozorlik:
#     if mahsulot in mahsulotlar: 
#         print(f'{mahsulot}ning narxi: {mahsulotlar[mahsulot]}')
    
# for mahsulot in bozorlik:
#     if mahsulot not in mahsulotlar:
#         print(f'iltimos {mahsulot}ni ham dokoningizga olib keling')
# print('dokonizmdagi mahsulotlar:')
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.capitalize())

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }
# for telefon in set(telefonlar.values()):#set har biridan bittadan oib chiqib beradi
#     print(telefon.capitalize())

#######################
tarjima_sozlar = {
    'amazing': 'ajoyib',
    'awful': 'dahshatli',  # "daxshatli" emas, "dahshatli" to'g'ri
    'view': 'manzara',
    'weather': 'ob-havo',
    'both': 'ikkalasi',
    'excited': 'hayajonlangan',  # "exsited" emas, "excited" to'g'ri
    'interview': 'suhbat',
    'sure': 'ishonchli',  # "ishonmoq" emas, "ishonchli" yoki "ishonaman" to'g'ri
    'see': 'ko‘rmoq',  # "qaramoq" emas, "see" ko'rmoq ma'nosida ishlatiladi
    'nervous': 'asabiy',
    'nurse': 'hamshira',
    'receptionist': 'qabulxona hodimi',
    'tomorrow': 'ertaga',
    'twin': 'egizak',
    'waitress': 'ofitsiant qiz'  # "waitres" emas, "waitress" to'g'ri
}

# for inglizcha in sorted(tarjima_sozlar):
#     print(f'{inglizcha} sozining ozbek tilidagi manosi: {tarjima_sozlar[inglizcha]}')

davlatlar = {
    'O\'zbekiston': 'Toshkent',
    'AQSh': 'Vashington',
    'Rossiya': 'Moskva',
    'Xitoy': 'Pekin',
    'Fransiya': 'Parij',
    'Germaniya': 'Berlin',
    'Braziliya': 'Braziliya shahri',
    'Turkiya': 'Anqara',
    'Italiya': 'Rim',
    'Hindiston': 'Yangi Dehli',
    'Buyuk Britaniya': 'London',
    'Yaponiya': 'Tokio',
    'Kanada': 'Ottava',
    'Misr': 'Qohira',
    'Saudiya Arabistoni': 'Ar-Riyod'
}
# davlat = input('davlat nomini kiriting: ').capitalize()

# if davlat in davlatlar:
#     print(f'{davlat}ning poytaxti: {davlatlar[davlat]}')
# else:
#     print(f'Bizdagi malumotlarda {davlat}ning poytaxti ma\'lum emas')

taomlar = {
    'Osh': 35000,
    'Manti': 30000,
    'Somsa': 10000,
    'Shashlik': 25000,
    'Lag‘mon': 40000,
    'Chuchvara': 32000,
    'Norin': 45000,
    'Shorva': 38000,
    'Qozon kabob': 60000,
    'Beshbarmoq': 50000,
    'Mastava': 28000,
    'Qaynatma sho‘rva': 35000,
    'Gushtli do‘lma': 37000,
    'Holva': 15000,
    'Chak-chak': 18000
}
# s=0
# for buyurtma in range(3):
#     taom = input(f'{buyurtma+1}-taomni nomini yozing: ').capitalize()
#     if taom in taomlar:
#         print(f'{taom}ning narxi: {taomlar[taom]}')
#         s=s+taomlar[taom]
#     else: 
#         print('Afsuski bunday taom mavjud emas')
    
# print(f'Barcha taomlarning narxi: {s}')

######################

buxoriy = {
    'ism': 'Abu Abdulloh Muhammad ibn Ismoil',
    'tyil': 810,
    'vyil': 870,
    'tjoy': 'Buxoro',
    'kitoblari': [
        "Al-Jome' as-Sahih",
        "Al-Adab al-Mufrad",
        "At-Tarix al-Kabir"
    ]
}

beruniy = {
    'ism': 'Abu Rayhon Beruniy',
    'tyil': 973,
    'vyil': 1048,
    'tjoy': 'Kat, Xorazm',
    'kitoblari': [
        "Qadimgi xalqlardan qolgan yodgorliklar",
        "Hindiston",
        "Geodeziya"
    ]
}

ibn_sino = {
    'ism': 'Abu Ali Ibn Sino',
    'tyil': 980,
    'vyil': 1037,
    'tjoy': 'Afshona, Buxoro',
    'kitoblari': [
        "Tib qonunlari",
        "Donishnoma",
        "Najot"
    ]
}

farobiy = {
    'ism': 'Abu Nasr al-Farobiy',
    'tyil': 872,
    'vyil': 950,
    'tjoy': 'Farob, O‘tror',
    'kitoblari': [
        "Fozil odamlar shahri",
        "Aql ma'nosi haqida risola",
        "Baxtga erishish haqida"
    ]
}

mirzo_ulugbek = {
    'ism': 'Mirzo Ulug‘bek',
    'tyil': 1394,
    'vyil': 1449,
    'tjoy': 'Sultoniya, Eron',
    'kitoblari': [
        "Zijji jadidi Ko‘ragoniy",
        "Tashkent rasadxonasi kuzatuvlari",
        "Yulduzlar jadvali"
    ]
}

al_xorazmiy = {
    'ism': 'Muhammad ibn Musa al-Khwarizmi',
    'tyil': 780,
    'vyil': 850,
    'tjoy': 'Xorazm',
    'kitoblari': [
        "Hisob al-jabr val-muqobala",
        "Zij al-Sindhind",
        "Yerning shakli haqida risola"
    ]
}

buyuklar = [buxoriy, beruniy, ibn_sino, farobiy, mirzo_ulugbek, al_xorazmiy]

# for shaxs in buyuklar:
#     print(f'{shaxs['ism']}, {shaxs['tyil']}-yilda, {shaxs['tjoy']}da tugilgan va {shaxs['vyil']}-yilda vafot etgan')
# for shaxs in buyuklar:
#     print(f'{shaxs['ism']}ning kitoblari:')
#     for kitob in shaxs['kitoblari']:
#         print(kitob)
#     print()

# kinolar = {
#     'umar': ['Umar ibn Xattob', 'Panjara ortida', 'Jeyson Born'],
#     'farux': ['Terminator', 'osmondagi bolalar'],
#     'al-xorazmiy': ['Osmondagi bolalar', 'Kafirat', 'Al-Quran']
# }

# for ism in kinolar:
#     print(f'{ism}ning sevimli kinolari:')
#     for kino in kinolar[ism]:
#         print(kino)
#     print()

# ism = input('ismingizni kiriting: ')
# kinolar = []
# for kino in range(3):
#     kinolar.append(input(f'{kino+1}-kino nomini yozing: '))
# print(kinolar)

# kinolar = {}


davlatlar = {
    'uzbekistan' : {
        'nomi': 'O‘zbekiston',
        'poytaxt': 'Toshkent',
        'maydon': 448978,  # kv.km
        'aholi': 36000000,  # taxminiy soni
        'pul_birligi': 'So‘m',
        'rasmiy_tili': 'O‘zbek tili'
    },

    'aqsh' : {
        'nomi': 'Amerika Qo‘shma Shtatlari',
        'poytaxt': 'Vashington',
        'maydon': 9834000,
        'aholi': 332000000,
        'pul_birligi': 'AQSh dollari',
        'rasmiy_tili': 'Rasmiy til yo‘q (ammo ingliz tili keng qo‘llanadi)'
    },

    'xitoy' : {
        'nomi': 'Xitoy Xalq Respublikasi',
        'poytaxt': 'Pekin',
        'maydon': 9597000,
        'aholi': 1412000000,
        'pul_birligi': 'Yuan',
        'rasmiy_tili': 'Xitoy tili (mandarin lahjasi)'
    },

    'rossiya' : {
        'nomi': 'Rossiya Federatsiyasi',
        'poytaxt': 'Moskva',
        'maydon': 17098242,
        'aholi': 144400000,
        'pul_birligi': 'Rubl',
        'rasmiy_tili': 'Rus tili'
    },

    'hindiston' : {
        'nomi': 'Hindiston',
        'poytaxt': 'Yangi Dehli',
        'maydon': 3287263,
        'aholi': 1408000000,
        'pul_birligi': 'Rupiya',
        'rasmiy_tili': 'Hind tili, Ingliz tili'
    }

}
# davlat = input('Qaysi davlat haqida malumot kerak: ')

# if davlat in davlatlar:
#     malumot = davlatlar[davlat]
#     print(f'\n{davlat}ning poytaxti: {malumot['poytaxt']}'
#         f'\nMaydoni: {malumot['maydon']}'
#         f'\nAaholi soni: {malumot['aholi']}'
#         f'\nPul birligi: {malumot['pul_birligi']}'
#         f'\nRasmiy tili: {malumot['rasmiy_tili']}')
# else: 
#     print('Bunday davlat haqida malumit yoq')


#####################################
# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating

# kitoblar = []
# while True:
#     kitob = input('Yangi kitob nomini kiriting (stop kiritish uchun "stop" tugmasini bosing): ')
#     if kitob == 'stop':
#         break

# while True:
#     yosh = input('Yoshingizni kiriting: ')
#     if yosh == 'exit':
#         break
#     elif int(yosh)<7:
#         print('Sizga kirish narxi-2000 so\'m')
#     elif(int(yosh)>=7 and int(yosh)<=18):
#         print('Sizga kirish narxi-3000 so\'m')
#     elif(int(yosh)>18 and int(yosh)<65):
#         print('Sizga kirish narxi-10000 so\'m')
#     elif(int(yosh)>=65):
#         print('Sizga kirish bepul')
#     else:
#         print('iltimos faqat yoshingizni kiriting, yoki exit deb yozing')

# fishka = True
# while fishka == True:
#     yosh = input('Yoshingizni kiriting: ')
#     if yosh == 'exit':
#         fishka = False
#     elif int(yosh)<7:
#         print('Sizga kirish narxi-2000 so\'m')
#     elif(int(yosh)>=7 and int(yosh)<=18):
#         print('Sizga kirish narxi-3000 so\'m')
#     elif(int(yosh)>18 and int(yosh)<65):
#         print('Sizga kirish narxi-10000 so\'m')
#     elif(int(yosh)>=65):
#         print('Sizga kirish bepul')
#     else:
#         print('iltimos faqat yoshingizni kiriting, yoki exit deb yozing')


savol = "Musbat son kiriting(dasturni to'xtatish uchun 'exit' deb yozing): "

# qiymat = input(savol)

# while True:
#     qiymat = input(savol)
#     if qiymat.capitalize()=='Exit':
#         break
#     elif int(qiymat)<0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")


#####################################

# taomlar = []
# while True:
#     mahsulot = input('Mahsulot nomini kiriting(Toxtatishg uchun exit deb yozing): ')
#     if mahsulot.capitalize()=='Exit':
#         break
#     else: 
#         taomlar.append(mahsulot)
# print(taomlar)


# mahsulotlar = {} 
# while True:
#     mahsulot = input('Mahsulot nomini kiriting(Toxtatish uchun exitni bosing): ')
#     if mahsulot == 'exit':
#         break
#     else: 
#         narx = input(f'{mahsulot}ning narxini kiriting: ')  
#         mahsulotlar[mahsulot] = int(narx)
     
# while taomlar:
#     buyurtma = taomlar.pop() 
#     if buyurtma in mahsulotlar.keys():
#         print(f'{buyurtma}ning narxi: {mahsulotlar[buyurtma]}')
#     else:
#         print(f'afsuski bizda {buyurtma} yoq')


#################################

# def salom_ber(ism):
#     ism = input('ismingizni kiriting: ')
#     print(f'salom, {ism}')
# salom_ber(ism)

# def tugilgan_yil():
#     print(f'{ism} {2025-yosh}-yilda tugilgan')
# ism = input('imsingizni kiriting: ')
# yosh = int(input('yoshingizni kiriting: '))

# tugilgan_yil()

# def tekshir():
#     for raqam in range(2,11):
#         if son%raqam == 0:
#             print(f'{son} {raqam} ga bo\'linadi')
#         else:
#             print(f'{son} {raqam} ga bo\'linmaydi')
# son = int(input('sonni kiriting: '))
# tekshir()

###################################
# def oraliq(min, max, qadam):
#     sonlar = [] 
#     while min<max:
#         sonlar.append(min)
#         min += qadam
#     return sonlar
# print(oraliq(1, 15, 2))

# def talaba_malumot(ismi, familiya, fakultet, yonalishi, t_yil=None):
#     talaba = {
#         'ismi': ismi,
#         'familiya': familiya,
#         'fakultet': fakultet,
#         'yonalishi': yonalishi,
#         'tugilgan yili': t_yil
#     }
#     return talaba

# print('Bizda ro‘yxatda bo‘lgan talabalar ma’lumotlarini taqdim etamiz:')
# talabalar = []

# while True:
#     print('Quyidagi ma’lumotlarni kiriting:')
#     ismi = input('Ismi: ')
#     familiya = input('Familiyasi: ')
#     fakultet = input('Fakulteti: ')
#     yonalishi = input('Yo‘nalishi: ')
    
#     t_yil = input('Tug‘ilgan yili (agar noma’lum bo‘lsa, bo‘sh qoldiring): ')
#     t_yil = int(t_yil) if t_yil.isdigit() else None  # Faqat raqam bo‘lsa, int ga o‘giramiz
    
#     talabalar.append(talaba_malumot(ismi, familiya, fakultet, yonalishi, t_yil))
    
#     yana = input('Yana ma’lumot kiritishni istaysizmi? (ha/yoq): ')
#     if yana.lower() == 'yoq':  # Katta-kichik harflarni inobatga olmaslik uchun
#         break

# for talaba in talabalar:
#     t_yil = talaba['tugilgan yili'] if talaba['tugilgan yili'] else 'Nomalum'
#     print(f"\nIsm-familiyasi: {talaba['ismi']} {talaba['familiya']}, {t_yil}-yilda tug‘ilgan, {talaba['fakultet']} fakultetining {talaba['yonalishi']} yo‘nalishida o‘qiydi.")



# def malumot_oluvchi(ismi, familiyasi, t_yili, oqish_joyi, tel_raqami=None, e_manzil=None):
#     malumotlar = {
#         'ism': ismi,
#         'familiyasi': familiyasi,
#         'tugilgan_yili': t_yili,
#         'yoshi': 2025 - t_yili,
#         'oqish_joyi': oqish_joyi,
#         'telefon_raqami': tel_raqami if tel_raqami else 'Nomalum',
#         'elektron_manzil': e_manzil if e_manzil else 'Nomalum'
#     }
#     return malumotlar

# malumotlar = []

# while True:
#     print('Quyidagi ma’lumotlarni kiriting:')
#     ismi = input('Ismi: ')
#     familiyasi = input('Familiyasi: ')
    
#     t_yili = int(input('Tug‘ilgan yili: '))
            

#     oqish_joyi = input('O‘qish joyi: ')
#     tel_raqami = input('Telefon raqami (yoki bosh qoldiring): ').strip()
#     e_manzil = input('Elektron manzil (yoki bosh qoldiring): ').strip()

#     # Ma'lumotlarni ro‘yxatga qo‘shish **shartdan oldin** bajariladi!
#     malumotlar.append(malumot_oluvchi(ismi, familiyasi, t_yili, oqish_joyi, tel_raqami, e_manzil))

#     # Shundan keyin, yana ma'lumot kiritish so‘raladi
#     davr = input('Yana ma’lumot kiritishni istaysizmi? (ha/yoq): ').lower()
#     if davr == 'yoq':
#         break

# # Natijalarni chiqarish
# for malumot in malumotlar:
#     print(f"\nIsm: {malumot['ism']}, Familiya: {malumot['familiyasi']}, Tug‘ilgan yili: {malumot['tugilgan_yili']}, "
#           f"Yoshi: {malumot['yoshi']}, O‘qish joyi: {malumot['oqish_joyi']}, "
#           f"Telefon raqami: {malumot['telefon_raqami']}, Elektron manzil: {malumot['elektron_manzil']}")
# sonlar = []
# for son in range(3):
#     son = input(f'{son+1}-sonni kiriting: ')
#     sonlar.append(son)
# print(max(sonlar))

# def kattasini_top(a, b, c):
#     return max(a, b, c)
# print(kattasini_top(2, 56, -19))

# radius = input('radiusni kiriting: ')
# def aylana(r):
#     aylana_malumotlari = {
#         'radius': r,
#         'diametri': 2*r,
#         'uzunligi': 2*r*3.14,
#         'yuzasi': r**2*3.14
#     }
#     return aylana_malumotlari
# print(aylana(10))

# def tub_sonlarni_top(min, max):
#     sonlar = list(range(min, max+1))
#     tub_sonlar = []
#     for son in sonlar:
#         for tub in range(2, int(son**0.5) + 1):
#             if son % tub == 0:
#                 break
            
#         else:
#             if son > 1:
#                 tub_sonlar.append(son)
#     return tub_sonlar

# print(tub_sonlarni_top(1, 30))

# def tub_sonlarni_top(min, max):
#     sonlar = list(range(min, max+1))
#     tub_sonlar = []
#     for son in sonlar:
#         tub = True  # Avval sonni tub deb hisoblaymiz
#         for boluvchi in range(2, int(son**0.5) + 1):
#             if son % boluvchi == 0:
#                 tub = False  # Agar bo‘linib qolsa, tub emas
#                 break
#         if tub==True and son > 1:  # Agar tub bo‘lsa va 1 dan katta bo‘lsa
#             tub_sonlar.append(son)
#     return tub_sonlar

# print(tub_sonlarni_top(500, 1000))

# son = input('sonni kiriting(toxtatish uchun exit deb yozing): ')
# for tub in range(2, int(int(son)**0.5)+1):
    
#     if int(son) % tub != 0:
#         print(f'{son} tub son')
#         break
#     else: 
#         print(f'{son} - tub son emas')
#         break
# son = int(input('sizga nechta fibonachi son kerak: '))
# def fibonachi_sonlarni_top(son):
#     fibonachi_sonlar = [1, 1]
#     if son > 2:
#         while (son-2):
#             fibonachi_sonlar.append(fibonachi_sonlar[-1]+fibonachi_sonlar[-2])
#             son = son - 1
#         return fibonachi_sonlar
#     elif son == 2:
#         return fibonachi_sonlar
#     elif son < 2:
#         print("iltimos 2 yoki undan katta son kiriting")
# print(fibonachi_sonlarni_top(0))

# def fibonachi_sonlarni_top(son):
#     fibonachi_sonlar = [1, 1]  # Har safar yangi ro‘yxat hosil qilinadi
#     if son > 2:
#         while (son - 2):
#             fibonachi_sonlar.append(fibonachi_sonlar[-1] + fibonachi_sonlar[-2])
#             son -= 1
#         return fibonachi_sonlar
#     elif son == 2:
#         return fibonachi_sonlar
#     else:
#         print("Iltimos, 2 yoki undan katta son kiriting")
#         return []

# print(fibonachi_sonlarni_top(1))

################################
 
# sozlar = []
# for i in range(3):
#     sozlar.append(input(f'{i+1}-sozni kiriting: '))
# def katta_harfga_aylantir():
#     katta_harfli_sozlar = []
#     for soz in sozlar:
#         katta_soz = soz.title()
#         katta_harfli_sozlar.append(katta_soz)
#     return katta_harfli_sozlar

# print(katta_harfga_aylantir())

# def katta_harfga_aylantir(sozlar):
#     return [soz.title() for soz in sozlar]
# sozlar = ['python', 'java', 'c++']
# sozlar2 = sozlar[:]

# print(katta_harfga_aylantir(sozlar2))
# print(sozlar)
# print(sozlar2)
# ismlar = ['umar', 'farrux', 'davron', 'ayub']
# ismlar2 = ismlar[:]
# def baholar(ismlar2):
#     baholar = {}
#     for ism in ismlar2:
#         baholar[ism.title()] = int(input(f'Talaba {ism.title()} ni baholang: '))
#     return baholar
# print(baholar(ismlar2))
# print(ismlar)


# def summa(*sonlar):
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi

# # print(summa(1, 2, 3, 4, 5))

# def summa2(*sonlar):
#     return sum(sonlar)

# # print(summa2(1, 2, 3, 4, 5))

# def kopaytma(x, y, *sonlar):
#     return x * y * sum(sonlar)
# print(kopaytma(2))

# def malumot(ism, familiya, *talabalar):
#     malumotlar = {}
#     for talaba in talabalar:

# def talaba_info(ism, familiya, **kwargs):
#     kwargs['ism']=ism
#     kwargs['familiya']=familiya
#     return kwargs

# talaba = talaba_info('olim','olimov',tyil=1995,fakultet='IT',yonalish='AT', yoshi = '30')

# # print(talaba)


# ################################
# import math
# uzunlik = lambda pi, radius : 2*pi*radius
# # print(uzunlik(math.pi, 100))

# kvadrat = lambda x, y : x**y
# # print(kvadrat(3, 4))

# def daraja(n):
#     return lambda x : x**n

# kvadrat = daraja(2)

# sonlar = list(range(11))
# ildi = list(map(math.sqrt, sonlar))
# # print(ildi)

# def kvadrati(x):
#     return x*x
# kvadrat_sonlar = list(map(kvadrati, sonlar))
# # print(kvadrat_sonlar)

# kvadratlar = list(map(lambda x: x**2, sonlar))
# # print(kvadratlar)

# a = [2, 3, 4]
# b = [5, 6, 7]
# a_plus_b = list(map(lambda x, y: x+y, a, b))
# # print(a_plus_b)

# import random 
# sonlar = random.sample(range(100), 10)
# # print(sonlar)

# def juftmi(x):
#     return x % 2 == 0
# juft_sonlar = list(filter(juftmi, sonlar))
# # print(juft_sonlar)

# mevalar = ['olma', 'anor', 'anjir', 'behi', 'xurmo', 'tarvuz']
# harf = 'b'
# mevalar_b = list(filter(lambda meva: meva.startswith(harf), mevalar))
# # print(mevalar_b)

# mevalar2 = list(filter(lambda meva: len(meva)<=5, mevalar))
# # print(mevalar2)
# #oddiy funksiyada:
# def kv_oshir():
#     kv = []
#     for son in range(10):
#         son = son**2
#         kv.append(son)
#     return kv
# # print(kv_oshir())

# #lambda funksiyada:
# # print(list(map(lambda son: son**2, range(10))))

# #oddiy funksiyada:
# def mus_son_top():
#     mus_sonlar = []
#     for son in range(-10, 10):
#         if son>0:
#             mus_sonlar.append(son)
#     return mus_sonlar
# # print(mus_son_top())

# #lambda funksiyada:
# mus_sonlar = list(filter(lambda son: son>0, range(-10, 10)))
# # print(mus_sonlar)

# #oddiy funksiyada:
# def mus_son_top():
#     kv_sonlar = []
#     for son in range(-10, 10):
#         if son>0:
#             kv_sonlar.append(son**2)
#     return kv_sonlar
# # print(mus_son_top())

# #lambda funksiyada:
# mus_sonlar = list(filter(lambda son: son>0, range(-10, 10)))
# kv = list(map(lambda son: son**2, mus_sonlar))
# print(kv)