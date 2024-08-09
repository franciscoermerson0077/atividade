nmb = ""
vmb = float('inf')
tdp = 0

for x in range(5):
    medicamento = input(f"Digite o nome do medicamento {x + 1}: ")
    preco = float(input(f"Digite o preço do medicamento {x + 1}: "))
    
    if preco < vmb:
        nmb = medicamento
        vmb = preco
    
    tdp += preco

media = tdp / 5

print(f"O medicamento mais barato é {nmb} com o preço de R$ {vmb:.2f}")
print(f"A média dos preços dos medicamentos é R$ {media:.2f}")
