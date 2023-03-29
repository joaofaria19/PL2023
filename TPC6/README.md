# PL2023 - TPC6

O trabalho para casa 6, da unidade curricular de Processamento de linguagens consiste na elaboração de analisador léxico para uma linguagem de programação previamente fornecida. Usando a biblioteca Ply o analisador léxico deve realizar a devida análise de um ficheiro de texto escrito na linguagem fornecida, e em seguida devolver a lista de tokens para a linguagem de programação.

### Exemplo 1 da linguagem fornecida
{

/* factorial.p
-- 2023-03-20 
-- by jcr
*/

int i;

// Função que calcula o factorial dum número n

function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}

}
### Exemplo 2 da linguagem fornecida

/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/

int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};

// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
