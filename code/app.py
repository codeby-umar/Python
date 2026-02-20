import math
from colorama import Fore , Style , init
init()

# # 1 - vazifa
# ism = input("Sizning isningiz :")
# full_Hello = f"Hello {ism}"
# print(full_Hello)

# 2 - vazifa
# get_Year = int(input("Yilingizni kiriting :"))
# new_Year = 2026
# full_Body = new_Year - get_Year
# print(full_Body)

# 3 - vazifa
# sum1 = float(input("Son kiriting :"))
# sum2 = float(input("Son kiriting :"))
# jami = sum1 + sum2
# print(jami)

# 4 - vazifa
# new_City = input("Siz shaxar kiriting :")
# full_Text = f"Men {new_City} shaharni juda yaxshi ko'raman "
# print(full_Text)

# 5 - vazifa
# a = int(input("Son kiritning a :"))
# b = int(input("Son kiritng b :"))
# code_Minus = a - b 
# code_Max = a + b
# code_big = a * b
# code_bool = a / b
# full_head = f"Ayriganda : {code_Minus} Qo'shganda : {code_Max} Ko'paytirganda : {code_big} Bo'lganda : {code_bool} "
# print(full_head)

# 6 - vazifa
# new_boy = input("Siznig boyingiz :")
# new_weith = input("Sizning vazningiz :")
# full_code = f"Sizning boyiningiz : {new_boy + "cm"} Siznig vazningiz : {new_weith + "kg"}"
# print(full_code)

# 7 - vazifa
# put_Money = float(input("Siz do'llar kiritng $ :"))
# new_year_Money = 12.280
# full_code = put_Money * new_year_Money
# print(full_code , "So'm")    

# 8 - vazifa
# code1 = "so'm"
# code2 = "$"
# new_year_Money = 12.280
# code_Operator = input(f"Siz {code1}  /  {code2} qilasizmi :")
# new_Money = float(input(f"Siz nechi {code_Operator} qilmoqchisiz :"))
# if code_Operator == code1:
#     h = new_Money * new_year_Money
#     print(f"{h} So'm")
# elif code_Operator == code2:
#     k = new_Money / new_year_Money
#     print(f"{k} $")
# else:
#     print("Sizda nimadur xatolik qilmoqda")

# 9 - vazifa
# name = str(input("Ismingizni kiriting :"))
# firstName = str(input("Famiyaningizni kiriting :"))
# full_Name = f"Sizning isminingiz : {name}  Sizning familyangiz : {firstName}"
# print(full_Name)

# 10 - vazifa
# a = (600 + 300) * 4
# b = (1800 / 6) + 90
# result = int(a - b)
# print("Natija : " , result)

# 11 - vazifa
# kvadrat_Heidth = float(input("Kvadrat bo'yini kiriting cm :"))
# kvadrat_Weidth = float(input("Kvadrat eni kiriting cm :"))
# kvadrat_Yuzi = kvadrat_Heidth * kvadrat_Weidth
# full_kvadrat = f"Kvadratning yuzi : {kvadrat_Yuzi}"
# print(full_kvadrat , "yuzi yani s")










# 1 - homework
# name = input("Ismingizni kiritng :")
# firstName = input("Famiyanigni kiritning :")
# full_Name = f"Sizning isminingiz : {name.upper()} , Sizning familyaningiz : {firstName.lower()}"
# print(full_Name)

# 2 - homework
# name = str(input("Sizning ismingiz :"))
# first_Name = str(input("Sizning familyaningiz :"))
# username = input("Username kiriting :")
# full_body = f"Sizning isminingiz : {name.capitalize()} + \
# Sizning familyangiz : {first_Name.capitalize()} + \
# Sizning Usernameiz : {username.replace("_" , ".")}"
# print(full_body)

# 3 - homework
# new_Text = input("So'z kiriting :")
# full  = sum(1 for c in new_Text if c.isalpha())
# print("Sizning yosgan so'zingiz harfi :" , full)

# 4 - homework 
# new_Number = input("Siz qanchadir son kiritining : ")
# full_code = sum(1 for code in new_Number if code.isdigit())
# print("Sizning yozgan soningiz nechtaligi : " , full_code)

# 5 - homework
# ism = input("Siz birota son kiriting :")
# for code in ism:
#     if code.isalpha():
#         print(code)
#     else :
#         print('Xatolik yuz berdi')

# 6 - homework
# New_words = input("Siz bironta narsa kiritng :")
# full_Code = New_words.startswith(New_words)
# print(full_Code)

