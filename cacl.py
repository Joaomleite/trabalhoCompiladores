import ply.lex as lex
import ply.yacc as yacc
import sys


tokens = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'x',
    'w',
    'y',
    'z',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'X',
    'W',
    'Y',
    'Z',
    'SPACE'
]


t_ignore = r' '

def t_a(t):
    r'01100001'
    t.value = 'a'
    return t

def t_A(t):
    r'01000001'
    t.value = 'A'
    return t

def t_b(t):
    r'01100010'
    t.value = 'b'
    return t

def t_B(t):
    r'01000010'
    t.value = 'B'
    return t

def t_c(t):
    r'01100011'
    t.value = 'c'
    return t

def t_C(t):
    r'01000011'
    t.value = 'C'
    return t

def t_d(t):
    r'01100100'
    t.value = 'd'
    return t

def t_D(t):
    r'01000100'
    t.value = 'D'
    return t

def t_e(t):
    r'01100101'
    t.value = 'e'
    return t

def t_E(t):
    r'01000101'
    t.value = 'E'
    return t

def t_f(t):
    r'01100110'
    t.value = 'f'
    return t

def t_F(t):
    r'01000110'
    t.value = 'F'
    return t

def t_g(t):
    r'01100111'
    t.value = 'g'
    return t

def t_G(t):
    r'01000111'
    t.value = 'G'
    return t

def t_h(t):
    r'01101000'
    t.value = 'h'
    return t

def t_H(t):
    r'01001000'
    t.value = 'H'
    return t

def t_i(t):
    r'01101001'
    t.value = 'i'
    return t

def t_I(t):
    r'01001001'
    t.value = 'I'
    return t

def t_j(t):
    r'01101010'
    t.value = 'j'
    return t

def t_J(t):
    r'01001010'
    t.value = 'J'
    return t

def t_k(t):
    r'01101011'
    t.value = 'k'
    return t

def t_K(t):
    r'01001011'
    t.value = 'K'
    return t

def t_l(t):
    r'01101100'
    t.value = 'l'
    return t

def t_L(t):
    r'01001100'
    t.value = 'L'
    return t

def t_m(t):
    r'01101101'
    t.value = 'm'
    return t

def t_M(t):
    r'01001101'
    t.value = 'M'
    return t

def t_n(t):
    r'01101110'
    t.value = 'n'
    return t

def t_N(t):
    r'01001110'
    t.value = 'N'
    return t

def t_o(t):
    r'01101111'
    t.value = 'o'
    return t

def t_O(t):
    r'01001111'
    t.value = 'O'
    return t

def t_p(t):
    r'01110000'
    t.value = 'p'
    return t

def t_P(t):
    r'01010000'
    t.value = 'P'
    return t

def t_q(t):
    r'01110001'
    t.value = 'q'
    return t

def t_Q(t):
    r'01010001'
    t.value = 'Q'
    return t

def t_r(t):
    r'01110010'
    t.value = 'r'
    return t

def t_R(t):
    r'01010010'
    t.value = 'R'
    return t

def t_s(t):
    r'01110011'
    t.value = 's'
    return t

def t_S(t):
    r'01010011'
    t.value = 'S'
    return t

def t_t(t):
    r'01110100'
    t.value = 't'
    return t

def t_T(t):
    r'01010100'
    t.value = 'T'
    return t

def t_u(t):
    r'01110101'
    t.value = 'u'
    return t

def t_U(t):
    r'01010101'
    t.value = 'U'
    return t

def t_v(t):
    r'01110110'
    t.value = 'v'
    return t

def t_V(t):
    r'01010110'
    t.value = 'V'
    return t

def t_w(t):
    r'01110111'
    t.value = 'w'
    return t

def t_W(t):
    r'01010111'
    t.value = 'W'
    return t

def t_x(t):
    r'01111000'
    t.value = 'x'
    return t

def t_X(t):
    r'01011000'
    t.value = 'X'
    return t

def t_y(t):
    r'01111001'
    t.value = 'y'
    return t

def t_Y(t):
    r'01011001'
    t.value = 'Y'
    return t

def t_z(t):
    r'01111010'
    t.value = 'z'
    return t

def t_Z(t):
    r'01011010'
    t.value = 'Z'
    return t

def t_SPACE(t):
    r'00100000'
    t.value = ' '
    return t

def t_error(t):
    print('Illegal characters!')
    t.lexer.skip(1)

lexer = lex.lex()

def p_expressao(p):
    '''
    expressao : frase 
                | empty
    '''
    if(p[1] is not None):
        print(run(p[1]))

def p_frase(p):
    '''
    frase : palavra SPACE frase 
            | palavra 
    '''
    if(len(p) > 2):
        print(p[1], p[2], p[3])
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_palavra(p):
    '''
    palavra : upperCase palavra 
              | lowerCase palavra 
              | upperCase 
              | lowerCase
    '''

    if(len(p) > 2):
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

def p_upperCase(p):
    '''
    upperCase : A 
                | B 
                | C 
                | D 
                | E 
                | F 
                | G 
                | H 
                | I 
                | J 
                | K 
                | L 
                | M 
                | N 
                | O 
                | P 
                | Q 
                | R 
                | S 
                | T 
                | U 
                | V 
                | X 
                | W 
                | Y 
                | Z 
    '''

    p[0] = p[1]

def p_lowerCase(p):
    '''
    lowerCase : a 
                | b 
                | c 
                | d 
                | e 
                | f 
                | g 
                | h 
                | i 
                | j
                | k 
                | l 
                | m 
                | n 
                | o 
                | p 
                | q 
                | r 
                | s 
                | t 
                | u 
                | v 
                | x 
                | w 
                | y 
                | z 
    '''

    p[0] = p[1]

def p_empty(p):
    '''
    empty :
    '''

    p[0] = None

def p_error(p):
    print('Syntax error found!')



parser = yacc.yacc()

def run(p):
    if type(p) == tuple:
        if(len(p) == 2):
            return f'{run(p[0])}{run(p[1])}'
        if(len(p) == 3):
            return f'{run(p[0])}{run(p[1])}{run(p[2])}'
    else:
        return p

while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    parser.parse(s)
