year = int(input("What year you want to check: "))

YearBy4 = (year / 4) 
YearBy100 = (year / 100)
YearBy400 = (year / 400)

if (YearBy4 - int(YearBy4)) == 0 and (YearBy100 - int(YearBy100)) == 0 and (YearBy400 - int(YearBy400)) == 0:
    print("Year is leap year")
elif (YearBy4 - int(YearBy4)) == 0 and (YearBy100 - int(YearBy100)) == 0:
    print("year is NOT leap year")
elif (YearBy4 - int(YearBy4)) == 0:
    print("year is leap year")
else:
    print("year is NOT leap year")
    
