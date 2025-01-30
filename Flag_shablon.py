#flag shablon
for x1 in range(1, 1001):
    fl = True
    for x2 in range(1, 1001):
        if not condition:
            fl = False
            break
    if fl == True:
        print(x1) #или x2, но обычно x1
        break #если надо найти наименьшее(если надо наибольшее - не ставим)
