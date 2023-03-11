import json
import re

f = open('./csv/dataset2.csv','r')
f_json = open('./json/dataset2.json','w')
lines = f.readlines()

#dataset1

first_line = lines.pop(0)

headExp = re.compile(r'^(?P<primeira>\w+),(?P<segunda>\w+),(?P<terceira>\w+)(,)*(?P<quarta>\w+[\{\d+\}|\{\d+,\d+\}])*(::)*(?P<operator>\w+)*(?P<n_notas>,+)*$')
# notasExp = re.compile(r'(?P<quarta>\w+[{\d+}|{\d+,\d+}])*(::)*(?P<operator>\w+)*(,+)')
bodyExp = re.compile(r'^(?P<numero>\d+),(?P<nome>(\w+\s*)+),(?P<curso>(\w+\s*)+),*(?P<notas>(\d+|,)+)*$')

headmatch = headExp.search(first_line)
dictjson={}
dictjson['alunos'] = []
for line in lines:
    dictaux={}
    match = bodyExp.search(line.strip())
    dictaux[headmatch.group('primeira')] = match.group('numero')
    dictaux[headmatch.group('segunda')] = match.group('nome')
    dictaux[headmatch.group('terceira')] = match.group('curso')
    dictjson['alunos'].append(dictaux)

    if len(match.groups())>3:
        max_notas = len(headmatch.group('n_notas'))
        # notas = len(match.group('notas'))



    #dictjson[headmatch.group('primeira')] = match.group('notas')
json.dump(dictjson,f_json,indent=4,ensure_ascii=False)