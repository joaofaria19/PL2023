import matplotlib.pyplot as plt

#Função responsável por mostrar os dados num gráfico de barras
def barChart(someDict,text1,text2):
    keys = list(someDict.keys())
    values = list(someDict.values())
    
    plt.barh(keys, values, color ='red', height = 0.4)
    plt.xlabel(text2)
    plt.ylabel(text1)
    plt.show()

# Função responsável por mostar os dados num gráfico circular
def pieChart(someDict,text):
    keys = list(someDict.keys())
    values = list(someDict.values())
    
    plt.pie(values, startangle=90)
    plt.legend(title=text,labels=keys)
    plt.show()



# Função responsável por verificar se uma dada linha retirada do .csv
# é considerada válida
def verifyLine(line):
    flagDigits = False
    flagSexo = False
    flagDoenca = False

    # necessário retirar o '\n' da linha
    paciente = line.strip().split(',')
    if len(paciente) == 6:
        if paciente[1] == "M" or paciente[1] == "F":
            flagSexo = True
        if paciente[0].isdigit() and paciente[2].isdigit() and paciente[3].isdigit() and paciente[4].isdigit():
            flagDigits = True
        if paciente[5].isdigit() and (int(paciente[5]) == 0 or int(paciente[5]) == 1):
            flagDoenca = True

    return flagDigits and flagSexo and flagDoenca


# Guarda em memória a lista detodos os pacientes
def saveData(lines):
    pacientes = []
    lines.pop(0)

    for line in lines:
        paciente = line.strip().split(',', 6)
        idade = paciente[0]
        sexo = paciente[1]
        tensao = paciente[2]
        colesterol = paciente[3]
        batimento = paciente[4]
        doenca = paciente[5]

        if verifyLine(line): pacientes.append(
            (int(idade), sexo, int(tensao), int(colesterol), int(batimento), int(doenca)))

    return pacientes

# Devolcve um dicionário com a distribuição da doença por sexo
def illnessByGender(pacientes):
    dictGenders = dict()
    dictGenders["M"] = 0
    dictGenders["F"] = 0
    for paciente in pacientes:
        if (paciente[5] == 1 and paciente[1] == "M"):
            dictGenders["M"] += 1
        elif (paciente[5] == 1 and paciente[1] == "F"):
            dictGenders["F"] += 1

    return dictGenders

# Devolcve um dicionário com a distribuição da doença por faixa etária
def illnessByAgeGroup(pacientes):
    dictAgeGroup = dict()

    for paciente in pacientes:
        if (paciente[5] == 1):
            ageG = int(paciente[0] / 5)
            key = str(ageG * 5)+"-"+str((ageG * 5) + 4)
            if (key in dictAgeGroup):
                dictAgeGroup[key] += 1
            else:
                dictAgeGroup[key] = 1
    return dictAgeGroup

# Devolve um tuplo com o menor e o maior valor de colesterol registados
def getMinMax(pacientes):
    paciente = pacientes[1]
    min = paciente[3]
    max = paciente[3]
    # remover a primeira linha do .csv (idade,sexo,tensao,colesterol,batimento,temDoenca)
    pacientes.pop(0)
    for paciente in pacientes:
        if (paciente[5] == 1 and min > paciente[3]):
            min = paciente[3]
        elif (paciente[5] == 1 and max < paciente[3]):
            max = paciente[3]
    return (min, max)

# Devolcve um dicionário com a distribuição da doença por faixa etária
def illnessByColesterol(pacientes):
    dictAgeGroup = dict()
    min_max = getMinMax(pacientes)
    aux = min_max[0]

    while aux <= min_max[1]:
        indice = str(aux)+"-"+str(aux + 9)
        aux += 10
        dictAgeGroup[indice] = 0

    for paciente in pacientes:
        ageG = int(paciente[3] / 10)
        key = str((ageG * 10) + min_max[0])+"-"+str((ageG * 10) + 9 + min_max[0])
        dictAgeGroup[key] += 1
    return dictAgeGroup

