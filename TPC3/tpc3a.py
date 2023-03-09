import matplotlib.pyplot as plt
import re

f = open('processos.txt','r')
lines = f.readlines()

"""
    Função responsável por mostrar os dados num gráfico de barras
"""
def barChart(someDict,text1,text2):
    keys = list(someDict.keys())
    values = list(someDict.values())
    
    plt.bar(keys, values, color ='red', width = 0.6)
    plt.xticks(rotation=270, fontsize=5)
    
    plt.xlabel(text1)
    plt.ylabel(text2)
    plt.tight_layout()
    plt.show()
"""
    Função responsável por imprimir uma tabela formatada, confoorme
    o dicionário passado como argumento
"""
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

"""
    Função responsável por coletar todos os processos desenvolvidos no mesmo ano,
    retorna um dicionário tendo como chave o ano e valor o número de processos 
    elaborados nesse mesmo ano
"""
def processos_por_ano(lines):
    dictA = dict()
    exp1 = re.compile(r'::(?P<ano>\d{4})-')
    for line in lines:
        ano = exp1.search(line)
        if ano:
            if ano.group(1) in dictA:
                dictA[ano.group(1)]+=1
            else:
                dictA[ano.group(1)] = 1
    return dictA

def printMenu():
    print("\n\n")
    print("+------| Frequência de processos por ano |-------+")
    print("|                                                |")
    print("| Como pretende ver os dados?                    |")
    print("| (1) Num grádico de barras                      |")
    print("| (2) Numa tabela                                |")
    print("| (3) Impressos no terminal                      |")
    print("| (4) Sair                                       |")
    print("+--------------------|      |--------------------+")
    print("\n")
    return input(">>")


def menu():
    while True:
        option = printMenu()
        if option == "1":
            barChart(processos_por_ano(lines),"Ano","Nº processo")
        elif option == "2":
            printDistribution(processos_por_ano(lines),"Ano","Nº processo")            
        elif option == "3":
            print(processos_por_ano(lines))            
        elif option == "4":
            print("Programa interrompido!")
            exit(0)
        input(">>Pressione ENTER para voltar...")

menu()