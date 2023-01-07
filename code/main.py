valorDespesas = []
def despesaCalc():
    despesas = input("Você tem despesas? ")

    if despesas == "s": 
        try:
            maisDespesas = ""

            while despesas == "s":
                valorDespesas.append(int(input("Digite sua despesa: R$")))
                maisDepesas = input("Gostaria de registar mais? S/N ")
                if maisDespesas != "s":
                    return despesaCalc()
        except:
            print(valorDespesas)
    else:
        print("Parabéns você não tem despesas")

if __name__ == "__main__":
    despesaCalc()
