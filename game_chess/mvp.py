from game_input import *
from game_mvt import *
from game_fin import *
from board import *
# from game_chess.game_input import *
# from game_chess.game_mvt import *
# from game_chess.game_fin import *
# from game_chess.board import *


dicocolor = {'b': 'blancs', 'n': 'noirs'}


mvt_dico = {'R': mvt_roi, 'D': mvt_dame, 'C': mvt_cavalier,
            'F': mvt_fou, 'T': mvt_tour, 'P': mvt_pion}


def edit_roque(lastmove, bool_roque):
    """Renvoie une copie de bool_roque modifiée en conséquence du lastmove

    Args:
        lastmove (liste de 2 tuples): les coordonnées du dernier coup
        bool_roque (dictionnaire de 6 booléens): si les tours/rois peuvent roquer
    """
    new_bool_roque = {}
    for piece in bool_roque.keys():
        # copie de bool_roque
        new_bool_roque[piece] = bool_roque[piece]
    if (0, 0) in lastmove:
        new_bool_roque['TourGaucheN'] = False
    if (0, 4) in lastmove:
        new_bool_roque['RoiN'] = False
    if (0, 7) in lastmove:
        new_bool_roque['TourDroitN'] = False
    if (7, 0) in lastmove:
        new_bool_roque['TourGaucheB'] = False
    if (7, 4) in lastmove:
        new_bool_roque['RoiB'] = False
    if (7, 7) in lastmove:
        new_bool_roque['TourDroitB'] = False
    return new_bool_roque


def coup_joueur(trait, board, lastmove, bool_roque):
    """Renvoie le plateau après un coup valide du joueur
        et les coordonnées (liste de 2 tuples) de ce coup

    Args:
        trait (string de 1 caractère): la couleur du joueur qui joue
        board (liste de 8 listes de 8 strings): configuration avant le coup
        lastmove (liste de 2 tuples): les coordonnées du dernier coup
        bool_roque (dictionnaire de 6 booléens): si les tours/rois peuvent roquer
    """
    command = read_player_command()
    depart, arrivee = command[0], command[1]
    i1, j1 = depart[0], depart[1]
    if board[i1][j1][1] != trait:
        # s'il y n'y a pas une pièce de la bonne couleur
        print("Il n'y a pas de pièce de votre couleur sur la case de départ...")
        return coup_joueur(trait, board, lastmove, bool_roque)
    pièce = board[i1][j1][0]
    newboard = [[case for case in row] for row in board]
    newboard = mvt_dico[pièce](newboard, depart, arrivee, lastmove, bool_roque)
    if newboard == board:
        # si le plateau reste le même ie si le coup est impossible
        print("La pièce ne peut pas se déplacer ainsi.")
        return coup_joueur(trait, board, lastmove, bool_roque)
    new_bool_roque = edit_roque(command, bool_roque)
    if echec(newboard, command, new_bool_roque)[trait]:
        # si le mouvement met en échec le joueur qui le joue
        print("Ce coup vous met en échec !")
        return coup_joueur(trait, board, lastmove, bool_roque)
    return newboard, command, new_bool_roque


def promotion(board):
    """Demande au joueur de promouvoir son pion s'il atteint la rangée du fond
        et renvoie l'échiquier avec la pièce voulue à la place du pion

    Args:
        board (liste de 8 listes de 8 strings): configuration actuelle
    """
    for j in range(8):
        if board[0][j] == 'Pb':
            # si un pion blanc est dans la rangée du haut
            promo = input("Entrez l'initiale de la promotion (C, F, T ou D) :")
            while promo not in ['C', 'F', 'T', 'D']:
                promo = input(
                    "Non valide. Entrez l'initiale de la promotion (C, F, T ou D) :")
            board[0][j] = promo + 'b'
            # la pièce blanche voulue remplace le pion
        if board[7][j] == 'Pn':
            # si un pion noir est dans la rangée du bas
            promo = input("Entrez l'initiale de la promotion (C, F, T ou D) :")
            while promo not in ['C', 'F', 'T', 'D']:
                promo = input(
                    "Non valide. Entrez l'initiale de la promotion (C, F, T ou D) :")
            board[7][j] = promo + 'n'
            # la pièce noire voulue remplace le pion
    return board


def game_play():
    """Lance le jeu quand elle est appelée
    """
    board = init_board()
    print(display_board(board))
    trait = 'b'  # le trait est d'abord aux blancs
    lastmove = [(0, 0), (0, 0)]
    bool_roque = {"RoiN": True, "RoiB": True, "TourGaucheB": True,
                  "TourGaucheN": True, "TourDroitB": True, "TourDroitN": True}
    gameover = False  # booléen 'si le jeu est terminé'
    while not (gameover):  # boucle d'un tour de jeu
        print('Aux ' + dicocolor[trait] + ' de jouer.')
        newboard, lastmove, bool_roque = coup_joueur(
            trait, board, lastmove, bool_roque)
        board = [[case for case in row] for row in newboard]
        board = promotion(board)
        print(display_board(board))
        trait = adversaire(trait)  # le trait sera au joueur adverse
        if echec(board, lastmove, bool_roque)[trait]:
            # si le joueur adverse est en échec
            print('Les ' + dicocolor[trait] + ' sont en échec.')
            if echec_et_mat(board, lastmove, bool_roque)[0]:
                # si le joueur adverse est en échec et mat
                print('Échec et mat !')
                gameover = True
        if pat(board, trait, lastmove, bool_roque):  # s'il y a pat
            print('Il y a pat...')
            gameover = True
    print('Fin de la partie')


game_play()
