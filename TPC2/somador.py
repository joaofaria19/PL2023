import sys

def list_words(lines):
    palavras=[]
    soma_flag=False
    for line in lines:
        splited = line.strip().split()
        palavras.extend(splited)
    return palavras

def soma_array_numbers(array):
    total = 0
    for i in array:
        total += float(i)
    return total

def run(words):
    soma_flag = False
    numbers=[]

    for word in words:
        if(soma_flag==True):
            if(word.isdigit()):
                numbers.append(word)
        if('=' in word) :
            total = soma_array_numbers(numbers)
            print("\n(TOTAL): "+ str(total))
        if("on" in word.lower()):
            soma_flag=True
        elif("off" in word.lower()):
            soma_flag=False
    

def main():
    lines = []
    print("<< Insira o texto em seguida e prima 'Ctrl+D' para ver o total >>\n")
    for linha in sys.stdin:
        lines.append(linha)
    words = list_words(lines)
    run(words)
    
if __name__ == "__main__":
    main()