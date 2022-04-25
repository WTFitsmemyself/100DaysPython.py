# Date: 2022/04/07
# Import Libraries
from importlib.resources import contents
from tkinter import W
import tarikh
import datetime
import os.path

#Date Conveersion
Date = str(datetime.date.today())
date_spilit = Date.split("-")
year_now = int(date_spilit[0])
month_now = int(date_spilit[1])
day_now = int(date_spilit[2])

#Check if file exists
file = os.path.isfile('./counter.txt')
if file == False:
    file = open("counter.txt","w+")
    file.write("0")
    file.close()

# Creating essentional variables for reaching to Final Number
last_gardon_number = int(input("How many Gardon you produced today?: "))
Shomare_Tamin_Konande = "S"
Shomare_Sazande = "F9" 
Shomare_Ghate = "AS"
tarikh__shamsi = tarikh.gregorian_to_jalali(year_now,month_now,day_now,)
sal = 0
mah = 0
rooz = 0
Shomare_Serial = 0
weight = ['8','7','6','5','4','3','2','9','1','9','8','7','6']
temp = [1, 2, 3, 4, 5, 6, 7, "8"]
Shomare_Serial_Bedone_Tabdil_harf_ha = []

#Converting year to alphabetic year
if tarikh__shamsi[0] == 1401:
    sal = "A"
elif tarikh__shamsi[0] == 1402:
    sal = "B"
elif  tarikh__shamsi[0] == 1403:
    sal = "C"
elif tarikh__shamsi[0] == 1404:
    sal = "D"
elif tarikh__shamsi[0] == 1405:
    sal = "E"
elif tarikh__shamsi[0] == 1406:
    sal = "F"
elif tarikh__shamsi[0] == 1407:
    sal = "G"
elif tarikh__shamsi[0] == 1408:
    sal = "H"
elif tarikh__shamsi[0] == 1409:
    sal = "J"
elif tarikh__shamsi[0] == 1410:
    sal = "K"
elif tarikh__shamsi[0] == 1411:
    sal = "L"


#Converting month
if tarikh__shamsi[1] == 1:
    mah = "0"
elif tarikh__shamsi[1] == 2:
    mah = "1"
elif tarikh__shamsi[1] == 3:
    mah = "2"
elif tarikh__shamsi[1] == 4:
    mah = "3"
elif tarikh__shamsi[1] == 5:
    mah = "4"
elif tarikh__shamsi[1] == 6:
    mah = "5"
elif tarikh__shamsi[1] == 7:
    mah = "6"
elif tarikh__shamsi[1] == 8:
    mah = "7"
elif tarikh__shamsi[1] == 9:
    mah = "8"
elif tarikh__shamsi[1] == 10:
    mah = "9"
elif tarikh__shamsi[1] == 11:
    mah = "A"
elif tarikh__shamsi[1] == 12:
    mah = "B"

#Converting day
if tarikh__shamsi[2] == 1:
    rooz = "0"
elif tarikh__shamsi[2] == 2:
    rooz = "1"
elif tarikh__shamsi[2] == 3:
    rooz = "2"
elif tarikh__shamsi[2] == 4:
    rooz = "3"
elif tarikh__shamsi[2] == 5:
    rooz = "4"
elif tarikh__shamsi[2] == 6:
    rooz = "5"
elif tarikh__shamsi[2] == 7:
    rooz = "6"
elif tarikh__shamsi[2] == 8:
    rooz = "7"
elif tarikh__shamsi[2] == 9:
    rooz = "8"
elif tarikh__shamsi[2] == 10:
    rooz = "9"
elif tarikh__shamsi[2] == 11:
    rooz = "A"
elif tarikh__shamsi[2] == 12:
    rooz = "B"
elif tarikh__shamsi[2] == 13:
    rooz = "C"
elif tarikh__shamsi[2] == 14:
    rooz = "D"
elif tarikh__shamsi[2] == 15:
    rooz = "E"
elif tarikh__shamsi[2] == 16:
    rooz = "F"
elif tarikh__shamsi[2] == 17:
    rooz = "G"
elif tarikh__shamsi[2] == 18:
    rooz = "H"
elif tarikh__shamsi[2] == 19:
    rooz = "J"
elif tarikh__shamsi[2] == 20:
    rooz = "K"
elif tarikh__shamsi[2] == 21:
    rooz = "L"
elif tarikh__shamsi[2] == 22:
    rooz = "M"
elif tarikh__shamsi[2] == 23:
    rooz = "N"
elif tarikh__shamsi[2] == 24:
    rooz = "P"
elif tarikh__shamsi[2] == 25:
    rooz = "R"
elif tarikh__shamsi[2] == 26:
    rooz = "S"
elif tarikh__shamsi[2] == 27:
    rooz = "T"
elif tarikh__shamsi[2] == 28:
    rooz = "V"
elif tarikh__shamsi[2] == 29:
    rooz = "W"