# 7 - homework
# new_Code = input("Bironta soz yoki number kiriting :")
# code_Full = new_Code.endswith(new_Code)
# print(code_Full)





# 1 - funtion is easy

# sum = int(input("Son kiritning a : "))
# sum1 = int(input("Son kiriting b :"))

# def get_Milus(minus , pilus):
#     return minus + pilus
 
# code_full = get_Milus(sum , sum1)
# print(type(get_Milus))


# 3 - funtion
# a = float(input("Son kiriting a :"))
# b = float(input("Son kiriting b :"))
# code_Operator = input("Nima qilmoqchisiz :")

# def get_Canculator(min , max , big , bool):
#     if code_Operator == min:
#         return a - b
#     elif code_Operator == max:
#         return a + b
#     elif code_Operator == big:
#         return a * b
#     elif code_Operator == bool:
#         return a / b
#     else:
#         print("Siz nimadadur xatolik qildingiz")

# full_Codes = get_Canculator('-' , '+' , '*' , '/')
# print(f"Natija : {full_Codes}")


# 4 - homework

# new_Number = int(input("Son kiriting :")) 

# def isParam(num):
#     if num < 2:
#         return False
#     for i in range(2 , num):
#         if num % i == 0:
#             return False
#     return True

# code = isParam(new_Number)
# print(code)



# 5 - homework






# string - uyga vaziflar javoblari


# 1 - vazifa
# new_words = input("Bironta so'z kiriting :")
# new_Code = len(new_words)
# print(new_Code)  
 
# new_Code = str(input("Bironta so'z kiritng :"))
# def get_Counds(num):
#     return len(num)
# Code_funtion = get_Counds(new_Code)
# print("Harflar soni : " , Code_funtion ,"ta harf bor ekan")

# 2 - vazifa
# upper - Barcha hariflarni katta harfda qilib beradi
# name = str(input("Ismingizni kiriting :"))
# new_Code = name.upper()
# print("Katta harf : " , new_Code)

# 3 - vazifa
# lower - Barcha matndagi harflarni kichkina qilib beradi
# little_Code = input("Biron bir so'z kiriting :")
# code_Bug = little_Code.lower()
# print("Hamma harfni kichkina :" , code_Bug)

# 4 - vazifa
# name = str(input("Isminingizni kiriting :"))
# code_New = f"Hello {name.upper()}"
# print(code_New)

# 5 - vazifa
# new_Soz = "Muhammad Umar is very clear"
# full_Code = new_Soz[0]
# print(full_Code)  


# 6 - vazifa
# new_Soz = "Muhammad Umar is very clear"
# full_Code = new_Soz[-1]
# print(full_Code) 

# 7 - vazifa
# ism = input("Bironta soz kiritning :")
# app = len(ism)
# print("Mana shuncha harf bor :" , app)


# 8 - vazifa
# new_Text = str(input("Bironta matn kiritng :"))
# rev = new_Text[::-1]    
# print(rev)

# 2 - usuli
# new_Text = str(input("Bironta matn kiritng :"))
# teskari = "".join(reversed(new_Text))
# print(teskari)

# 9 -vazifa
# new_Text = str(input("So'z kiritning :"))
# siz_quiz = str(input("Siz qaysi harfni sanamoqchisiz : "))
# new_Code = new_Text.count(siz_quiz)
# print(f"Bu yerda {new_Code} marta ishlatilgan")

# 10 - vazifa
# new_userName = str(input("Siz username kriting :"))
# new_Full = new_userName.replace(" " , "_")
# new_line = new_Full.lower()
# print("Sizning usernameiningiz :" , new_line)

# 11 - vazifa
# new_tehno = "1212 Salom"
# new_Code = new_tehno.startswith(new_tehno)
# print(new_Code)

# Startswith - bu faqat matni bosh soz bilan boshlansa True yoki False qaytaradi
# print("Salom hwllo world 3121".startswith("Salom"))

# a = "Python is very clear boy"
# b = a.startswith("Python")
# print(b)

# endwith - matnda so'z bila tugaydiga bolsa true youki false
# new_words = "Siz juda aqili inson ekasiz hey 1212"
# code = new_words.endswith("212123")
# print(code)


# a = "Salom juda aclisdjsids dsdjsds"
# b = a.find("s")
# print(b)


# a = "Salom juda aclisdjsids dsdjsds"
# b = a.count("s")
# print(b)



# sum = float(input("Son kiriting :"))
# sum1 = float(input("Son kiriting :"))
# code_Full = sum + sum1
# print("Yig'indisi :" , code_Full)



