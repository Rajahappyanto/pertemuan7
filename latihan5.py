a = int(input('masukkan bilangan 1 : '))
b = int(input('masukkan bilangan 2 : '))
c = int(input('masukkan bilangan 3 : '))
if a > b:
    if a  > c:
        print('\nBilangan terbesar = ', a)
    elif b > c:
        print('\nBilangan terbesar = ', b)
    else:
        print('\nBilangan terbesar = ', c)