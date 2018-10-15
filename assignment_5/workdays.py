def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True

def weekday_newyear(year):
    day = 0
    for x in range(1900, year):
        if(is_leap_year(x)):
           day += 2 
        else:
            day += 1
    return day % 7 

def is_workday(day):
    if(day < 5):
        return True
    else:
        return False

def workdays_in_year(year):
    days = 365
    if(is_leap_year(year)):
        days = 366

    start = weekday_newyear(year)
    days += start
    workdays = 0
    for x in range(start, days):
        if(x % 7 < 5):
            workdays += 1
    return workdays

days = ["man", "tir", "ons", "tor", "fre", "lør", "søn"]
for x in range(1900, 1920):
    print(x, days[weekday_newyear(x)]) 


for x in range(1900, 1920):
    print(x,"har",  workdays_in_year(x), "arbeidsdager") 

