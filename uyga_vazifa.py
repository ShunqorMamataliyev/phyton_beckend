####   Matematik Operatorlar (Arithmetic Operators)
#from random import random
#from pickle import PROTO
#from multiprocessing.spawn import import_main_path

# a = int(10) #int()
# b = int(3) #float()
# a=int(input ("a sonni kiriting  "))
# b=int(input("b sonni kiriting  "))
# print(a + b)  # Qo‘shish: 13
# print(a - b)  # Ayirish: 7
# print(a * b)  # Ko‘paytirish: 30
# print(a / b)  # Bo‘lish: 3.3333
# print(a % b)  # Qoldiq olish: 1
# print(a ** b) # Darajaga ko‘tarish: 1000 (10^3)
# print(a // b) # Butun bo‘lish: 3


####  Taqqoslash Operatorlari (Comparison Operators)

# x = 5
# y = 10
#
# print(x == y)  # False
# print(x != y)  # True
# print(x > y)   # False
# print(x < y)   # True
# print(x >= 5)  # True
# print(y <= 10) # True

####. Mantiqiy Operatorlar (Logical Operators)

# a = True #1
# b = False #0
# c= True
# d= True
#
# print(a and b or c and d)  # False   1*0=0
# print(a or b)   # True  1+0=1
# print(not a)    # False



########    Qo‘shilish Operatorlari (Assignment Operators)


# x = int(5)
# x += 3  # x = x + 3
# print(x)  # 8
#
# x *= 2  # x = x * 2
# print(x)  # 16
#
# x -= 5  # x = x - 5
# print(x)  # 11



######   Bitwise Operatorlar
# Bu operatorlar ikkilik sonlar bilan ishlaydi:
# & (AND)
# | (OR)
# ^ (XOR)
# ~ (NOT)
# << (chapga siljitish)
# >> (o‘ngga siljitish)

# a = 5   # 0101
# b = 3   # 0011
#
# print(a & b)  # 1 (0001)
# print(a | b)  # 7 (0111)
# print(a ^ b)  # 6 (0110)
# print(~a)     # -6 (1010)
# print(a << 1) # 10 (1010)
# print(a >> 1) # 2 (0010)



#####    Identifikatsiya va A'zo Operatorlari
# Identifikatsiya operatorlari:
# is (xuddi o‘sha obyektmi?)
# is not (xuddi o‘sha obyekt emasmi?)
# Misol:

# ism="G'ofurov Abdurouf"
# print(ism)

# x = [1, 2, 3]
# y = x
# z = [1, 2, 3]
#
# print(x is y)      # True (bir obyekt)
# print(x is z)      # False (faqat qiymat teng)
# print(x is not z)  # True

# a = [1, 21222, 13, 4]
# print(13 in a)
# print(13 not in a)
# print(1 in a)
# print(4 not in a)


# ###7. Matematik Kutubxona

# import math
#
# print(math.sqrt(16))  # 4.0 (ildiz)
# print(math.pi)        # 3.14159
# print(math.sin(math.radians(90))) # 1.0 (sinus)
# print(math.factorial(5))          # 120


       # #uyga vazifa
