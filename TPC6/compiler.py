import ply.lex as lex
import sys

f = open('file.txt','r')

lines = f.readlines()

states = (
    ('comment', 'exclusive'),
)

tokens = ('LINECOMMENT','OPEN_BLOCKCOMMENT','CLOSE_BLOCKCOMMENT','BLOCKCOMMENT',
          'LPARENT','RPARENT','LBRACKET','RBRACKET','LSQUAREBRACKET','RSQUAREBRACKET',
          'SUM','MINUS','PRODUCT','DIVIDE','EQUAL','EQUALS','GREATER','LESS','GREATEREQUAL',
          'LESSEQUAL', 'NOTEQUALS','NUMBER','ID','NEWLINE','COMMA','SEMICOLON','DOT',
          'FOR','WHILE','FUNCTION','PROGRAM','PRINT','INT','IN','IF','ELSE'
          )


t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LSQUAREBRACKET = r'\['
t_RSQUAREBRACKET = r'\]'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_SUM = r'\+'
t_PRODUCT = r'\*'
t_MINUS = r'-'
t_DIVIDE = r'\/'
t_EQUAL = r'='
t_EQUALS = r'=='
t_NOTEQUALS = r'!='
t_LESS = r'<'
t_GREATER = r'>'
t_LESSEQUAL = r'<='
t_GREATEREQUAL = r'>='
t_COMMA = r','
t_SEMICOLON = r';'
t_DOT = r'\.'
t_FOR = r'(for)(?=\s?\w+)'
t_WHILE = r'(while)(?=\s?\w+)'
t_FUNCTION = r'(function)(?=\s?\w+)'
t_PROGRAM = r'(program)(?=\s?\w+)'
t_PRINT = r'(print)(?=\()'
t_IN = r'(in)(?=\s?\w+)'
t_INT = r'(int)(?=\s?\w+)'
t_IF = r'(if)(?=\s?\w+)'
t_ELSE = r'(else)'
t_LINECOMMENT = r'//[^\n]*'
t_ID = r'[a-zA-Z_]\w*'


def t_OPEN_BLOCKCOMMENT(t):
    r'^(\/\*)'
    t.lexer.begin('comment')
    t.lexer.lineno += t.value.count('\n')
    return t 

def t_comment_CLOSE_BLOCKCOMMENT(t):
    r'(\*\/)$'
    t.lexer.begin('INITIAL')
    t.lexer.lineno += t.value.count('\n')
    return t 

def t_comment_BLOCKCOMMENT(t):
    r'[\w+\.\s\t\?\(\)\[\]\{\}\+\*\/=><#$%",-:]+'
    t.lexer.lineno += t.value.count('\n')
    return t

t_comment_ignore = ' \t'

def t_comment_error(t):
    print(f"Illegal character: '{t.value[0]}', on line: {t.lexer.lineno}")
    t.lexer.skip(1)


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character: '{t.value[0]}', on line: {t.lexer.lineno}")
    t.lexer.skip(1)


lexer = lex.lex()

for line in lines :
    lexer.input(line)
    while True:
        tok = lexer.token()
        if not tok: 
            break
        print(tok)