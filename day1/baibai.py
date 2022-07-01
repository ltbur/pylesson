n=1#栗まんじゅう
minute=0
days=1
day_minute=days*60*24#mins
while minute < day_minute:
    n*=2
    minute+=5
    print(minute,'分後',n)
print(n)