# print(5**4)  #625  # 5 ning 4-darajasini toping
#
# print(22%4)  #2  # 22 ni 4 ga bo'lganda qancha qoldiq qoladi?
#
# #Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping
# import math
# a=125
# print(4*a) # peremetr 4a
# print(a**2) #yuzi a **2
# print(math.pow(a,2)) # yuzi pow orqali
#
# #Diametri 12 ga teng bo'lgan doiraning yuzini toping  (π=3.14)
# # S=πr**2  r=d/2
# d=12 #diametr
# r=d/2 # radius diametrni yarmi
# π=3.14 # p qiymat
# S=π*r**2 # doira yuzini topish formulasi
# print(S)
# #Katetlari 3 va 4 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping (Pifagor teoremasidan foydalaning)
# # pifagor teoremasi a2+b2=c2
# a=3
# b=4
# c=a**2+b**2 # pifagor fo'rmulasi
# print(math.sqrt(c)) #c ildizdaan chiqaramz
#
# # xabar deb nomlangan o'zgaruvchiga biror matn yuklang va
# # konsolga chiqaring, keyin esa o'zgaruvchiga yangi qiymat berib
# # uni ham konsolga chiqaring.
# habar="Mamataliyev Shunqor Sherali o'g'li"
# print(habar)
# habar='27636'
# print(habar)
#
#  # class den nomlangan o'zgaruvchi yarating, unga biror qiymat bering
# # va konsolga chiqaring (siz kutgan natija chiqdimi?)
# #class='t73te'
# #print(class)  # bu hatolik beradi o'zgaruvchilar paythondagi kalit so'zlar blan nomlanmaydi
#
# #Dastur sizdan ism familiya, yoshinggizni va is_student yoki
# # student emasligizzi ,qayrda yashashligzni so'rasin,va oxirida bitta
# # print orqali:
# #"Alisher Axmadov yoshi 23da Toshkent shahrida yashaydi" deb chiqarsin
# a=input("Familya ismingiz: ")
# b=input("yoshingiz: ")
# c=input("talabamisz: ")
# d=input("yashash manzilingiz: ")
# print(a, ' ',b,' ',c,' ',d)
# import math
# print("a*x**2+b*x+c=0")
# a=float(input("a koeffitsentni kiriting: "))
# print(a)
# b=int(input("b koeffitsentni kiriting: "))
# print(b)
# c=int(input("c  ozod hatni kiriting: "))
# print(c)
# D=b**2-4*a*c
# if D>0:
#     x1=(-b+math.sqrt(D))/(2*a)
#     x2=(-b-math.sqrt(D))/(2*a)
#     print("x1: ",x1 ,' ',"x2: ",x2)
# elif D==0:
#     x=int(-b/(2*a))
#     print("yagona ildizi bor: " ,x)
# else:
#     print("ildizga ega emas")
# a=float(input(" a ni kiriting: "))
# b=float(input(" b ni kiriting: "))
# c=float(input(" c ni kiriting: "))
# if a>b>c:
#      print(a,b,c)
# elif a<b<c:
#     print(c,b,a)
# else:
#     print("teng")
# a=float(input("a Sonni kiriting:"))
# b=float(input("b Sonni kiriting:"))
# c=float(input("c Sonni kiriting:"))
# x=float(input("x Sonni kiriting:"))
# y=float(input("y Sonni kiriting:"))
#
# if a<=x and b<=y or b<=x and a<=y:
#     print("Tirqishga sig'adi ")
# elif b<=x and c<=y or c<=x and b<=y:
#     print("Tirqishga sig'adi ")
# elif a<=x  and c<=y or c<=x and a<=y:
#     print("Tirqishga sig'adi ")
# else:
#     print("Tirqishga sig'maydi ")

# x=float(input(" x ni kiriting:"))
# y=float(input(" y ni kiriting:"))
# if x>y:
#     print(x-y)
# else:
#     print(x-y+1)

# x=float(input(" 1 son ni kiriting: "))
# y=float(input(" 2 son ni kiriting: "))
# if x>y:
#      print(x)
# else:
#      print(x," va ",y)

# a=float(input("a Sonni kiriting:"))
# b=float(input("b Sonni kiriting:"))
# c=float(input("c Sonni kiriting:"))
# if 1<a<3:
#     print("a (1,3) oraliqqa tegishli")
# elif 1<b<3:
#     print("b  (1,3) oraliqa tegishli")
# elif 1<c<3:
#     print("c (1,3) oraliqqa tegishli")
# else:
#     print("bunday son mavjud emas")

# a=int(input("a Sonni kiriting:"))
# if a>=0 and a%2==0:
#     print(" kvadrati: ",a**2)
# else:
#     print(" son manfiy yoki juft emas")

# a=int(input("a Sonni kiriting:"))
# if a>=0 and a%2==1:
#  print(" kubi: ",a**3)
# else:
#     print(" son manfiy yoki toq emas")

# a=int(input("a Sonni kiriting:"))
# if a<0 and a%2==0:
#   print(abs(a))
# else:
#     print(" son musbat yoki juft emas")

# a=float(input("a Sonni kiriting:"))
# if a<0 and a%2==1:
#   print(math.sqrt(abs(a))) #manfiy sondan ildiz chiqmaydi
# else:
#     print(" son musbat yoki toq emas")

# a=int(input("sonni kiriting: "))
# if a==0:
#     print("son nolga teng: ")
# else:
#     print("son nolga teng emas: ")

# a=int(input(" extimoliy yil kiriting: "))
# if a>0 and a%4==0 or a%100==0 and a%400==0:
#     print("Kabisa yili")
# else:
#     print("Kabisa yili emas")

# a=int(input("a Sonni kiriting:"))
# b=int(input("b Sonni kiriting:"))
# c=str(input("Amalni kiriting"))
# if c=='+':
#     print("yig'indi: ", a+b)
# elif c=='*':
#     print("Ko'paytma: ",a*b)
# elif c=='/' and a!=0:
#     print("Bo'linma: ",a/b)
# elif c=='-':
#     print("Ayirma: ")
# else:
#     print("Siz nayto'g'ri amal kiritdingiz")

# a=float(input("a tomonni  kiriting: "))
# b=float(input("b tomonni kiriting:"))
# c=float(input("c tomonni kiriting:"))
# if a<(b+c) and b<(a+c) and c<(a+b):
#      print("Uchburchak yasash mumkin")
# elif a==b==c:
#     print(" teng tomonli uchburchak")
# elif a==b or b==c or c==a:
#     print("teng yonli uchburchak")
# else:
#     print("Uchburchak yasab bo'lmaydi")

