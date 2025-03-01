import math
# yosh = input('yoshingizni kiriting: ')
# try:
#     yosh = int (yosh)
#     # print(f'siz {2021-yosh} yilda ytugilgan ekansiz')
# except:
#     print('Iltimos, yoshningizni!')
# else:
#     print(f'siz {2021-yosh} yilda ytugilgan ekansiz')

# a = int(input('a sonni kiriting: '))
# b = int(input('b sonni kiriting: '))
# try:
#     print('i')
# except:
#     print('Iltimos')
##########################################
#amaliyot

#Topshiriq 1
try:
    a = int(input('a soni kiriting: '))
    b = int(input('b soni kiriting: '))
    print(a/b)
except ZeroDivisionError:
    print('Iltimos, b soni 0 ga teng bo`lmasligi lozim')
except ValueError:
    print('Iltimos, a va b sonlar raqamlardan iborat bo\'lsin')

# Topshiriq 2
try:
    son = int(input('sonni kiriting: '))
    print(math.sqrt(son))
except Exception as e:
    print(f'xatolik: {e}')

# Topshiriq 3
#men hali fayllar bilan ishlash mavzusini o'tmadim

# Topshiriq 4
fishka = True
while fishka == True:
    try:
        massiv = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        indeks = input('indeks(dasturni toxtatish uchun toxta deb yozing): ')
        if(indeks == 'toxta'):
            fishka = False
        else:
            print(massiv[int(indeks)])
    except Exception as e:
        print(f'xatolik: {e}')