elif tarikh__shamsi[2] == 30:
    rooz = "X"
elif tarikh__shamsi[2] == 31:
    rooz = "Y"

def tabdil(x):
    for i in range(0, 8):
        new = x[i] 
        if new == "A":
            new = "1"
        elif new == "B":
            new = "2"
        elif new == "C":
            new = "3"
        elif new == "D":
            new = "4"
        elif new == "E":
            new = "5"
        elif new == "F":
            new = "6"
        elif new == "G":
            new = "7"
        elif new == "H":
            new = "8"
        elif new == "J":
            new = "9"
        elif new == "K":
            new = "9"
        elif new == "L":
            new = "8"
        elif new == "M":
            new = "7"
        elif new == "N":
            new = "6"
        elif new == "P":
            new = "5"
        elif new == "R":
            new = "4"
        elif new == "S":
            new = "3"
        elif new == "T":
            new = "2"
        elif new == "V":
            new = "1"
        elif new == "W":
            new = "3"
        elif new == "X":
            new = "6"
        elif new == "Y":
            new = "9"
        temp[i] = new
    adad__tabdili = (str(temp[0]) +str(temp[1]) +str(temp[2]) +str(temp[3]) +str(temp[4]) +str(temp[5]) + str(temp[6]) +str(temp[7]) + str(Shomare_Serial))
    # print(f"adad = {adad__tabdili}")
    return adad__tabdili

def m(x):
    summ = 0
    for i in range(0,len(weight)):
        multiply = int(x[i]) * int(weight[i])
        summ += multiply
        # print(summ)
    m = summ % 10
    # print(f"sum : {summ}")
    # print(f"m : {m}")
    return m

f = open("./counter.txt","r")
for i in range(int(f.read())+1, last_gardon_number+1):
    if i < 10:
        Shomare_Serial = "0000" + str(i)
        Shomare_Serial_Bedone_Tabdil_harf_ha = Shomare_Tamin_Konande + Shomare_Sazande + Shomare_Ghate + str(sal) + str(mah) + str(rooz) + str(Shomare_Serial)
        adad = tabdil(Shomare_Serial_Bedone_Tabdil_harf_ha)
        adad14om = m(adad)
        print(f"Gardon {i} = {Shomare_Serial_Bedone_Tabdil_harf_ha} {adad14om}")
        print("----------------------------------------------------------------")
    elif i > 9 and i < 100:
        Shomare_Serial = "000" + str(i)
        Shomare_Serial_Bedone_Tabdil_harf_ha = Shomare_Tamin_Konande + Shomare_Sazande + Shomare_Ghate + str(sal) + str(mah) + str(rooz) + str(Shomare_Serial)
        adad = tabdil(Shomare_Serial_Bedone_Tabdil_harf_ha)
        adad14om = m(adad)
        print(f"Gardon {i} = {Shomare_Serial_Bedone_Tabdil_harf_ha} {adad14om}")
        print("----------------------------------------------------------------")
    elif i > 99 and i < 1000:
        Shomare_Serial = "00" + str(i)
        Shomare_Serial_Bedone_Tabdil_harf_ha = Shomare_Tamin_Konande + Shomare_Sazande + Shomare_Ghate + str(sal) + str(mah) + str(rooz) + str(Shomare_Serial)
        adad = tabdil(Shomare_Serial_Bedone_Tabdil_harf_ha)
        adad14om = m(adad)
        print(f"Gardon {i} = {Shomare_Serial_Bedone_Tabdil_harf_ha} {adad14om}")
        print("----------------------------------------------------------------")
    elif i > 999 and i < 10000:
        Shomare_Serial = "0" + str(i)
        Shomare_Serial_Bedone_Tabdil_harf_ha = Shomare_Tamin_Konande + Shomare_Sazande + Shomare_Ghate + str(sal) + str(mah) + str(rooz) + str(Shomare_Serial)
        adad = tabdil(Shomare_Serial_Bedone_Tabdil_harf_ha)
        adad14om = m(adad)
        print(f"Gardon {i} = {Shomare_Serial_Bedone_Tabdil_harf_ha} {adad14om}")
        print("----------------------------------------------------------------")
    elif i > 9999 and i < 100000:
        Shomare_Serial = str(i)
        Shomare_Serial_Bedone_Tabdil_harf_ha = Shomare_Tamin_Konande + Shomare_Sazande + Shomare_Ghate + str(sal) + str(mah) + str(rooz) + str(Shomare_Serial)
        adad = tabdil(Shomare_Serial_Bedone_Tabdil_harf_ha)
        adad14om = m(adad)
        print(f"Gardon {i} = {Shomare_Serial_Bedone_Tabdil_harf_ha} {adad14om}")
        print("----------------------------------------------------------------")
        
str_last_num = str(last_gardon_number)
f = open("./counter.txt","w")
f.write(str_last_num)
f.close