# n = 3.14 
# radius = float(input("Siz radius kiriting :"))
# full_Code = n * (radius ** 2)
# print("Aylananing yuzi : " , full_Code)


# new_Words = input("Siz bironta narsa kiritng :")
# new_Word = input("Siz so'z kiriting :")
# full_Code = new_Words + new_Word
# print(full_Code)


# name = str(input("Sizning ismingiz :"))
# firstName = str(input("Sizning familyangiz :"))
# code, code1 = name  , firstName
# code_Full = f"Sizning ismingiz : {code} Sizing familyangiz : {code1}"
# print(code_Full)


# new_Age = input("Sizning youshingiz :")
# new_Code = int(new_Age)
# print("Sizning yoshingiz : " , new_Code)



# sum = float(input("Son kiriting :"))
# sum1 = float(input("Son kiriting :"))
# code_Full = sum + sum1
# print("Yig'indisi :" , code_Full)









# string methods

# ism = "Shukurullo"
# code = ism[3]
# print(code)


# a , b , c = "Salom" , "Hi" , "Hello"
# print(a)



# name = str("olma")
# print(name)


# upper - Hamma harflarni katta qilib beradi 
# ism = str(input("Ismingiz"))
# code = ism.upper()
# print(code)


# lower - hamma harfni kichkina qilib beradi
# python = "Python Is Very Easy"
# code = python.lower()
# print(code)

# title - matnda hamma bosh harfini kattada qilib beradi
# code = "olma , shaftoli , nok"
# Full = code.title()
# print(Full)


# capitalize - boshidagi bitta sozni katta qilib beradi
# login = "shiklat@gmail.com"
# full_Code = login.capitalize()
# print(full_Code)


# replace - matnda keraksiz sozni olib orniga yangi matn qaytaradi
# login = str(input("Login kiriting :"))
# full_Code = login.replace("m" , "_")
# print(full_Code)


# len - matnni uzunligini qaytaradi
# nom = "olma"
# code = len(nom)
# print(code)


# strip - boshi va ooxiridan joylarni olib beradi

# ism = "   Anvar       "
# print(ism)
# code = ism.strip()
# print(code)




"""1 - vazifa"""
# street = "Guliston"
# mahalla = "Manak"
# city = "Andijon"
# tuman = "Xo'jabod"
# full_Code = f"{city} viloyati {tuman} tumani {mahalla} qishlog'i {street} ko'chasi"
# print(full_Code)
"""2 - vazifa"""
"""Siz uchun mahalla va qishloginingni royxatga olamisz"""
# kocha = str(input("Sizning kochangiz :"))
# qishlog = str(input("Sizning qishlog'ingiz : "))
# tuman = str(input("Sizning tumaningiz :"))
# shahar = str(input("Sizning shaxaringiz :"))
# data = f"Sizning ko'chaningiz : {kocha} Sizning qishloginingiz : {qishlog} \
# Sizning tumaningiz : {tuman} Sizning shahariningiz : {shahar}"
# print(data)
"""3 - vazifa"""

# value_Type = input("Biron narsa kiriting :")

# if type(value_Type) == int:
#     print("Bu yozgan data type : number yani integer")
# elif type(value_Type) == str:
#     print("Bu yozgan data type : string")
# elif type(value_Type) == float:
#     print("Bu yozgan data type : Float")
# else:
#     print("____Error____")

"""4 - vazifa"""
# ism = str(input("Sizing ismingiz : "))
# login = str(input("Sizning loginingiz :"))
# password = input("Sizning passwordningiz :")

# if len(password) > 8:
#     print(f"--------------------Hello {ism.capitalize()}-------------------------")
#     print(f"Sizning passwordiningiz {len(password)} tadan kichik maximum 8 bolish kerak")
#     print(f"Sizning loginingiz : {login.replace(" " , "@gmail.com").lower() }")
#     print("---------------------------------------------")
# elif len(password) == 8:
#     print(f"--------------------Hello {ism.capitalize()}-------------------------")
#     print(f"Sizning paroliningiz togri  {len(password)}! Saytga xush kelibsiz")
#     print(f"Sizning loginingiz : {login.replace(" " , "@gmail.com").lower() }")
#     print("---------------------------------------------")
# else:
#     print("---------------------Error------------------------")
#     print(f'Sizni parolingiz 8 tadan kam {len(password)} ta ')
#     print(f"Sizning loginingiz : {login.replace(" " , "@gmail.com").lower() }")
#     print("---------------------------------------------")

