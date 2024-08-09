senhacorreta = 123456
tmx = 3  

for i in range(3):
    senha = int(input(f"Digite sua senha: "))

    if senha == senhacorreta:
        print("senha correta")
        exit()
    else:
        tentativas = tmx - (i + 1)
        if tentativas > 0:
            print(f"senha incorreta! voce ainda tem {tentativas} tentativas")
        else:
            print("conta bloqueada")
