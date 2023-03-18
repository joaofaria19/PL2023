def funcao(moedas_total):
    f_moeda = int(moedas_total/100)
    s_moeda = moedas_total - 100*f_moeda
    moeda_string = ''
    if f_moeda > 0:
        moeda_string = str(f_moeda)+'e'+str(s_moeda)+'c'
    else:
        moeda_string = str(s_moeda)+'c'

    return moeda_string

print(funcao(445))