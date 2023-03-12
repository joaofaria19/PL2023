import json
import re

f = open('./csv/dataset5.csv','r')
f_json = open('./json/dataset5.json','w')

lines = f.readlines()

first_line = lines.pop(0)

header = re.split(r'(?<=[a-zA-Z]),(?=[a-zA-Z])',first_line.strip())

bodyExp = re.compile(r'^(?P<numero>\d+),(?P<nome>(\w+\s*)+),(?P<curso>(\w+\s*)+),*(?P<notas>(\d+|,)+)*$',re.UNICODE)

maxMinExp = re.compile(r'^\w+(\{(?P<nota>\d+)\}|\{(?P<ni>\d+),(?P<ns>\d+)\})')

operatorExp = re.compile(r'(::)(?P<operator>\w+)')


dictjson={}
dictjson['alunos'] = []

for line in lines:
    dictaux={}
    match = bodyExp.search(line.strip())
    dictaux[header[0]] = match.group('numero')
    dictaux[header[1]] = match.group('nome')
    dictaux[header[2]] = match.group('curso')

    if len(header)>3:
        match_nota = maxMinExp.search(header[3])
        lista_notas = []
        if match_nota.group('nota'):
            maximo = int(match_nota.group('nota'))
            notas_group = match.group('notas')
            notas = re.split(',',notas_group)
            for i in range(0,maximo):
                lista_notas.append(notas[i])
        else: 
            minimo = int(match_nota.group('ni'))
            maximo = int(match_nota.group('ns'))
            notas_group = match.group('notas')
            notas = re.split(',',notas_group)
            for i in range(0,maximo):
                if(notas[i].isdigit()):
                    lista_notas.append(notas[i])
        dictaux['Notas'] = lista_notas
        
        match_operator = operatorExp.finditer(header[3])
        if match_operator:
            notas_group = match.group('notas')
            notas = re.split(',',notas_group)
            for match in match_operator:
                op = match['operator']
                if op.lower() == 'sum':
                    valor = 0
                    for nota in notas:
                        if nota.isdigit():
                            valor+= int(nota)
                    dictaux['Notas_sum'] = valor
                elif op.lower() == 'media':
                    valor=0
                    for nota in notas:
                        if nota.isdigit():
                            valor+= int(nota)
                    valor /= len(notas)
                    dictaux['Notas_media'] = valor
                elif op.lower() == 'min':
                    dictaux['Notas_media'] = min(notas)
                elif op.lower() == 'max':
                    dictaux['Notas_media'] = max(notas)

    dictjson['alunos'].append(dictaux)


json.dump(dictjson,f_json,indent=4,ensure_ascii=False)