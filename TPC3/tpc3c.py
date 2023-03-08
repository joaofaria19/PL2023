import matplotlib.pyplot as plt
import re

f = open('processos.txt','r')
lines = f.readlines()

output = open('./testes/outputRelacao.txt','w')

"""
    Função responsável por mostrar os dados num gráfico de barras
"""
def barChart(someDict,text1,text2):
    keys = list(someDict.keys())
    values = list(someDict.values())
    
    plt.bar(keys, values, color ='red', width = 0.6)
    plt.xticks(rotation=300, fontsize=6)
    
    plt.xlabel(text1)
    plt.ylabel(text2)
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

# Apanhar todos os parentescos
def parentesco(lines):
    dictP = dict()
    er1 = re.compile(r'(,(?P<parentesco>[A-Z][a-z]+(\s[A-Z][a-z]+)*)(\.|,)(\s*Proc))')
    n_line = 1
    for line in lines:
        match = er1.search(line)
        if match:
            matchAll = er1.finditer(line)
            for p in matchAll:
                if p['parentesco'] in dictP:
                    dictP[p['parentesco']]+=1
                else:
                    dictP[p['parentesco']] = 1
                output.write(str(n_line)+"|"+p['parentesco']+'\n')
        n_line+=1
    return dictP

barChart(parentesco(lines),"Grau de parentesco", "Nº de encontrados")
printDistribution(parentesco(lines),"Grau de parentesco", "Nº de encontrados")
        

