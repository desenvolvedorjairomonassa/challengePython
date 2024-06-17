### check if year is leap year

def is_leap(year):
    leap = False
    
    leap = (year//100 == 0) and (year//4 == 0)
    
    return leap