"""5 - vazifa"""

# name = str(input("Ismingizni kkiriting : "))
# replaces = name.replace(" " , "").lower()
# value = len(replaces)
# full_Code = f"Sizning ismingiz : {name} , {replaces} ismingizda  {value} harfdan iborat"
# print(full_Code)


# easy homework
"""1 - vazifa"""
"""1. Foydalanuvchidan ism so‘ra va ekranga:"""
# name = str(input("Ismingiz kiriting :"))
# print("Salom" , name.capitalize())
"""2 - vazifa"""
"""2. Ikkita son kiritib, ularning yig‘indisini chiqar."""
# sum = input("Son kiriting :")
# sum2 = input("Son kiriitng :")
# Value_Key = float(sum) + float(sum2)
# print("Javob :" , Value_Key)
"""3 - vazifa"""
"""3. Son kiritib, uning juft yoki toqligini aniqlovchi dastur yoz."""
# number = int(input("Son kirititng :"))

# if number % 2 == 0:
#     print(f"Bu son {number} juft son")
# else:
#     print(f"Bu son {number} juft emas")
"""4 - vazifa"""
"""4. Foydalanuvchi yoshini kiritsin. Agar 18 dan katta bo‘lsa "Ruxsat berildi", aks holda "Ruxsat yo‘q" chiqarsin."""

# new_Age = int(input("Son kiriting :"))

# if new_Age > 18:
#     print("------------------------------------")
#     print("Tabriklaymiz siz ishga olindingiz !")
#     print("------------------------------------")
# elif new_Age == 18:
#     print("------------------------------------")
#     print("Tabriklaymiz siz ishga olindingiz !")
#     print("------------------------------------")
# else:
#     print("------------------------------------")
#     print(f"Sizni ishga olmaymisz chunki yoshingiz {new_Age}")
#     print("------------------------------------")

"""5 - uyga vazifa"""
"""5. 1 dan 10 gacha bo‘lgan sonlarni for yordamida chiqar."""
# for i in range(1 ,10):
#     print(i)

"""6 - vazifa"""
# sum = int(input("Son kiriting :"))
# kub = sum ** 3
# kvadrat = sum ** 2
# print(f"Bu kubi : {kub} Bu esa Kvadrati : {kvadrat}")
"""7 - vazifa"""
# sum = int(input("Son kiriting :"))
# full_Code = math.factorial(sum)
# print(f"{sum} factoryani {full_Code}")

"""8 - vazifa"""


# 9. List ichidagi eng katta sonni top.
# Masalan: [4, 7, 1, 9, 3]

# 10. Foydalanuvchi kiritgan matnni teskari qilib chiqar.
# Masalan: "salom" → "molas"

# 11. Son tub (prime) yoki yo‘qligini aniqlovchi dastur yoz.

# 12. 1 dan N gacha bo‘lgan sonlar yig‘indisini hisobla.

# 13. List ichidagi takrorlanadigan elementlarni olib tashla.

# 14. Parol tekshiruvchi dastur yoz. To‘g‘ri parol: "python123"

# 15. Oddiy kalkulyator yoz (+, -, *, /).
# 16. Random son o‘yini yoz.
# Kompyuter 1–10 orasida son o‘ylaydi, foydalanuvchi topishi kerak.
# (Buning uchun random modulidan foydalan.)
# 17. Matndagi harflar sonini hisoblovchi funksiya yoz.
# 18. Fibonacci ketma-ketligini N ta elementgacha chiqar.
# 19. Mini login tizimi yoz:
# Username va password to‘g‘ri bo‘lsa kirishga ruxsat.
# 20. Mini Bank Tizimi yoz.
# Talablar:
# Boshlang‘ich balans = 1000
# 1 – Pul qo‘shish
# 2 – Pul yechish
# 3 – Balansni ko‘rish
# 4 – Chiqish
# Agar balansdan ko‘p pul yechmoqchi bo‘lsa xatolik chiqsin
# while sikl ishlatish shart



# login = str(input("loginingizni kiriting :"))
# password = int(input("passwordingizni kiriting :"))

# if login == "codingbyumar@gmail.com":
#     text = "Sizning loginingiz to'gri , Saytga xush kelibsiz "
#     print(Fore.GREEN + text)
# elif password == 0000:
#     text = "Sizning loginingiz to'gri , Saytga xush kelibsiz "
#     print(Fore.GREEN + text)
# else:
#     text = "Try again ---Error---"
#     print(Fore.RED + text)



