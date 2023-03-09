import re

f_nomes = open('./testes/nomesproprios.txt','w')
f_apelidos = open('./testes/apelidos.txt','w')


f = open('processos.txt','r')
lines=f.readlines()

"""
    Função responsável por imprimir uma tabela formatada, confoorme
    o dicionário passado como argumento
"""
def printDistribution2(someDict, text1, text2, text3):
    vazio = " "
    keys = list(someDict.keys())
    values = list(someDict.values())

    # Para prevenir o caso em que temos diferentes tamanhos
    max_col1_length = max([len(str(key)) for key in keys])
    max_col2_length = max([len(str(value)) for value in values])

    if max_col1_length < len(text1):
        max_col1_length = len(text1)

    max_col2_length = len(text2)

    max_col3_length = len(text3)

    # Cabeçalho da tabela
    print(f"\n+{'-' * (max_col1_length + 2)}-{'-' * (max_col2_length + 2)}-{'-' * (max_col3_length + 2)}+")
    print(f"| {text1.ljust(max_col1_length)} | {text2.ljust(max_col2_length)} | {text3.ljust(max_col3_length)} |")

    # Imprimir a tabela
    for i in range(len(keys)):
            print(f"|{'-' * (max_col1_length + 2)}|{'-' * (max_col2_length + 2)}|{'-' * (max_col3_length + 2)}|")
            flag=1    
            for j in  range(len(someDict[keys[i]][0])):
                if flag:
                    print(f"| {str(keys[i]).ljust(max_col1_length)} | {str(someDict[keys[i]][0][j]).ljust(max_col2_length)} | {str(someDict[keys[i]][1][j]).ljust(max_col3_length)} |")
                    flag=0
                else:
                    print(f"| {vazio.ljust(max_col1_length)} | {str(someDict[keys[i]][0][j]).ljust(max_col2_length)} | {str(someDict[keys[i]][1][j]).ljust(max_col3_length)} |")

    print(f"+{'-' * (max_col1_length + 2)}-{'-' * (max_col2_length + 2)}-{'-' * (max_col3_length + 2)}+")

"""
    Função responsável por fazer um dicionário com todos os séculos existentes no
    data set como key, o valor correspondente a cada século é 0, indicando o vazio
"""
def data_seculo(lines):
    lista=[]
    dictS = dict()
    exp1 = re.compile(r'::(?P<seculo>\d{4})-')
    for line in lines:
        lista_seculo = exp1.finditer(line)
        for seculo in lista_seculo:
            lista.append(seculo['seculo'])
    
    minimo = int(min(lista))
    maximo = int(max(lista))
    while minimo < maximo:
        dictS[(minimo,minimo+100)] = (dict(),dict())
        minimo+=100
    return dictS

"""
    Função responsável por fazer um dicionário com todos os séculos existentes no
    data set como key, e como valor correspondente a cada século é um dicionário que
    por sua vez, apresenta como chave o nome de uma pessoa e valor o número de ocrrencias 
    desse mesmo nome, obtemos assim um dicionário de séculos com as várias pessoas registadas
    em cada século
"""
def frequencia_por_nome(lines,dictSeculo):
    index=1
    key = (0,0)

    exp1 = re.compile(r'::(?P<seculo>\d{4})-')

    exp2 = re.compile(r'(?P<primeiro>[A-Z]([a-z])+)\s([A-Z][a-z]+\s)*(?P<apelido>[A-Z]([a-z])+)(::|,|\se)')
    
    for line in lines:
        match_seculo = exp1.search(line)
        if match_seculo:
            ano = match_seculo.group(1)
            
            for ano_seculo in dictSeculo.keys(): 
                if int(ano) > ano_seculo[0] and int(ano) < ano_seculo[1]:
                    key=(ano_seculo[0],ano_seculo[1])

            full_name = exp2.finditer(line)

            for name in full_name:
                dictNome = dictSeculo[key][0]
                dictApelido = dictSeculo[key][1]
                
                if name['primeiro'] in dictNome:
                    dictNome[name['primeiro']] += 1
                    f_nomes.write(str(index)+'|'+ano+'|'+name['primeiro']+'\n')
                else:
                    dictNome[name['primeiro']] = 1
                    f_nomes.write(str(index)+'|'+ano+'|'+name['primeiro']+'\n')
                if name['apelido'] in dictApelido:
                    dictApelido[name['apelido']]+=1
                    f_apelidos.write(str(index)+'|'+ano+'|'+name['primeiro']+'\n')
                else:
                    dictApelido[name['apelido']] = 1
                    f_apelidos.write(str(index)+'|'+ano+'|'+name['primeiro']+'\n')
                
                dictSeculo[key] = (dictNome,dictApelido)
        index+=1 
    
    return dictSeculo

"""
    Função responsável por ordenar os dois dicionáios presentes em dictS e em seguida
    devolver um dicionário com um tuplo correspondente à lista com o top 5 de nomes ou apelidos,
    correspondente, por século
"""
def getTop5(dictS):
    dictNew = dict()
    nomes_ord = []
    apelidos_ord = []
    nomes_top5 = []
    apelidos_top5 = []
    for key in dictS.keys(): 
        nomes = dictS[key][0]
        apelidos = dictS[key][1]
        
        nomes_ord = sorted(nomes, key=lambda x: nomes[x], reverse=True)
        apelidos_ord = sorted(apelidos, key=lambda x: apelidos[x], reverse=True)

        nomes_top5 = nomes_ord[:5]
        apelidos_top5 = apelidos_ord[:5]
        dictNew[key] = (nomes_top5,apelidos_top5)
    
    return dictNew



def printMenu():
    print("\n\n")
    print("+-| Frequêcia de processos por nome e apelido |-+")
    print("|                                                |")
    print("| Como pretende ver os dados?                    |")
    print("| (1) Numa tabela                                |")
    print("| (2) Impressos no terminal                      |")
    print("| (3) Sair                                       |")
    print("+--------------------|      |--------------------+")
    print("\n")
    return input(">>")


def menu():
    while True:
        option = printMenu()
        if option == "1":
            printDistribution2(getTop5(frequencia_por_nome(lines,data_seculo(lines))),"Século","Nome mais utilizado","Apelido mais utilizado")
        elif option == "2":
            print(getTop5(frequencia_por_nome(lines,data_seculo(lines))))
        elif option == "3":
            print("Programa interrompido!")
            exit(0)
        input(">>Pressione ENTER para voltar...")

menu()