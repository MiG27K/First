#перевод из одной системы счисления в другую
def base(a, n):
    s = ''
    while a > 0:
        d = a % n
        a = a // n
        t = str(d)
        s = s + t
    print(s[::-1])
print(base(500, 5))
