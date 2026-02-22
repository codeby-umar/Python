import mymodule
app = mymodule.calculyator("Muhammad Umar" , 19)
print(app)


from datetime import datetime , date , time , timedelta 

# kun = datetime.now() # hozirgi paytni olish
# print(kun)

# time = time(12 , 30 , 40) # qol bilan kiritish
# print(time)

# dates = date(4 , 12 , 2008)
# print(date)

# now = date(2008 , 4 , 12)
# futee = now + timedelta( days = 5)
# print(futee)




oy = int(input("Tug'ilgan oyingiz :"))
kun = int(input("Tug'ilgan kuningizni kiriting :"))
year = int(input("Tug'ilgan yilingizni kiriting :"))

over_Times = date(year , oy , kun)
print(over_Times)

now_Dates = date(2026 , 2 , 22 )
print(now_Dates)

jami = now_Dates - over_Times
print( "shuncha yashab qoyibsanku :" , jami)