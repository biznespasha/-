import os
h = [-2,9,8,7,4,5,6,3,2,1,5,5]
#большое количество кода
#newh = []
#for x in h:
#     newh.append(x*2)
#print(newh)
#тоже что и сверху только лучше
#newh2 = [x*2 for x in h]
#z = {x*2 for x in h}
#f = {x: x*2 for x in h}
#print(newh2)
#print(z)
#print(f)
#g = [x for x in h if x % 2 == 0 and x > 0]
#print(g)
price = {'m':2, "b":1, 'p': 0.5, 'w': 3}
new_d = {i: round(price[i] * 0.85, 2) for i in price.keys()}
print(new_d)