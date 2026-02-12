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



