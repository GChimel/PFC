despesas = input("Você tem despesas? ")

if despesas == "s":
    
    try:
        valorDespesas = []

        maisDespesas = ""

        while despesas == "s":

            valorDespesas.append(int(input("Digite sua despesa:")))

            maisDepesas = input("Gostaria de registar mais? S/N ")
    except:
        print(valorDespesas)
else:
    print("Parabéns você não tem despesas")

