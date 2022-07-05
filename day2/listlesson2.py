import pprint
data=[[1,2,3],[4,5,6]]
print(data[1][2])

data=[
        [1,2,3],
            [4,5,6],
]
print(data)
print(data[1][1])   

data=[]
for i in range(10):
        temp=[]
        for j in range(10):
            temp.append(0)
        data.append(temp)
pprint.pprint(data)

data=[1,2,3]+[4,5]
print(data)

data=[1,2,3]*3
print(data)


data=[None]*10
for i in range(10):
    data[i]=[0]*10
pprint.pprint(data)


data=[[0]*10]*10
pprint.pprint(data)


data[1][1]=5
pprint.pprint(data)


data=[[0] * 10 for i in range(10)] # 0が10個並んだ配列を10回繰り返す
pprint.pprint(data)


data=[[i] * 10 for i in range(10)] 
pprint.pprint(data)


data[i for i in range(1,11)]
print(data)


