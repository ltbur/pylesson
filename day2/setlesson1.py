scores={70,80,55,80}
scores.add(80)
print(scores)
print(len(scores))
print(sum(scores))

scores={'network':60,'database':80,'security':60}
members=['松田','浅木','工藤']
print(tuple(members))
print(list(scores))
print(set(scores.values()))


matsuda_scores={'network':60,'database':80,'security':50}
asagi_scores={'network':80,'database':75,'security':92}
member_scores={
        '松田':matsuda_scores,
        '浅木':asagi_scores,
        }
print(member_scores['松田']['network'])


member_hobbies = {
        '松田':{'SNS','麻雀','自転車'},
        '浅木':{'麻雀','食べ歩き','数学','数学','数学'}
        }
print(member_hobbies)
print(member_hobbies['松田'])
print(member_hobbies['浅木'])


a=[1,2,3]
b=[4,5,6]
c=[a,b]
print(c)
print(c[0])
print(c[1][2])

common_hobbies=member_hobbies['松田'] & member_hobbies['浅木']
print(common_hobbies)


A={1,2,3,4}
B={2,3,4,5}
print(A|B)
print(A&B)
print(A-B)
print(A^B)
