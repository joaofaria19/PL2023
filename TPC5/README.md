# PL2023 - TPC5

O trabalho para casa 5, da unidade curricular de Processamento de linguagens consiste na elaboração de uma máquina de estados que modela a interação de um utilizador com um telefone numa cabine pública.

O telefone reage aos comandos seguintes:

- LEVANTAR - levantar o auscultador, marca o início duma interacção;
- POUSAR - pousar o auscultador, no fim da interacção, é indicado o montante a ser devolvido;
- MOEDA <lista de valores> - inserção de moedas (só aceitar moedas válidas, para valores inválidos é gerada uma mensagem de erro): lista de valores válidos = 5c,10c,20c,50c,1e,2e;
- T=numero - disca o número ( o número deve ter 9 dígitos excepto se for iniciado por "00"); as diferentes chamadas deverão ser tratadas da seguinte maneira:
    - para números iniciados por "601" ou "641" a chamada é "bloqueada";
    - para chamadas internacionais (iniciadas por "00") o utilizador tem que ter um saldo igual ou superior a 1,5 euros, caso contrário deverá ser avisado que o saldo é -insuficiente e a máquina volta ao estado anterior; a chamada se for realizada tem um custo de 1,5 euros;
    - para chamadas nacionais (iniciadas por "2") o saldo mínimo e custo de chamada é de 25 cêntimos;
    - para chamadas verdes (iniciadas por "800") o custo é 0;
    - para chamadas azuis (iniciadas por "808") o custo é de 10 cêntimos.
- ABORTAR - interromper a interacção; a máquina devolve as moedas.
