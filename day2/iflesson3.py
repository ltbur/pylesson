scores={'network':60,'database':80,'security':50}
key=input('追加する科目を入力してください>>')
if key in scores:
    print('登録済みです')
else:
    data=int(input('得点>>'))
    scores[key]=data
print(scores)
