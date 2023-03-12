# PL2023 - TPC4

O trabalho para casa 4, da unidade curricular de processamento de linguagens, consiste na criação de um programa em python que implementa um conversor de um ficheiro CSV para formato JSON. Para se poder realizar a conversão pretendida, é importante saber que a primeira linha do CSV dado funciona como cabeçalho que define o que representa cada coluna.

Neste trabalho tivemo em conta que o cabeçalho pode variar das seguintes formas:
- Exemplo dataset1.csv:

Numero,Nome,Curso
3162,Cândido Faísca,Teatro
7777,Cristiano Ronaldo,Desporto
264,Marcelo Sousa,Ciência Política

- Exemplo dataset2.csv:

Número,Nome,Curso,Notas{5},,,,,
3162,Cândido Faísca,Teatro,12,13,14,15,16
7777,Cristiano Ronaldo,Desporto,17,12,20,11,12
264,Marcelo Sousa,Ciência Política,18,19,19,20,18

- Exemplo dataset3.csv:

Número,Nome,Curso,Notas{3,5},,,,,
3162,Cândido Faísca,Teatro,12,13,14,,
7777,Cristiano Ronaldo,Desporto,17,12,20,11,12
264,Marcelo Sousa,Ciência Política,18,19,19,20,

- Exemplo dataset4.csv:

Número,Nome,Curso,Notas{3,5}::sum,,,,,
3162,Cândido Faísca,Teatro,12,13,14,,
7777,Cristiano Ronaldo,Desporto,17,12,20,11,12
264,Marcelo Sousa,Ciência Política,18,19,19,20,

- Exemplo dataset5.csv:

Número,Nome,Curso,Notas{3,5}::sum::media,,,,,
3162,Cândido Faísca,Teatro,12,13,14,,
7777,Cristiano Ronaldo,Desporto,17,12,20,11,12
264,Marcelo Sousa,Ciência Política,18,19,19,20,

Estes são apenas alguns exempos da forma como o cabeçalho do dataset era aceitável, no entanto poderiamos o intervalo de notas, o tipo de operação podia ser de min ou max, e podiamos ter ainda mais operações seguidas no formato (::operação1::operação2::operação3).