#
# son1 = float(input("1-sonni kiriting: "))
# son2 = float(input("2-sonni kiriting: "))
# son3 = float(input("3-sonni kiriting: "))
# son4 = float(input("4-sonni kiriting: "))
# son5 = float(input("5-sonni kiriting: "))
# eng_katta = son1
#
# if son2 > eng_katta:
#     eng_katta = son2
# if son3 > eng_katta:
#     eng_katta = son3
# if son4 > eng_katta:
#     eng_katta = son4
# if son5 > eng_katta:
#     eng_katta = son5

# print(f"Eng katta son: {eng_katta}")


# #1-misol
# a=int(input("ixtiyoriy raqam :"))
# if 0<a<11:
#     print("birinchi dekada")
# elif 10<a<21:
#     print("ikkinchi dekada")
# elif 20<a<31:
#     print("uchinchi dekada")
# else:
#     print("xato;kun 30 dan katta bo'lishi mumkin emas")

#2-misol
# yosh=int(input("yoshingizni kiriting: "))
# balans = int(input("Kerakli balansni kiriting: "))
# if yosh<18:
#     print("kredit uchun yoshingiz to'g'ri kelmaydi")
# elif 18<=yosh<=25:
#     if balans>=10000000:
#         kredit_miqdori = balans * 1.3
#         print(" kredit miqdori 30% : ",balans*0.3," summ")
#         print(" To'lanadigan kredit summasi : ", kredit_miqdori, " summ")
#         if kredit_miqdori>=20000000:
#            print(kredit_miqdori," Sizdan maxsus tasdiq talab qilinadi")
#     else:
#         print("kredit berilmaydi")
# elif yosh>=26 and balans<5000000:
#     print("kredit berilmaydi")
# elif balans>=5000000 and yosh>=26:
#         kredit_miqdori = balans * 1.5
#         print(" kredit miqdori 30% : ", balans * 0.5, " summ")
#         print(" To'lanadigan kredit summasi : ", kredit_miqdori, " summ")
#         if kredit_miqdori>=20000000:
#            print(kredit_miqdori," Sizdan maxsus tasdiq talab qilinadi")
# else:
#     print("XATO: Iltimos malumotlarni qayta to'ldiring")

#3-misol
# yil=int(input("Hozirgi yilni kiriting: "))
# yili=int(input("Avtomobilingiz yilini kiriting: "))
# tajriba=float(input("Haydovchilik tajribangizni kiriting: YIL: "))
# narx=int(input("Avtomabilingiz qiymatini kiriting: "))
# if yil-yili<0 or tajriba<=0 or narx<0:
#     print("Iltimos malumotlarni qayta kiriting")
# elif yil-yili<5 and tajriba<1:
#     sugurta_narxi=narx*0.1
#     if sugurta_narxi>10000000:
#         print("Sug'urta narxi:",sugurta_narxi,"MAXSUS CHEGIRMA: ",sugurta_narxi*0.05)
#     elif sugurta_narxi<10000000:
#         print("Sug'urta narxi avtomobil narxining 10% ga teng: ",sugurta_narxi)
# elif 1<tajriba<3 and yil-yili<5:
#     sugurta_narxi = narx * 0.07
#     if sugurta_narxi>10000000:
#         print("Sug'urta narxi:",sugurta_narxi,"MAXSUS CHEGIRMA: ",sugurta_narxi*0.05)
#     elif sugurta_narxi<10000000:
#         print("Sug'urta narxi avtomobil narxin ing 7% ga teng: ",sugurta_narxi)
# elif  tajriba>3 and yil-yili<5:
#     sugurta_narxi = narx * 0.05
#     if sugurta_narxi>10000000:
#         print("Sug'urta narxi:",sugurta_narxi,"MAXSUS CHEGIRMA: ",sugurta_narxi*0.05)
#     elif sugurta_narxi<10000000:
#         print("Sug'urta narxi avtomobil narxin ing 5% ga teng: ",sugurta_narxi)
# elif yil-yili>5 and tajriba<3:
#     sugurta_narxi = narx * 0.08
#     if sugurta_narxi>10000000:
#         print("Sug'urta narxi:",sugurta_narxi,"MAXSUS CHEGIRMA: ",sugurta_narxi*0.05)
#     elif sugurta_narxi<10000000:
#         print("Sug'urta narxi avtomobil narxin ing 8% ga teng: ",sugurta_narxi)
# elif yil-yili>5 and tajriba>3:
#     sugurta_narxi = narx * 0.06
#     if sugurta_narxi > 10000000:
#         print("Sug'urta narxi:", sugurta_narxi, "MAXSUS CHEGIRMA: ", sugurta_narxi * 0.05)
#     elif sugurta_narxi < 10000000:
#         print("Sug'urta narxi avtomobil narxin ing 6% ga teng: ", sugurta_narxi)

