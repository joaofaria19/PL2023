import re
import ply.lex as lex
import sys

moedas_exp = re.compile(r'^MOEDA\s+(?P<moedas>(\d+(c|e)(,\s*|(?=;)|(?=.))*)*)')

numero_exp = re.compile(r'^T=\s*(?P<numero>\d{9,})$')

"""
    Função responsável por pegar num número correspondente a uma moeda ou à soma 
de várias moedas, e transformar esse número no respetivo formato, uma string correspondente 
ao valor introduzido.
"""
def intToStringCoin(moeda):
    moeda_euro = int(moeda/100)
    moeda_cent = moeda - 100*moeda_euro
    moeda_string = ''
    if moeda_euro>0 and moeda_cent <= 0:
        moeda_string = str(moeda_euro)+'e'
    elif moeda_euro > 0:
        moeda_string = str(moeda_euro)+'e'+str(moeda_cent)+'c'
    else:
        moeda_string = str(moeda_cent)+'c'
    return moeda_string

"""
    Função responsável por verificar as várias moedas introduzidas, recebe portanto a lista de moedas introduzidas. 
Se a moeda for válida esta é adicionada ao valor total de moedas, se a moeda for inválida 
é acrescentada à lista de moedas inválidas. No final é retornado um tuplo contendo o valor total de moedas e 
a lista de moedas inválidas (que será convertida numa única string), respetivamente.
"""
def moeda_handler(lista_moedas):
    moedas_validas = ['5c','10c','20c','50c','1e','2e']
    moedas_total = 0
    moedas_invalidas = []
    
    for moeda in lista_moedas:
        if moeda not in moedas_validas:
            moedas_invalidas.append(moeda)
        else:
            if moeda == '1e' or moeda == '2e':
                moeda = moeda[:-1]
                moeda = int(moeda) * 100
            else: 
                moeda = moeda[:-1]
            moedas_total += int(moeda)
    
    moeda_invalidas_string=''

    if len(moedas_invalidas) > 0:
        for moeda in moedas_invalidas:
            moeda_invalidas_string += moeda+", "

    return (moedas_total,moeda_invalidas_string)

"""
    Função run trata de todo o processo para a realização de uma chamada.
Para cada opção disponível faz a devida verificação se a mesma pode ocorrer ou não.
Faz uso de uma stack que permite guardar o estado em que o programa se encontra.
"""
def run():
    saldo = 0
    stack  = []
    for linha in sys.stdin:
        if linha.strip().upper() == 'LEVANTAR' and len(stack) == 0:
            print("maq: 'Introduza moedas'")
            stack.append(linha.strip())

        elif len(stack) > 0  and moedas_exp.match(linha.strip()):
            if stack[-1].upper() == 'LEVANTAR' or stack[-1].upper() == 'MOEDA':
                moedas = moedas_exp.match(linha).group('moedas').split(',')
                (total, invalidas) = moeda_handler(moedas)
                saldo += total
                total_string = intToStringCoin(saldo)
                if len(invalidas) == 0:
                    print('maq: "saldo = '+ total_string +'"')
                else:
                    print('maq: "'+ str(invalidas) +' moeda inválida, saldo = '+total_string+'"')
                stack.append('MOEDA')

        elif len(stack)>0 and numero_exp.match(linha.strip()):
            if stack[-1].upper() == 'MOEDA': 
                numero = numero_exp.match(linha).group('numero')
                if len(numero) >= 9 :
                    if numero[:3] == '601' or numero[3:] == '641':
                        print('maq: "Esse número não é permitido neste telefone. Queira disque um novo número"')
                    elif numero[:2] == '00':
                        if saldo>150:
                            saldo-=150
                            stack.append('T')
                            print('maq: "saldo %s"' % intToStringCoin(saldo))
                        else:    
                            print('maq: "Saldo insuficiente, necessário 1e50c para realizar a chamada"')

                    elif numero[:1] == '2': 
                        if len(numero) == 9:   
                            if saldo>25:
                                saldo-=25
                                stack.append('T')
                                print('maq: "saldo %s"' % intToStringCoin(saldo))

                            else:    
                                print('maq: "Saldo insuficiente, necessário 25c para realizar a chamada"')
                        else:
                            print('maq: "Número incorreto, disque novamente um número com 9 digitos"')

                    elif numero[:2] == '80':
                        if len(numero) == 9:   
                            if numero[:3] == '800':
                                stack.append('T')
                                print('maq: "saldo %s"' % intToStringCoin(saldo))
                            elif numero[:3] == '808':
                                if saldo>10:
                                    saldo-=10
                                    stack.append('T')
                                    print('maq: "saldo %s"' % intToStringCoin(saldo))
                                else:    
                                    print('maq: "Saldo insuficiente, necessário 10c para realizar a chamada"')
                        else:
                            print('maq: "Número incorreto, disque novamente um número com 9 digitos"')
                    else:
                        saldo-=15
                        print('maq: "saldo %s"' % intToStringCoin(saldo))
        elif linha.strip().upper() == 'POUSAR' or linha.strip().upper() == 'ABORTAR':
            if len(stack)>0 and stack[-1] == 'T' or  stack[-1] == 'MOEDA':
                stack = []
                saldo_string = intToStringCoin(saldo)
                print('maq: "troco= %s; Volte sempre!"' % saldo_string)
            else:
                stack = []
                break
        else:
            print('maq: "Não é possível realizar a chamada"')
            
run()
