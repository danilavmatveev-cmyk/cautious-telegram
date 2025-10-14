year = int(input())
cache = {}
def is_leap_year(year):

    if year in cache:
        return cache[year]
    if (year % 4 == 0 and year % 100 > 0) or year % 400 == 0:
        cache[year] = True
        return True
    else:
        return False
    
print(is_leap_year(year))