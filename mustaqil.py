# S.isdigit() - Satrda raqamlar ishtirok etganligini tekshirish.
# S.isalpha() - Satr faqat harflardan iboratligini tekshirish.
# S.isalnum() - Satr harf yoki raqamlardan iboratligini tekshiradi.
# S.islower() - Satr quyi registrdagi belgilardan iboratligini tekshiradi.
# S.isspace()-Satrda ko`rinmaydidan belgilar borligini tekshirish (probel, sahifani o`tkazish
# belgisi(‘\p’), yangi satrga o`tish(‘\n’), koretkani qaytarish(‘\r’), gorizontal tabulyatsiya(‘\t’) va
# vertikal tabulyatsiya)
# S.istitle() - Satrda so`zlar bosh harf bilan boshlanishini tekshirish.
# S.starswith(str)- S satr str shablonidan boshlanishini tekshirish.
# S.endswith(str)- S satr str shabloni bilan tugashini tekshirish.
# S.join(ro`yxat)- S ajratuvchiga ega ro`yxatdan qatorni yig`ish.
# from curses.ascii import isdigit
# List – tartiblangan va o’zgaruvchan ro’yxat. Elementlarini dublikatlash mumkin.
#  Tuple – tartiblangan va o’zgarmas ro’yxat. Elementlarini dublikatlash mumkin.
# Set – Tartiblanmagan va indekslanmagan to’plam. Elementlari dublikatlanmaydi.
#  Dictionary – tartiblanmagan,o’zgaruvchan va indekslangan to’plam. Elementlari
# dublikatlanmaydi.

# List.append(x) Ro`yxat oxiridan element qo`shish
# List.extend(L) Oxiriga hamma elementlarni qo`shib list ro`yxatini
# kengaytiradi.
# List.insert(i,x) i-elementga x qiymatini kiritadi
# List.remove(x) Ro`yxatdan x qiymatga ega elementni o`chiradi
# List.pop([i]) Ro`yxatning i-elementini o`chiradi va qaytaradi. Agarda indeks
# ko`rsatilmagan bo`lsa oxirgi element o`chiriladi
# List.index(x,[start],[end]) X qiymatga teng start dan end gacha birinchi elementni
# qaytaradi
# List.count(x) X qiymatga teng elementlar sonini qaytaradi
# List.sort([key=funksiya]) Funksiya asosida ro`yxatni saralaydi
# List.reverse() Ro`yxatni ochadi
# List.copy() Ro`txatning nusxalaydi
# List.clear() Ro`yxatni tozalaydi

# a=3
# b=2
# c=1
# print((a+b+c)//3)
# from random import random

# def string_to_integer(s:str)->int:
#     result = ''
#     for i in s:
#         if isdigit(i):
#             result = result + i
#     return  int(result)
#
# print(string_to_integer('1133dvsj'))

# x = {"a","b","c"}
# y = (1,2,3)
# z = x.union(y)
# print(z)

# string1 = "98765"
# string2 = "Ninja" # True
# print(string1.isdigit()) #False
# print(string2.isdigit())





