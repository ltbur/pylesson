name='松田'

def hello():
    name='山田'
    print('こんにちは',name,'さん')

hello()
print(name)


name='松田'

def hello():
    global name
    name='山田'
    print('こんにちは',name,'さん')

hello()
print(name)
