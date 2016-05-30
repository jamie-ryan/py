import turtle as t
def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
           koch(t, order-1, size/3)
           t.left(angle)

ordr = 1 
siz = 100
kch = koch(t,ordr,siz)
