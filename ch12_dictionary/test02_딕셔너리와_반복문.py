info1 = {'name': '홍길동', 'age': 19, 'tel': '010-1111-2222', 'vip': False}

for e in info1:  # e: name, age, tel, vip
    print(e, info1[e])
# name 홍길동
# age 19
# tel 010-1111-2222
# vip False


for key in info1.keys():  # key: name, age, tel, vip
    print(key, info1[key])
# name 홍길동
# age 19
# tel 010-1111-2222
# vip False

for value in info1.values():
    print(value)
# 홍길동
# 19
# 010-1111-2222
# False

entities = info1.items()
print(entities)  # dict_items([('name', '홍길동'), ('age', 19), ('tel', '010-1111-2222'), ('vip', False)])
for k, v in info1.items():
    print(k, v)
# name 홍길동
# age 19
# tel 010-1111-2222
# vip False
