import ply.lex as lex

tokens = ('LEVANTAR','POUSAR','ABORTAR','TELEFONE','MOEDAS')

t_LEVANTAR = r'LEVANTAR'
t_POUSAR = r'POUSAR'
t_ABORTAR = r'ABORTAR'

def t_TELEFONE(t):
    r'^T=\s*\d{9,}$'
    return t

def t_MOEDAS(t):
    r'^MOEDA\s+(\d+(c|e)(,\s*|;|.)*)*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore ='\t '

def t_error(t):
    # print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()