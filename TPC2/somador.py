import sys

def list_to_digit(lista):
    l = len(lista)
    n=1
    num=0
    while l>0:
        num+=int(lista[l-1])*n
        n *= 10
        l-=1
    return num

def extrair(texto):
    palavras = []
    i = 0
    while i < len(texto):
        if texto[i] == '=':
            palavras.append('=')
            i += 1
        elif texto[i] == 'o' and texto[i+1] == 'n':
            palavras.append('on')
            i += 2
        elif texto[i] == 'o' and texto[i+1] == 'f' and texto[i+2] == 'f':
            palavras.append('off')
            i += 3
        elif texto[i].isdigit():
            inicio = i
            while i < len(texto) and texto[i].isdigit():
                i += 1
            palavras.append(list_to_digit(texto[inicio:i]))
        else:    
            i += 1
    print(palavras)
    return palavras



def run(texto):
    on_stack = []
    soma = 0
    for word in texto:
        if word == 'on':
            on_stack.append('on')
        elif word =='off':
            on_stack.pop()
        elif word == '=':
            print(">> "+ str(soma))
        elif len(on_stack) > 0:
            soma += (word)

def main():
    lines = []
    print("<< Insira o texto em seguida e prima 'Ctrl+D' para ver o total >>\n")
    for linha in sys.stdin:
        lines.extend(linha)
    words = extrair(lines)
    run(words)

if __name__ == "__main__":
    main()