import re
import json

f = open('processos.txt','r')
lines = f.readlines()

f_json = open('processos.json','w')

exp = re.compile(r'(?P<pasta>\d+)::(?P<data>\d{4}-\d{2}-\d{2})::(?P<nome>(\w+\s*)+)::(?P<pai>(\w+\s*)+)*::(?P<mae>(\w+\s*)+)*(::|::::)(?P<observacao>.+(::))*$')
expObs = re.compile(r'(?P<nome_familia>(\w+\s*)+),(?P<parentesco>(\w+\s*)+).\sProc.(?P<processo>\d+).(::|\s+)')


dictjson = {}
dictjson["processos"] = []

index=0
for line in lines[:20]:
    processo = {}
    match = exp.search(line)
    if match :
        processo['id'] = index
        processo['pasta'] = match.group('pasta')
        processo['data'] = match.group('data')
        processo['nome'] = match.group('nome')
        processo['pai'] = match.group('pai')
        processo['mae'] = match.group('mae')
        index+=1
        
        lista_observacoes = []
        
        bloco_observacao = match.group('observacao')

        if bloco_observacao :
            match_observacao = expObs.finditer(bloco_observacao) 
            for obs in match_observacao:
                observacao = {}
                observacao['nome'] = obs['nome_familia']
                observacao['parentesco'] = obs['parentesco']
                observacao['Processo'] = obs['processo']
                lista_observacoes.append(observacao)
            processo['observacoes'] = lista_observacoes
    dictjson["processos"].append(processo)


json.dump(dictjson,f_json,indent=4)