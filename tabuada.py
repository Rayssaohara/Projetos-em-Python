
print("Olá)
a = 3
def tabuada(a):
    auxiliar = 0
    while (auxiliar <= 10):
        print('{} x {} = {} '. format(a,auxiliar, (auxiliar * a)))
        auxiliar = auxiliar + 1
    print('\n')
#tabuada(a)
for a in range(2,10):
    tabuada(a)
