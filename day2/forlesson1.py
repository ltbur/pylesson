scores = [80,20,75,60]
for data in scores:
    if data >= 60:
        print('合格')
    else:
        print('不合格')


ages = [28,50,8,20,78,25,22,10,27,33]
num = 5
samples = list()
for age in ages:
    if 20 <= age <30:
        if len(samples) < num:
            samples.append(age)
print(samples)



ages = [28,50,'ひみつ',20,78,25,22,10,'無回答',33]
samples = list()
for data in ages:
    #if not isinstance(data,int):
    if not type(data) is int:
        continue
    if data < 20  or data >= 30:
        continue
    samples.append(data)
print(samples)
