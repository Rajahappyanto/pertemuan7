
print ('mengurutkan bilangan dari yang terkecil ke yang terbesar')
def pengulangan():
    print ('masukkan 3 bilangan yang diinginkan!')
    a=int(input('bilangan1 = '))
    b=int(input('bilangan2 = '))
    c=int(input('bilangan3 = '))

    if a<b and a<c:
        if b<c:
            print(a, b, c)
        else:
            print(a, c, b)
    elif b<a and b<c:
        if a<c:
            print(b, a, c)
        else:
            print(b, c, a)
    else:
        if a<b:
            print(c, a, b)
        else:
            print(c, b, a)

    print("")
    print('are you want to try it more? (yes/no)')
    x=input()
    if x=='yes':
        return pengulangan()
    if x=='no':
        print('have a nice day sir agung')
pengulangan()

