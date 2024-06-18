### check if year is leap year in the gregorian calendar

def is_leap(year):
    year = int(year)
    leap = False
    century = (year % 100 == 0)
    leap = (year>=1900) and (year<= 100000)

    leap = leap and ((century and year % 400 == 0) or (not century and year % 4 == 0))
    return leap