##mustaqil
# t=60*60*24*365
# ml=1
# l=1000*ml
# x=int(input("yilni kiriting"))
# if 1<=x<=50:
#     y=t*x/l
#     print(y)

# x=float(input("x ni kiriting "))
# y=float(input("y ni kiriting "))
# if 1<=x and y<=10:   # and vas or
#     #c1=((x+y)/(y**2+abs(y**2+2/x+(x**3/5))))+math.e**(y+2)
#     a =
#     print(c1)

#import math

# x = float(input("x ni kiriting: "))
# y = float(input("y ni kiriting: "))
#
# if 1 <= x <= 10 and 1 <= y <= 10:  # Shartni to'g'ri yozish
#     surat = 2 * math.tan(x + math.pi / 6)
#     mahraj = (1 / 3) + math.cos(y + x**2)**2
#     yigindi = math.log2(x**2 + 2)
#     f1 = surat / mahraj + yigindi
#     print(f"f1 = {f1}")
# else:
#     print("x va y 1 va 10 oralig'ida bo'lishi kerak.")

# x = float(input("x ni kiriting: "))
# y = float(input("y ni kiriting: "))
# surat=(1/(x+(2/x**2)+(3/x**3))+math.e**(x**2+3*x))
# mahraj=math.atan(x+y)+math.pow(abs(5+x),2)
# ayirma=math.cos(y**2+(x**2/2))**2
# f2=surat/mahraj-ayirma
# print(f2)

# a=float(input("a ni kiriting: "))
# b= float(input("b ni kiriting: "))
# ildiz1=(math.sqrt(a))**(1/5)
# ildiz2=(math.sqrt(b*((a+b)/(2*b+a*b))))**(1/4)
# kopaytma=pow(a,2)+pow(b,2)+2
# T=ildiz1+ildiz2*kopaytma
# print(T)

### sugurta
# yosh=int(input("avtomabil yoshni kiriting, "))
# staj=int(input("tajribangiz, "))
# narx=int(input("avtomabil narxi, "))
# if 0<yosh<=5 and 0<staj<=1:
#     skidka=narx*(1/10)
#     if skidka>=10000000:
#         print("maxsus chegirmada",skidka-skidka*(5/100))
#     else:
#         print("sugurta narxi",narx*(1/10))
# elif 0<yosh<=5 and staj>1 and staj<=3:
#     skidka=narx*(7/100)
#     if skidka>=10000000:
#         print("maxsus chegirmada",skidka-skidka*(5/100))
#     else:
#         print("sugurta narxi",narx*(7/100))
# elif 0<yosh<=5 and staj>3:
#     skidka=narx*(5/100)
#     if skidka>=10000000:
#         print("maxsus chegirmada",skidka-skidka*(5/100))
#     else:
#         print("sugurta narxi",narx*(5/100))
# elif yosh>5 and 0<staj<3:
#     skidka=narx*(8/100)
#     if skidka>=10000000:
#         print("maxsus chegirmada",skidka-skidka*(5/100))
#     else:
#         print("sugurta narxi",narx*(8/100))
# elif yosh>5 and staj>3:
#     skidka=narx*(6/100)
#     if skidka>=10000000:
#         print("maxsus chegirmada",skidka-skidka*(5/100))
#     else:
#         print("sugurta narxi",narx*(6/100))
# else:
#     print("xatolik")

# ##list uyga vazifa
# tavsiyalar = ["Bolalar bog'chasiga boring", "Maktabga boring", "Oliy o'quv yurtiga boring", "Ish qidirish vaqti keldi"]
# yosh=int(input("yoshingizni kiriting: "))
# if 0<yosh<=6:
#     print(tavsiyalar[0])
# elif 7<= yosh <= 17:
#         print(tavsiyalar[1])
# elif 18<=yosh<=22:
#     print(tavsiyalar[2])
# elif yosh >=23:
#         print(tavsiyalar[3])
# else:
#     print("Noto'g'ri yosh kiritildi!")

#orta_osiyo=["O'zbekiston","Tojikiston","Qirg'iziston","Qozog'iston","Afg'oniston","Turkmaniston"]
#print(orta_osiyo) #1

#print(len(orta_osiyo))   #2

#print(orta_osiyo)

#print(sorted(orta_osiyo))    #3

# teskari_list=sorted(orta_osiyo,reverse=True)
# print(teskari_list)   #4

#print(orta_osiyo) #5

# orta_osiyo.reverse()
# print(orta_osiyo)  #6

# orta_osiyo.sort()
# print(orta_osiyo)  #7

# orta_osiyo.sort(reverse=True)
# print(orta_osiyo) #8

# for i in range(120,1201):   #9
#     if i%2==0:
#         a.append(i)   # for orqali
# print(a)

