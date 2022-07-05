def is_leapyear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

year = int(input('何年?>>'))
if is_leapyear(year):
        print(f'{year}年はうるう年です')
else:
        print(f'{year}年はうるう年ではありません')
