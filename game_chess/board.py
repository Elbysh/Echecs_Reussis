def init_board():
    """Initialisation de l'échiquier, 
    renvoie une liste de listes de strings d'un plateau d'échec en début de partie"""
    board = [
        ['Tn', 'Cn', 'Fn', 'Dn', 'Rn', 'Fn', 'Cn', 'Tn'],
        ['Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn'],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb'],
        ['Tb', 'Cb', 'Fb', 'Db', 'Rb', 'Fb', 'Cb', 'Tb']
    ]
    return board


def display_board(board):
    """Affiche l'échiquier, en prenant en parametre une liste de listes de strings"""
    a = ' ====' * 8
    res = '  '
    abssices = ''
    for k in range(8):  # 8 = taille de l'échiquier
        res += a
        res += '\n'
        res += str(8-k)
        res += ' |'
        for l in range(8):
            res += ' ' + str(D[board[k][l]]) + ' |'
        res += '\n  '
    res += a
    res += '\n    a    b    c    d    e    f    g    h'
    return res  # + '\n   '


# Dictionnaire pour l'affichage
D = {'Pn': '♙ ', 'Tn': '♖ ', 'Cn': '♘ ', 'Fn': '♗ ', 'Dn': '♕ ', 'Rn': '♔ ',
     'Pb': '♟ ', 'Tb': '♜ ', 'Cb': '♞ ', 'Fb': '♝ ', 'Db': '♛ ', 'Rb': '♚ ', '  ': '  '}


# print(display_board(init_board()))