# Função responsável por imprimir uma tabela formatada, confoorme
# o dicionário passado como argumento
def printDistribution(someDict, text1, text2):
    keys = list(someDict.keys())
    values = list(someDict.values())

    # Para prevenir o caso em que temos diferentes tamanhos
    max_key_length = max([len(str(key)) for key in keys])
    max_value_length = max([len(str(value)) for value in values])

    if max_key_length < len(text1): max_key_length = len(text1)
    if max_value_length < len(text2): max_value_length = len(text2)

    # Cabeçalho da tabela
    print(f"\n+{'-' * (max_key_length + 2)}-{'-' * (max_value_length + 2)}+")
    print(f"| {text1.ljust(max_key_length)} | {text2.ljust(max_value_length)} |")

    # Imprimir a tabela
    for i in range(len(keys)):
        print(f"|{'-' * (max_key_length + 2)}|{'-' * (max_value_length + 2)}|")
        print(f"| {str(keys[i]).ljust(max_key_length)} | {str(values[i]).ljust(max_value_length)} |")
    print(f"+{'-' * (max_key_length + 2)}-{'-' * (max_value_length + 2)}+")

# Função que imprime todas as tabelas pedidas
def printAllDistribution(pacientes):
    dictG = illnessByGender(pacientes)
    dictAG = illnessByAgeGroup(pacientes)
    dictCol = illnessByColesterol(pacientes)
    printDistribution(dictG, "Sexo", "Quantidade")
    printDistribution(dictAG, "Idade", "Quantidade")
    printDistribution(dictCol, "Nível", "Quantidade")

# Função que imprime um menu onde o usuário pode optar sobre o que pretende mostrar
def printMenu():
    print("\nQue distribuição pretende ver?\n")
    print("(1) Distribuição da doença por sexo.")
    print("(2) Distribuição da doença por faixa etária.")
    print("(3) Distribuição da doença por nível de colesterol.")
    print("(4) Todas as distribuições.")
    print("(5) Sair.")
    return input(">> ")

# Função que imprime um segundo menu onde o usuário pode optar sobre a forma como pretende visualizar os dados
def print2Menu():
    print("\nDe que forma pretende ver os dados?\n")
    print("(1) Tabela.")
    print("(2) Gráfico de Barras.")
    print("(3) Gráfico Circular.")
    print("(4) Voltar.")
    return input(">> ")

# Função que lê de um ficheiro .csv todas as linhas e retorna as mesmas numa lista
def readfile():
    # Abrir um ficheiro em python
    file = open('myheart.csv', 'r')

    # Lê todas as linhas do ficheiro
    lines = file.readlines()

    #Fechar o ficheiro
    file.close()
    return lines

# Função que trata da visualização dos dados conforme o input do usuário
def minirun(someDict,last_option):
    option = print2Menu()
    if option == "1" and last_option=="1":
        printDistribution(someDict, "Sexo", "Quantidade")
    elif option == "1" and last_option=="2":
        printDistribution(someDict, "Idade", "Quantidade")
    elif option == "1" and last_option=="3":
        printDistribution(someDict, "Nível", "Quantidade")
    elif option == "2" and last_option=="1":
        barChart(someDict, "Sexo", "Nº de doentes")
    elif option == "2" and last_option=="2":
        barChart(someDict, "Faixa etária", "Nº de doentes")
    elif option == "2" and last_option=="3":
        barChart(someDict, "Nível de Colesterol", "Nº de doentes")
    elif option == "3" and last_option=="1":
        pieChart(someDict, "Sexo: ")
    elif option == "3" and last_option=="2":
        pieChart(someDict, "Faixa etária: ")
    elif option == "3" and last_option=="3":
        pieChart(someDict, "Níveis de Colesterol")
    
    
# Função principal do programa
# Responsável por ligar a opção do usuário à tabela que deve ser imprimida
def run():
    lines = readfile()
    pacientes = saveData(lines)

    while True:
        option = printMenu()
        if option == "1":
            dictG = illnessByGender(pacientes)
            minirun(dictG,"1")

        elif option == "2":
            dictAG = illnessByAgeGroup(pacientes)
            minirun(dictAG,"2")
            
        elif option == "3":
            dictCol = illnessByColesterol(pacientes)
            minirun(dictCol,"3")
            
        elif option == "4":
            dictG = illnessByGender(pacientes)
            dictAG = illnessByAgeGroup(pacientes)
            dictCol = illnessByColesterol(pacientes)
            printDistribution(dictG, "Sexo", "Quantidade")
            printDistribution(dictAG, "Idade", "Quantidade")
            printDistribution(dictCol, "Nível", "Quantidade")
            
        elif option == "5":
            print("Programa interrompido!")
            exit(0)
        else:
            print("Opção inválida.\n")
        input("\nPressione ENTER para voltar atrás....")


def main():
    run()

if __name__ == "__main__":
    main()
