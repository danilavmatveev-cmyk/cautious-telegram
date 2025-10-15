year = int(input())
cache = {}
def is_leap_year(year):

    if year in cache:
        return cache[year]
    if (year % 4 == 0 and year % 100 > 0) or year % 400 == 0:
        print(f"{year} - високосный год")
        cache[year] = True
        return True

    else:
        print(f"{year} - не високосный год")
        cache[year] = False
        return False

print(is_leap_year(year))

is_leap_year(year)