#numbers=list(range(120,1201,2)) #9 2 usul
# print(numbers)

# numbers=list(range(120,1201,2)) #9 2 usul #10
# print(sum(numbers))

# numbers=list(range(120,1201,2))
# print(max(numbers)-min(numbers))

# numbers=list(range(120,1201,2))
# print(len(numbers))      # 11

# numbers=list(range(120,1201,2))
# print(numbers[0:20])

# numbers=list(range(120,1201,2))
# print(numbers[-20:])

# numbers=list(range(120,1201,2))
# son=int(len(numbers)/2)
# print(numbers[son-10:son+10])

# taomlar=["osh","manti","sho'rva","xonim","lag'mon"]
# nonushta=taomlar.copy()
# print(nonushta)
# nonushta.remove("manti")
# nonushta.remove("osh")
# nonushta.extend(["chuchvara","tuxum"])
# print(nonushta)
# print("natija =",taomlar+nonushta)

# taom=taomlar[::] #copy
# print(taom)

# a=[]
# a.append(1)
# a.append(4)
# a.insert(2,"shunqor")
# print(a)

#a=[1,2,3,4]
#a.clear()
#b=a.copy()
#b.count(2)
#print(a.count(1))

# a=[1,2,3,4]
# print(a.index(1))

# matrix=[[1,2,3,4],[4,3,'salom']]
# print(matrix[0])
# print(matrix[1][2])

# Ro'yxatni o'rnatamiz
# royxat = [1, 2, 3, 4, 5]
# toq_sonlar_yigindisi = sum(son for son in royxat if son % 2 != 0)
# print("Ro'yxatdagi toq sonlar yig'indisi:", toq_sonlar_yigindisi)

# a=[1,2,3,4,5]
# son=1
# for i in a:
#     son*=i
# print(son)

# a=[]
# if len(a)>0:
#     print('BOSH EMAS')
# else:
#     print("bo'sh")


# # O'zgaruvchi
# A = "Shun9qo7rb6e4k"
# yigindi = sum(int(raqam) for raqam in A if raqam.isdigit())
# print("Raqamlar yig'indisi:", yigindi)

# thisset = {"apple", "banana", "cherry", False, True, 121212}
# print(thisset)
# print(len(thisset))
# print(type(thisset))
#
#
# thisset = {"apple", "banana", "cherry", False, True, 121212}
# numbers={12,12,2,23,23,3,23,23}
# thisset.update(numbers)
# print(thisset)


# thisset = {"apple", "banana", "cherry", False, True, 121212}
# thisset.remove('banana')
# thisset.discard(123123)
# print(thisset)

# thisset = {"apple", "banana", "cherry", True, 121212}
# x=thisset.pop()
# print(x)
# print(thisset)

# thisset = {"apple", "banana", "cherry", False, True, 121212}
# thisset.clear()
# print(thisset)


# fullname='ddddd'
# thisset = {"apple", "banana", "cherry", False, True, 121212}
# del fullname
# print(fullname)

# first_one={1,2,3,4,5}
# second_one={3,4,5,6,7,8}
# print(first_one.intersection(second_one)) #3,4,5
# print(first_one.union(second_one)) #hammasi
# print(first_one.difference(second_one)) # 1,2

#############################
# Bo'sh dictionary
# my_dict = {}

# Kalit-qiymat juftliklari bilan
# my_dict = {"name": "Alex", "age": 25, "city": "Tashkent"}
# print(my_dict.get('name'))
# print(my_dict['age'])
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())


# my_dict = {"name": "Alex", "age": 25, "city": "Tashkent"}
# other_dict={"color":"qizil","kurs":"backend",'ichimlik':"flash"}
# my_dict.update(other_dict)
# print(my_dict)

# my_dict = {"name": "Alex", "age": 25, "city": "Tashkent"}
# new_dict=my_dict.copy()
# print(new_dict)

# my_dict = {"name": "Alex", "age": 25, "city": "Tashkent"}
# my_dict['first_name']="Alisher" #yange qoshish
# my_dict['age']=26 # o'zgaritirsh
# print(my_dict)

# kalitla=['age','name','city',1212]
# new_dict=dict.fromkeys(kalitla,'lyuboy narsa')
# print(new_dict)


# my_dict = {"name": "Alex", "age": 25, "city": "Tashkent"}
# print(my_dict.get("xxxxxxxx"))
# print(my_dict.get("xxxxxxxx",'bunaqa element yo'))

# my_dict = {"name": "Alex", "age": 25, "city": "Tashkent"}
# deleted_item=my_dict.pop("age")
# deleted_item=my_dict.popitem()
# print(deleted_item)
# print(my_dict)

# my_dict = {"name": "Alex", "age": 25, "city": "Tashkent"}
# my_dict['phone_number']=input("telefon raqammi kiriting  ")
# my_dict[input("kalit kriiting ")]=input("yangi qiymat kiriting   ")
# print(my_dict)

