#!/usr/bin/python

nsundays = 0

ndays = 0
day = 0
month = 0
year = 0

done = False

def nextday():
    global ndays, day, month, year, nsundays
    ndays += 1
    if month in (3, 5, 10) and ndays == 30:
        nextmonth()
    elif month == 1:
        if year % 4 == 0 and ndays == 29:
            if year % 100 != 0:
                nextmonth()
        elif ndays == 28:
            nextmonth()
    else:
        if ndays == 31:
            nextmonth()
    day = (day + 1) % 7
    if day == 6 and ndays == 0 and year > 0:
        nsundays += 1

def nextmonth():
    global month, ndays
    ndays = 0
    month = (month + 1) % 12
    if month == 0:
        nextyear()

def nextyear():
    global year, done
    year += 1
    if year == 101:
        done = True

while done == False:
    nextday()
print nsundays
