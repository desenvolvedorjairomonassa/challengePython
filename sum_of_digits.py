#sum of digitis
def sum_of_digits(num: int):
    numstr = str(num)
    total = 0 
    for i in numstr:
        total += int(i)
    return total
