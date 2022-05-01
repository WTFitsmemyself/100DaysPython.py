def leapYear(year):
    YearBy4 = (year / 4) 
    YearBy100 = (year / 100)
    YearBy400 = (year / 400)

    if (YearBy4 - int(YearBy4)) == 0 and (YearBy100 - int(YearBy100)) == 0 and (YearBy400 - int(YearBy400)) == 0:
        return True
    elif (YearBy4 - int(YearBy4)) == 0 and (YearBy100 - int(YearBy100)) == 0:
        return False
    elif (YearBy4 - int(YearBy4)) == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leapYear(year) == True and month == 2:
        return month_days[1] + 1
    else:
        return month_days[month-1]
        
    
year = int(input("Enter a year: "))
month = int(input("Enter the month: "))
days = days_in_month(year, month)
print(f"The {month} month of year {year} have {days}days")