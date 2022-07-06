"""
text=input('何を記録>>')
file=open('diary.txt','a')
file.write(text + '\n')
file.close()
"""
text=input('記録>>')
with open('diary.txt','a',encoding='utf-8') as file:
    file.write(text+'\n')
