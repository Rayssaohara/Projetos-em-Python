import matplotlib.pyplot as plt

arquivo = open('/home/rayssa/daniel graficos','r')
daniel = arquivo.read()
print(daniel)
daniel_lista = str(daniel)


daniel_lista = daniel_lista.replace('\n', ' ')
daniel_lista = daniel_lista.split(' ')

print(daniel_lista)



daniel_lista_a = []
daniel_lista_b = []
i = 0

print(daniel_lista.__len__())
for x in range:


# while (i < daniel_lista.__len__() - 1):
#     daniel_lista_a.insert(daniel_lista_a.__len__(), float(daniel_lista[i]))
#     daniel_lista_b.insert(daniel_lista_b.__len__(), float(daniel_lista[i+1]))
#     i = i + 2
#
# print(daniel_lista_a)
# print(daniel_lista_b)
#
# print(type(daniel_lista_a[0]))
# # plt.scatter(daniel_lista_a, daniel_lista_b)
# plt.plot(daniel_lista_a, daniel_lista_b)
# plt.show()
# #item = daniel_lista[0]
# #a = item.split(' ')
# #print(a)
#
#
# # arquivo.open('daniel graficos','r')
#
# # x = [1,2,3,4,5,6,7,8,9,10]
# # y = [1,2,3,4,5,6,7,8,9,10]
#
# #plt.scatter(x, y)
# # plt.plot(x, y)
# plt.show()