#########################


# import random

# print(random.random())          # 0 va 1 orasida tasodifiy son
# print(random.randint(1, 10))    # 1 dan 10 gacha tasodifiy butun son
# fruits = ['apple', 'banana', 'cherry','2323']
# print(random.choice(fruits))    # Tasodifiy meva
# random.shuffle(fruits)          # Mevalarni aralashtirish
# print(fruits)

##uyga vazifa set dict
#1-misol
# num_set={1,2,3,4,5}
# if 6 in num_set:
#     num_set.remove(6)
#     print(num_set)
# else:
#     num_set.add(6)
#     print(num_set)

#2-misol
# n1_set={2,4,6,8}
# n2_set={7,9,11,13}
# print(n1_set.intersection(n2_set))
# print(n1_set.union(n2_set))

# 3-misol
# jumla=str(input(print('Malumot kiriting: ')))
# unical_set=jumla.split()
# unical_sozlar=set(unical_set)
# print(unical_sozlar)

#4-misol
# n1_set=set()
# n2_set=set()
# for i in range(1,11):
#     n1_set.add(i)
# for i in range(5, 16):
#     n2_set.add(i)
# print("set 1=",n1_set)
# print("set 2=",n2_set)
# print("1 set farqi=",n1_set.difference(n2_set))
# print("2 set farqi=",n2_set.difference(n1_set))

#5-misol
#ishtirokchilar={'Shunqor','Barkamol','Javohir','Umidjon','Lazizbek','Abbosbek'}
#print("ishtirokchilar=",ishtirokchilar)
#chetlashtirilgan={'Javohir','Shunqor'}
#print(ishtirokchilar.difference(chetlashtirilgan))
#print("chetlatilgan=",chetlashtirilgan)
#print("qolgan ishtirokchilar=",ishtirokchilar)

#dict misol
#1-misol
# talaba = {}
# a = str(input("Ismingizni kiriting: "))
# b = str(input("Yoshingizni kiriting: "))
# c = str(input("Fakultetingizni kiriting: "))
# talaba['ism'] = a
# talaba['yosh'] = b
# talaba['fakultet'] = c
# print("Yaratilgan dictionary:", talaba)

#3-misol
# mahsulot={'olma':25,'anor':30,'uzum':40}
# a=str(input('Mahsulot nomini kiriting: '))
# if a in mahsulot:
#     print(a ,"narxi: ",mahsulot.get(a))
# else:
#     print("Mahsulot topilmadi")
# narxlar = sorted(mahsulot.values())
# print("Eng qimmat narx: ",narxlar[-1])

#4-misol
# import random
# tasodifiy_son = random.randint(1, 100)
# while True:
#     foydalanuvchi_soni = int(input("1 dan 100 gacha bo'lgan biror sonni kiriting: "))
#
#     if foydalanuvchi_soni == tasodifiy_son:
#         print("Teng! Siz to'g'ri topdingiz!")
#         break
#     elif foydalanuvchi_soni < tasodifiy_son:
#         print("Yuqoriroq son kiriting.")
#     else:
#         print("Pastroq son kiriting.")


# from idlelib.configdialog import changes
#
# yangi_list={"aziz","javohir","shunqor","umid"}
# print(yangi_list)
# ism_list =input("Ism kiriting: ").split()
# yangi_list.update(ism_list)
# print(yangi_list)
# golib = random.choice(list(yangi_list))
# print(f"G‘olib: {golib}")


# talabalar_dict={"ism": "Alex","yosh":30,"fakultet":"fizika"}
# ism=input("Ism kiriting: ")
# yosh=int(input("Yosh kiriting: "))
# fakultet=input("Fakultet kiriting: ")
# talabalar_dict["new talaba"]={"ism": ism,"yosh": yosh,"fakultet": fakultet}
# print(talabalar_dict)
# import random
# tasodifiy_son=random.randint(1,1000)
# print(tasodifiy_son)

# import random
# a=random.randint(1,100)
# while True:
#     b = int(input("Ixtiyoriy son kiriting: "))
#     if a==b:
#         print("Teng:Siz to'g'ri topdingiz")
#         break
#     elif a<b:
#         print("Kichikroq son kiriting")
#     elif a>b:
#         print("Kattaroq son kiriting")
#     else:
#         print("Teng emas qayta urining")
##for vazifa
## rasm misol
#for  son in range(5,6):
# for kopaytmalar in range(0,11):
#      print(f"{5} x {kopaytmalar} ={5*kopaytmalar}")

# for kvadrat in range(1,11):
#     for jadval in range(1,11):
#         print(f"{kvadrat} x {jadval}={kvadrat*jadval}")

## 1-misol
# toq_son=[]
# juft_son=[]
# for son in range(1,101):
#     if son%2==1:
#         toq_son.append(son)
#     else:
#         juft_son.append(son)
# print("Toq=",toq_son)
# print("Juft=",juft_son)

