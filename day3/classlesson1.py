class Hero:
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp
    def sleep(self,hours):
        print('{}は{}時間寝た！'.format(self.name,hours))
        self.hp += hours

print('スッキリファンタジーXII ～金色の理想郷～')
h = Hero('松田',100)
h.sleep(3)
print('{}のHPは現在{}です'.format(h.name,h.hp))


scores1=[80,40,50]
scores2=[80,40,50]

print('scores1のidentity:{}'.format(id(scores1)))
print('scores2のidentity:{}'.format(id(scores2)))

if scores1 == scores2:
    print('scores1とscores2は同じ内容です')
else:
    print('scores1とscores2は違う内容です')

if id(scores1) == id(scores2):
    print('scores1とscores2は同じ内容です')
else:
    print('scores1とscores2は違う内容です')


names=list()
print('前:{}'.format(id(names)))
names.append('松田')
print('後:{}'.format(id(names)))

name='松田'
print('前:{}'.format(id(name)))
name=name+'さん'
print('後:{}'.format(id(name)))