# New_Text = input("So'z kiriting : ")
# new_Color = input("Siz text qaysi rangda bolishini hohlaysiz : ")
# code_New = new_Color.lower().replace(" ", "")

# def Over_Color():
#     print("------------------------------------")

#     if code_New == "red":
#         print(Fore.RED + New_Text)
#     elif code_New == "blue":
#         print(Fore.BLUE + New_Text)
#     elif code_New == "yellow":
#         print(Fore.YELLOW + New_Text)
#     elif code_New == "white":
#         print(Fore.WHITE + New_Text)
#     elif code_New == "black":
#         print(Fore.BLACK + New_Text)
#     else:
#         print("Bunday rang mavjud emas!")

#     print(Style.RESET_ALL)
#     print("------------------------------------")

# Over_Color()

# soz = "Salom Muhammad Umar"

# def Red(text):
#     return Fore.RED + text

# print(Red(soz))



# funtion - vazifalar

# 1

# a = int(input("Son kiritng :"))
# b = int(input("Son kiriting :"))

# def get_Calculater(minus , pilus):
#     return minus + pilus

# full_Code = get_Calculater(a , b)
# print("Javob :" , full_Code)

# 2

# def Get_Minus(num , num1):
#     return num - num1

# resualt = Get_Minus(20 , 5) 
# print( "Javob :" , resualt)

# 3

# a = int(input("Son kiriting :"))
# operator = input("kub\kvadrat :")

# if operator == "kub":
#     full = f"Siz kubini so'radingiz mana sizga kub : {a ** 3}"
#     run = Fore.GREEN + full
#     print(run)
# elif open == "kvadrat":
#     full = f"Siz kubini so'radingiz mana sizga kub : {a ** 2}"
#     run = Fore.GREEN + full
#     print(run)
# else :
#     print(Fore.RED + "Siz xatolik sodir bo'ldi iltimos qayta urining !")


# 4
# print("------------------------------------------------------")

# Tushuncha = f"Siz bu kamculyator orqali + , - , * , /  \
# factorial , ekub , ekuk , kub , topishingiz mumkin : "
# print(Fore.GREEN + Tushuncha)

# print("------------------------------------------------------")

# a = float(input("Son kiriting a :"))
# b = float(input("Son kiriting b :"))
# operator = str(input('Siz nima qilmoqchisiz :'))

# if operator == "+":
#     full = a + b
#     print("------------------------------------------------------")
#     print(Fore.BLUE + "Javob :" , full)
#     print("------------------------------------------------------")
# elif operator == "-":
#     full = a - b
#     print("------------------------------------------------------")
#     print(Fore.BLUE + "Javob :" , full)
#     print("------------------------------------------------------")
# elif operator == "*":
#     full = a * b
#     print("------------------------------------------------------")
#     print(Fore.BLUE + "Javob :" , full)
#     print("------------------------------------------------------")
# elif operator == "/":
#     full = a / b
#     print("------------------------------------------------------")
#     print(Fore.BLUE + "Javob :" , full)
#     print("------------------------------------------------------")
# elif operator == "factorial":
#     full = math.factorial(a)
#     print("------------------------------------------------------")
#     print(Fore.BLUE + "Javob :" , full)
#     print("------------------------------------------------------")
# elif operator == "ekub":
#     full = math.gcd(int(a) , int(b))
#     print("------------------------------------------------------")
#     print(Fore.BLUE + "Javob :" , full)
#     print("------------------------------------------------------")
# elif operator == "ekuk":
#     full = math.lcm(int(a) , int(b))
#     print("------------------------------------------------------")
#     print(Fore.BLUE + "Javob :" , full)
#     print("------------------------------------------------------")
# else :
#     print("------------------------------------------------------")
#     print(Fore.RED + "Xatolik roy berdi iltimos qayta urining !")
#     print("------------------------------------------------------")
    
    

# 5
# name = str(input('Ismingiz kiriting :'))
# print("Salom" , name)

# 6
# a = int(input("Son kiriting :"))
# b = int(input("Son kiriting :"))
# full_Code = a + b
# print(full_Code)


# a = str(input("yil kiriting :"))
# oxirgi = a.replace(" " , "-")

# print("------------------------------")
# if oxirgi == "12-04-2008":
#     code = "muhammad umar".title()
#     sari = Fore.GREEN + code
#     print(sari)
# elif oxirgi == "14-06-2008":
#     code = "Mirjalol".title()
#     sari = Fore.GREEN + code
#     print(sari)
# else:
#     print(Fore.RED + "___Error___")

# print("------------------------------")



