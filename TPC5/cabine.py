import re
import ply.lex as lex
import sys

# Coins list
moedas_validas = ['5c','10c','20c','50c','1e','2e']

saldo = 0

stack  = []

moedas_exp = re.compile(r'^MOEDA\s+(?P<moedas>(\d+(c|e)(,\s*|(?=;)|(?=.)))*)')

numero_exp = re.compile(r'^T=(?P<numero>\d{9,})$')

def intToStringCoin(moeda):
    f_moeda = int(moeda/100)
    s_moeda = moeda - 100*f_moeda
    moeda_string = ''
    if f_moeda > 0:
        moeda_string = str(f_moeda)+'e'+str(s_moeda)+'c'
    else:
        moeda_string = str(s_moeda)+'c'
    return moeda_string

def moeda_handler(lista_moedas):
    moedas_total = 0
    moedas_invalidas = []
    for moeda in lista_moedas:
        if moeda not in moedas_validas:
            moedas_invalidas.append(moeda)
        else:
            if moeda == '1e' or moeda == '2e':
                moeda = moeda[:-1]
                moeda*100
            else: 
                moeda = moeda[:-1]
            moedas_total += int(moeda)
    
    moeda_invalidas_string=''
    if len(moedas_invalidas) > 0:

        for moeda in moedas_invalidas:
            moeda_invalidas_string += moeda +", "

    return (moedas_total,moeda_invalidas_string)


for linha in sys.stdin:
    if linha.strip().upper() == 'LEVANTAR' and len(stack) == 0:
        print("maq: 'Introduza moedas'")
        stack.append(linha.strip())
        
    elif stack[-1].upper() == 'LEVANTAR'and moedas_exp.match(linha.strip()):
        moedas = moedas_exp.match(linha).group('moedas').split(',')
        (total, invalidas) = moeda_handler(moedas)
        total_string = intToStringCoin(total)
        saldo += total
        if len(invalidas) == 0:
            print('maq: "saldo = '+ total_string +'"')
        else:
            print('maq: "'+ str(invalidas) +' moeda inválida, saldo = '+total_string+'"')
        stack.append('MOEDA')

    elif stack[-1] == 'MOEDA' and numero_exp.match(linha.strip()):
        numero = numero_exp.match(linha).group('numero')
        if numero[:3] == '601' or numero[3:] == '641':
            print('maq: "Esse número não é permitido neste telefone. Queira disque um novo número"')
        elif numero[:2] == '00':
            if saldo>150:
                saldo-=150
                stack.append('T')
            else:    
                print('maq: "Saldo insuficiente, necessário 1e50c para realizar a chamada"')

        elif numero[:1] == '2':
            if saldo>25:
                saldo-=25
                stack.append('T')
            else:    
                print('maq: "Saldo insuficiente, necessário 25c para realizar a chamada"')
        elif numero[:2] == '80':
            if numero[:3] == '800':
                stack.append('T')
            elif numero[:3] == '808':
                if saldo>10:
                    saldo-=10
                    stack.append('T')
                else:    
                    print('maq: "Saldo insuficiente, necessário 10c para realizar a chamada"')

    elif linha.strip().upper() == 'POUSAR' or linha.strip().upper() == 'ABORTAR':
        if stack[-1] == 'T' or  stack[-1] == 'MOEDA':
            saldo_string = intToStringCoin(saldo)
            print('maq: "troco= %s; Volte sempre!"' % saldo_string)
            pass
        else:
            break
    else:
        print('maq: "Não é possível realizar a chamada"')
    print(stack)
        

