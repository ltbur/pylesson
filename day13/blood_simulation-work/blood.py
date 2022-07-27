import numpy as np

type_parents = np.array([{"O","O"},{"O","A"},{"O","B"},
                         {"O","Z"},{"A","A"},{"A","B"},
                         {"A","Z"},{"B","B"},{"B","Z"},
                         {"Z","Z"}])

type_child = np.array([[1.00, 0.00, 0.00, 0.00],
                       [0.40, 0.60, 0.00, 0.00],
                       [0.43, 0.00, 0.57, 0.00],
                       [0.00, 0.50, 0.50, 0.00],
                       [0.16, 0.84, 0.00, 0.00],
                       [0.17, 0.26, 0.23, 0.34],
                       [0.00, 0.50, 0.20, 0.30],
                       [0.19, 0.00, 0.81, 0.00],
                       [0.00, 0.22, 0.50, 0.28],
                       [0.00, 0.25, 0.25, 0.50]])

def rand_blood(p=[0.32, 0.37, 0.22, 0.09]):
    bt_list = ["O", "A", "B", "AB"]
    prob = p
    brand = np.random.choice(bt_list, p=prob)
    return brand

def inherit_blood(b1, b2):
    if b1 == "AB":
        b1 = "Z"
    if b2 == "AB":
        b2 = "Z"
    idx_arr = np.where(type_parents == {b1, b2})
    idx = idx_arr[0][0]
    prop = type_child[idx]
    return rand_blood(p=prop)

print('こどもの血液型をシミュレーションします。')
btm=input('母親の血液型を入力してください（半角ローマ字）>')
btf=input('父親の血液型を入力してください（半角ローマ字）>')
nt=int(input('試行回数を入力してください>'))

res = []
for i in range(nt):
    btc = inherit_blood(btm, btf)
    res.append(btc)    
print(res)