##2-misol
# n=int(input("Ixtiyoriy son kiriting: "))
# yigindi=0
# for son in range(1,n):
#     yigindi+=son
# print(f"{n} gacha sonlar yig'indisi ={yigindi}")

##3-misol
# toq_yigindi=0
# juft_yigindi=0
# n=int(input("Ixtiyoriy son kiriting: "))
# for son in range(1,n):
#     if son%2==1:
#         toq_yigindi+=son
#     else:
#         juft_yigindi+=son
# print("Toq sonlar yig'indisi=",toq_yigindi)
# print("Juft sonlar yigindisi=",juft_yigindi)

##4-misol
# toq_sonlar=[1,3,5,7,9]
# juft_sonlar=[2,4,6,8,10]
# list_kopaytma=[]
# for son1 in toq_sonlar:
#     for son in juft_sonlar:
#         list_kopaytma.append(son1*son)
# print(len(list_kopaytma))
# print(list_kopaytma)

##5-misol
# son=str(input(" kamida 5  xonali son kifiting: "))
# yigindi=0
# if len(son)>=5:
#     for x in son:
#         yigindi+=int(x)
#     print(f" raqamlar yigindisi={yigindi}")
# else:
#     print("Kamida 5 xonali son kiriting")

## 6-misol
# x=str(input("Ixtiyoriy so'z kiriting: "))
# x=x.lower()
# if x==x[::-1]:
#     print(f"{x} so'zi palindrom")
# else:
#     print(f"{x} so'zi  palindrom emas")

##7-misol
# import math
# list1=[1,2,3]
# list2=[]
# for factorial in list1:
#     list2.append(math.factorial(factorial))
# print(list2)

# list1=[3,7,5]
# list2=[math.factorial(son) for son in list1]
# print(list2)

##8-misol
# for son in range(0,101):
#     if son%3==0 and son%4==0:
#         print(son)

# for son in range(0,100,12):
#     print(son)

##while misol
# kitob=('Yaxshi korgan kitobingizni kiriting: \n')
# kitob+="Dasturni to'xtatish uchun exit deb yozing: "
# ishora=True
# while ishora:
#     qiymat=input(kitob)
#     if qiymat=='stop':
#        ishora=False
#        print("Dastur to'xtadi")

##2
# while True:
#     age = input("Yoshingzizni kiriting:\nESLATMA:dasturni toxtatish uchun exit yoki quit deb yozing:")
#     if age.lower() in['exit','quit']:
#         print("Dastur tugadi")
#         break
#     if age.isdigit():
#         yosh=int(age)
#         if yosh<7:
#             print( 'Chipta narxi 2000 summ')
#         elif 7<=yosh<18:
#             print( 'Chipta narxi 3000 summ')
#         elif 18<=yosh<65:
#             print( 'Chipta narxi 10000 summ')
#         else:
#             print("Siz uchun chipta narxi Bepul")
##4
# myllist=[]
# while True:
#     mahsulot=input("mahsulot nomini kiriting: ")
#     if mahsulot=='exit':
#         break
#     myllist.append(mahsulot)
# print(myllist)


# def malumot(tel:int,ism,fam):
#     print(f"Sizning ismingiz: {ism.title()}\nFamilyangiz: {fam.title()}\nTel: {tel}")
# malumot('937179764','shunqor','mamataliyev')

###funktsiya vazifa

######1-misol
# def yosh_hisobla(ism,yosh, joriy_yil=2024):
#     print(f"Siz {joriy_yil-yosh}-yilda tugilgansiz\nIsmingiz {ism}")
# yosh_hisobla('Shunqor',20)

# def tugilgan_yil(yosh,yil=2024):
#     kerak = yil - yosh
#     return kerak
# yosh=int(input("Yoshingizni kiriting: "))
# print(f" Siz {tugilgan_yil(yosh)}-yilda tug'ilgansiz")

###2-misol
# import math
# def kv_kub(son):
#     print(f"Son kvadrati: {math.pow(son,2)}\nSon kubi: {math.pow(son,3)}")
# kv_kub(3)

# import math
# def kv(son):
#    kvadrat=int(math.pow(son,2))
#    return kvadrat
# def kub(son):
#    kubb=int(math.pow(son,3))
#    return kubb
# son=int(input("Ixtiyoriy son kiriting: "))
# print(f"{son} kvadrati: {kv(son)}")
# print(f"{son} kubi: {kub(son)}")

### 3 misol
# def tekshirish(son):
#     if son%2==0:
#         print(f"{son} juft")
#     else:
#         print(f"{son} toq")
# tekshirish(4)

# def tekshirish(son):
#     if son%2==0:
#        return  'juft'
#     else:
#         return  'toq'
# a=int(input("Ixtiyoriy son kiriting: "))
# print(tekshirish(a))

