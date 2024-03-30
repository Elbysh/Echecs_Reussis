from game_chess.game_fin import *
lastmove = [(0, 0), (1, 0)]
bool_roque = {"RoiN": True, "RoiB": True, "TourGaucheB": True,
              "TourGaucheN": True, "TourDroitB": True, "TourDroitN": True, }


def test_adversaire():
    assert adversaire('b') == 'n' and adversaire('n') == 'b'


def test_echec():
    board = [['Tn', 'Cn', 'Fn', 'Dn', 'Rn', 'Fn', 'Cn', 'Tn'],
             ['Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn'],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pn', 'Pb', 'Pb'],
             ['Tb', 'Cb', 'Fb', 'Db', 'Rb', 'Fb', 'Cb', 'Tb']]
    dico_echec = echec(board, lastmove, bool_roque)
    assert dico_echec['b'] and not dico_echec['n']
    board = [['Tn', 'Cn', 'Fn', 'Dn', 'Rn', 'Fn', 'Cn', 'Tn'],
             ['Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn'],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb'],
             ['Tb', 'Cb', 'Fb', 'Db', 'Rb', 'Fb', 'Cb', 'Tb']]
    dico_echec = echec(board, lastmove, bool_roque)
    assert not dico_echec['b'] and not dico_echec['n']
    board = [['Tn', 'Cn', 'Fn', 'Dn', 'Rn', 'Fn', 'Cn', 'Tn'],
             ['Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn'],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb'],
             ['Tb', 'Cb', 'Fb', 'Db', 'Rn', 'Fb', 'Cb', 'Tb']]
    dico_echec = echec(board, lastmove, bool_roque)
    assert not dico_echec['b'] and dico_echec['n']


test_echec()


def test_rois():
    board = [['Tn', 'Cn', 'Fn', 'Dn', 'Rn', 'Fn', 'Cn', 'Tn'],
             ['Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn'],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb'],
             ['Tb', 'Cb', 'Fb', 'Db', 'Rb', 'Fb', 'Cb', 'Tb']]

    assert (rois(board)['b'] == (7, 4) and rois(board)['n'] == (0, 4))

    board = [['Tn', 'Cn', 'Fn', 'Dn', '  ', 'Fn', 'Cn', 'Tn'],
             ['Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn'],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', 'Rn', 'Rb', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb'],
             ['Tb', 'Cb', 'Fb', 'Db', '  ', 'Fb', 'Cb', 'Tb']]

    assert (rois(board)['b'] == (3, 3) and rois(board)['n'] == (3, 2))


test_rois()


def test_echec_et_mat():
    board = [['Tn', 'Cn', 'Fn', 'Dn', 'Rn', 'Fn', 'Cn', 'Tn'],
             ['Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn'],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pn', 'Pb', 'Pb'],
             ['Tb', 'Cb', 'Fb', 'Db', 'Rb', 'Fb', 'Cb', 'Tb']]

    assert (not echec_et_mat(board, lastmove, bool_roque)[
            0] and echec_et_mat(board, lastmove, bool_roque)[1] == '')

    board = [['Tn', 'Cn', 'Fn', 'Dn', 'Rn', 'Fn', 'Cn', 'Tn'],
             ['Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn'],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pn', 'Pb', 'Pb'],
             ['Tb', 'Cb', 'Fb', 'Db', 'Rb', 'Fb', 'Cb', 'Tb']]

    assert (not echec_et_mat(board, lastmove, bool_roque)[
            0] and echec_et_mat(board, lastmove, bool_roque)[1] == '')

    board = [['Tn', 'Cn', 'Fn', 'Dn', 'Rn', 'Fn', 'Cn', 'Tn'],
             ['Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn'],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', 'Pn', '  ', '  ', '  '],
             ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb'],
             ['Tb', 'Cb', 'Fb', 'Db', 'Rn', 'Fb', 'Cb', 'Tb']]

    assert (not echec_et_mat(board, lastmove, bool_roque)[
            0] and echec_et_mat(board, lastmove, bool_roque)[1] == '')

    board = [['Tn', 'Cn', 'Fn', 'Dn', 'Rn', 'Fn', 'Cn', 'Tn'],
             ['Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn'],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', 'Pn', '  ', 'Rn', '  '],
             ['  ', '  ', '  ', '  ', '  ', 'Pb', '  ', '  '],
             ['Pb', 'Pb', 'Pb', '  ', '  ', '  ', 'Pb', 'Pb'],
             ['Tb', 'Cb', 'Fb', '  ', '  ', '  ', 'Cb', 'Tb']]

    # assert (not echec_et_mat(board, lastmove, bool_roque)[
    #         0] and echec_et_mat(board, lastmove, bool_roque)[1] == '')

    board = [['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['Fn', 'Fn', 'Fn', 'Fn', 'Fn', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', 'Rb', '  ', '  ']]
    assert (echec_et_mat(board, lastmove, bool_roque)[
            0] and echec_et_mat(board, lastmove, bool_roque)[1] == 'b')

    board = [['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['Tn', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['Dn', '  ', '  ', '  ', '  ', 'Rb', '  ', '  ']]
    assert (echec_et_mat(board, lastmove, bool_roque)[
            0] and echec_et_mat(board, lastmove, bool_roque)[1] == 'b')

    board = [['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', 'Fb', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['Tn', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['Dn', '  ', '  ', '  ', '  ', 'Rb', '  ', '  ']]
    assert (not echec_et_mat(board, lastmove, bool_roque)[0] and echec_et_mat(
        board, lastmove, bool_roque)[1] == '')  # le fou qui carry


test_echec_et_mat()


def test_pat():
    board = [['Tn', 'Cn', 'Fn', 'Dn', 'Rn', 'Fn', 'Cn', 'Tn'],
             ['Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn', 'Pn'],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pn', 'Pb', 'Pb'],
             ['Tb', 'Cb', 'Fb', 'Db', 'Rb', 'Fb', 'Cb', 'Tb']]
    assert not pat(board, 'b', lastmove, bool_roque)
    board = [['  ', '  ', '  ', '  ', '  ', '  ', '  ', 'Rn'],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', 'Pn', '  ', '  ', '  ', '  ', 'Db', '  '],
             ['Pn', 'Pb', '  ', '  ', '  ', '  ', '  ', '  '],
             ['Pb', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', 'Rb', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']]
    assert pat(board, 'n', lastmove, bool_roque)
    board = [['  ', '  ', '  ', '  ', '  ', '  ', '  ', 'Rn'],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', 'Pn', '  ', '  ', '  ', '  ', 'Db', '  '],
             ['Pn', 'Pb', '  ', '  ', 'Pn', '  ', '  ', '  '],
             ['Pb', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', 'Rb', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']]
    assert not pat(board, 'n', lastmove, bool_roque)
    board = [['  ', '  ', '  ', '  ', '  ', '  ', '  ', 'Rb'],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', 'Pn', '  ', '  ', '  ', '  ', 'Dn', 'Rn'],
             ['Pn', 'Pb', '  ', '  ', '  ', '  ', '  ', '  '],
             ['Pb', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']]
    assert pat(board, 'b', lastmove, bool_roque)
    board = [['  ', '  ', '  ', '  ', '  ', '  ', '  ', 'Rn'],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', 'Db', 'Rb'],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']]
    assert pat(board, 'n', lastmove, bool_roque)


test_pat()
