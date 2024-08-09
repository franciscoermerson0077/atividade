termo = int(input("Primeiro termo: "))
quantidade = int(input("Quaantidade de termos: "))
razao = int(input("Razão: "))
a = 0
for x in range(termo, quantidade+1, razao):
    a += x
print(a)
