name=input('あなたの名前を教えてください>>')
print('{}さん、こんにちは'.format(name))
food=input('{}さんの好きなたべものは何ですか？>>'.format(name))
if 'カレー' in food:
    print('素敵です。カレーは最高ですよね！')
else:
    print('私も{}が好きですよ'.format(food))
