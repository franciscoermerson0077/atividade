a = int(input("Digite o valor de a:")
b = int(input("Digite o valor de b:")

if a < b:
  soma = 0
for i in range(a,b+1):
  soma += i 
print(f"A soma dos números inteiros no intervalo [{a}, {b}] é {soma}")
else:
  print("Erro: o valor de a deve ser menor que  valor de b.")