####4-misol
# def tekshir(a,b):
#     if a>b:
#         print(f"{a} soni katta")
#     if a<b:
#         print(f"{b} soni katta")
#     elif a==b:
#         print(f"{a} va {b} sonlar teng")
# tekshir(2,3)

# def tekshir(son1,son2):
#     if son1>son2:
#         return son1
#     if son1<son2:
#         return son2
#     elif son1==son2:
#         return 'Sonlar teng'
# son1=int(input("1 sonni kiriting: "))
# son2=int(input("2 sonni kiriting: "))
# print(tekshir(son1,son2))

###5-misol
# import math
# def daraja(x,y):
#     print(math.pow(x,y))
# daraja(2, 3)

# import math
# def daraja(x,y):
#     natija=math.pow(x,y)
#     return natija
# x=int(input("x ni kiriting: "))
# y=int(input("y ni kiriting: "))
# print(f"x ni y darajasi: {daraja(x,y)}")

###7-misol
# def tekshir_for(son):
#     for i in range(2,11):
#         if son%i==0:
#             print(f"{son} soni {i} bolinadi")
#         else:
#             print(f"{son} soni {i} bolinmaydi")
# print(f"Ixtiyoriy sonni  2 dan 10 gacha sonlarga qoldiqsiz bo'linishi ")
# tekshir_for(10)

# ###9-misol
# def malumot(*xarakteristka):
#     data={'ism':ismi,'familya':familyasi,'tugilgan_yili':tugilgan_yili,'tugilgan_joyi':tugilgan_joyi,'email_adres':email,'tel':tel_raqam}
#     return data
# malumotnoma=[]
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting")
#     ismi = input("Ismingizni kiriting: ")
#     familyasi = input("Familyangizni kiriting: ")
#     tugilgan_yili = input("Tugilgan yilingizni kiriting: ")
#     tugilgan_joyi = input("Tugilgan joyingizni kiriting: ")
#     email = input("Emailingizni kiriting: ")
#     tel_raqam = input("Tel raqamingizni kiriting : ")
#     malumotnoma.append(malumot(ismi, familyasi, tugilgan_yili, tugilgan_yili, email, tel_raqam))
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob == 'no':
#         break
# print(malumotnoma)


###11-misol
# def maxx(x,y,z):
#     if x>y and x>z:
#         return 'x'
#     elif y>x and y>z:
#         return 'y'
#     elif z>x and z>y:
#         return 'z'
# #x=int(input("1 sonni kiriting: "))
# #y=int(input("2 sonni kiriting: "))
# #z=int(input("3 sonni kiriting: "))
# print(maxx(2,4,2))

###12-misol


####data module
###9
# def malumotnoma(*args):
#     malumot= {
#         'ism': args[0],
#         'familya': args[1],
#         'tugilgan_joyi': args[2],
#         'Tugilgan yili': args[3],
#         'email': args[4],
#         'tel': args[5],
#     }
#     return malumot
#
# # Avtomobil ma'lumotlarini yaratish
# malumot1= malumotnoma('Shunqor', 'Mamataliyev', 'Ohangaron', 2018,'shunqormamataliyev737@gmail.com',937179764)
# print(malumot1)

##10
# def malumotnoma(*args):
#     malumot = {
#         'ism': args[0],
#         'familya': args[1],
#         'tugilgan_joyi': args[2],
#         'Tugilgan yili': args[3],
#         'email': args[4],
#         'tel': args[5],
#     }
#     return malumot
#
# while True:
#     print("\nYangi foydalanuvchi ma'lumotlarini kiriting:")
#     ism = input("Ism: ")
#     familya = input("Familya: ")
#     tugilgan_joyi = input("Tug'ilgan joyi: ")
#     tugilgan_yili = input("Tug'ilgan yili: ")
#     email = input("Email: ")
#     tel = input("Telefon raqami: ")
#
#     malumot = malumotnoma(ism, familya, tugilgan_joyi, tugilgan_yili, email, tel)
#     print("\nKiritilgan ma'lumotlar:")
#     print(malumot)
#     break

##11
# def maxxx(*sonlar):
#     a=max(sonlar)
#     return a
# print(maxxx(32,3,235))


# def kopaytma_son(*sonlar):
#     kopaytma = 1
#     a = 0
#     while True:
#         a += 1
#         son=input('Son kiriting: ')
#         if son.lower()=='exit' and a  > 0 :
#             return kopaytma
#         else:
#             return kopaytma *= son
# print(kopaytma_son())

# a=int(input('son kiriting: '))
# for i in (1,a):
#     print(i)

# a = """ 1
#  1 2
#  1 2 3
#  1 2 3 4
#  1 2 3 4 5"""
# b = ''' A
#  B B
#  D D D
#  E E E E
#  F F F F F'''
# print(a)
# print(b)










