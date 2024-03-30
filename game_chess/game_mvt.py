import tkinter as tk


def mvt_cavalier_poss(echiquier, depart, arrivee, lastmove, bool_roque):
    """Indique si le mouvement du cavalier est possible

    Args:
        echiquier (liste de listes de strings): configuration avant mvt
        depart (tuple de taille 2): les coordonnées de la pièce à déplacer
        arrivee (tuple de taille 2): les coordonnées de la case d'arrivée
        lastmove (liste de 2 tuples): les coordonnées du dernier coup
        bool_roque (dictionnaire de 6 booléens): si les tours/rois peuvent roquer

    Returns:
        booléen: possibilité ou non de mouvement
    """
    x_depart, y_depart = depart[0], depart[1]
    x_arrivee, y_arrivee = arrivee[0], arrivee[1]
    ecarts = [abs(x_depart - x_arrivee), abs(y_depart - y_arrivee)]
    if ecarts == [2, 1] or ecarts == [1, 2]:
        # si le déplacement est bien en L
        if echiquier[x_arrivee][y_arrivee] != '  ':
            if echiquier[x_depart][y_depart][1] != echiquier[x_arrivee][y_arrivee][1]:
                # s'il n'y a pas de pièce de la même couleur sur la case d'arrivée
                return True
        else:
            return True
    return False


def mvt_cavalier(echiquier, depart, arrivee, lastmove, bool_roque):
    """effectue le mouvement du cavalier, s'il est possible

    Args:
        echiquier (liste de listes de strings): configuration avant mvt
        depart (tuple de taille 2): les coordonnées de la pièce à déplacer
        arrivee (tuple de taille 2): les coordonnées de la case d'arrivée
        lastmove (liste de 2 tuples): les coordonnées du dernier coup
        bool_roque (dictionnaire de 6 booléens): si les tours/rois peuvent roquer

    Returns:
        echiquier (liste de listes de strings): grille de jeu après le mouvement
    """
    if mvt_cavalier_poss(echiquier, depart, arrivee, lastmove, bool_roque):
        # si le déplacement est valide
        x_depart, y_depart = depart[0], depart[1]
        x_arrivee, y_arrivee = arrivee[0], arrivee[1]
        # le cavalier remplace la case d'arrivée
        echiquier[x_arrivee][y_arrivee] = echiquier[x_depart][y_depart]
        echiquier[x_depart][y_depart] = '  '  # la case de départ est vide
    return echiquier


def mvt_roi_poss(echiquier, depart, arrivee, lastmove, bool_roque):
    """Renvoie un booléen selon si le mouvement de la pièce
        de la case de départ jusqu'à la case d'arrivée est possible

    Args:
        echiquier (liste de listes de strings): configuration avant mvt
        depart (tuple de taille 2): les coordonnées de la pièce à déplacer
        arrivee (tuple de taille 2): les coordonnées de la case d'arrivée
        lastmove (liste de 2 tuples): les coordonnées du dernier coup
        bool_roque (dictionnaire de 6 booléens): si les tours/rois peuvent roquer
    """
    x_depart, y_depart = depart[0], depart[1]
    x_arrivee, y_arrivee = arrivee[0], arrivee[1]
    ecarts = [abs(x_depart - x_arrivee), abs(y_depart - y_arrivee)]
    if ecarts in [[1, 1], [1, 0], [0, 1]]:
        # si le déplacement est bien de 1 case
        if echiquier[x_arrivee][y_arrivee] != '  ':
            if echiquier[x_arrivee][y_arrivee][1] != echiquier[x_depart][y_depart][1]:
                # s'il n'y a pas de pièce de la même couleur sur la case d'arrivée
                return True
        else:
            return True
    # grand roque chez le roi blanc
    elif depart == (7, 4) and arrivee == (7, 2) and bool_roque["RoiB"] and bool_roque["TourGaucheB"]:
        # si toutes les cases entre le roi et la tour sont vides
        if echiquier[7][2] == '  ' and echiquier[7][3] == '  ':
            for i in range(0, 8):  # si le roi risque d'être en échec
                for j in range(0, 8):
                    if echiquier[i][j][1] == 'n':
                        for k in [2, 3, 4]:
                            if mvt_dico_poss[echiquier[i][j][0]](echiquier, (i, j), (7, k), lastmove, bool_roque):
                                return False
            return True
        else:
            return False
    # petit roque chez le blanc
    elif depart == (7, 4) and arrivee == (7, 6) and bool_roque["RoiB"] and bool_roque["TourDroitB"]:
        # si toutes les cases entre le roi et la tour sont vides
        if echiquier[7][5] == '  ' and echiquier[7][6] == '  ':
            for i in range(0, 8):  # si le roi risque d'être en échec
                for j in range(0, 8):
                    if echiquier[i][j][1] == 'n':
                        for k in [4, 5, 6]:
                            if mvt_dico_poss[echiquier[i][j][0]](echiquier, (i, j), (7, k), lastmove, bool_roque):
                                return False
            return True
        else:
            return False
    # grand roque chez le noir
    elif depart == (0, 4) and arrivee == (0, 2) and bool_roque["RoiN"] and bool_roque["TourGaucheN"]:
        # si toutes les cases entre le roi et la tour sont vides
        if echiquier[0][3] == '  ' and echiquier[0][2] == '  ':
            for i in range(0, 8):  # si le roi risque d'être en échec
                for j in range(0, 8):
                    if echiquier[i][j][1] == 'b':
                        for k in [2, 3, 4]:
                            if mvt_dico_poss[echiquier[i][j][0]](echiquier, (i, j), (0, k), lastmove, bool_roque):
                                return False
            return True
        else:
            return False
    # petit roque chez le roi noir
    elif depart == (0, 4) and arrivee == (0, 6) and bool_roque["RoiN"] and bool_roque["TourDroitN"]:
        # si toutes les cases entre le roi et la tour sont vides
        if echiquier[0][5] == '  ' and echiquier[0][6] == '  ':
            for i in range(0, 8):  # si le roi risque d'être en échec
                for j in range(0, 8):
                    if echiquier[i][j][1] == 'b':
                        for k in [4, 5, 6]:
                            if mvt_dico_poss[echiquier[i][j][0]](echiquier, (i, j), (0, k), lastmove, bool_roque):
                                return False
            return True
        else:
            return False
    else:
        return False


def mvt_roi(echiquier, depart, arrivee, lastmove, bool_roque):
    """Renvoie le plateau une fois la pièce déplacée du départ à l'arrivée
        (renvoie le plateau en argument si le mouvement est invalide)

    Args:
        echiquier (liste de listes de strings): configuration avant mvt
        depart (tuple de taille 2): les coordonnées de la pièce à déplacer
        arrivee (tuple de taille 2): les coordonnées de la case d'arrivée
        lastmove (liste de 2 tuples): les coordonnées du dernier coup
        bool_roque (dictionnaire de 6 booléens): si les tours/rois peuvent roquer
    """
    x_depart, y_depart = depart[0], depart[1]
    x_arrivee, y_arrivee = arrivee[0], arrivee[1]
    if mvt_roi_poss(echiquier, depart, arrivee, lastmove, bool_roque):
        # si le déplacement est valide
        if depart == (7, 4) and arrivee == (7, 2):  # grand roque blanc
            echiquier[x_arrivee][y_arrivee] = echiquier[x_depart][y_depart]
            echiquier[7][0], echiquier[7][3] = '  ', echiquier[7][0]
        elif depart == (7, 4) and arrivee == (7, 6):  # petit roque blanc
            echiquier[x_arrivee][y_arrivee] = echiquier[x_depart][y_depart]
            echiquier[7][7], echiquier[7][5] = '  ', echiquier[7][7]
        elif depart == (0, 4) and arrivee == (0, 2):  # grand roque noir
            echiquier[x_arrivee][y_arrivee] = echiquier[x_depart][y_depart]
            echiquier[0][0], echiquier[0][3] = '  ', echiquier[0][0]
        elif depart == (0, 4) and arrivee == (0, 6):  # petit roque noir
            echiquier[x_arrivee][y_arrivee] = echiquier[x_depart][y_depart]
            echiquier[0][7], echiquier[0][5] = '  ', echiquier[0][7]
        else:
            echiquier[x_arrivee][y_arrivee] = echiquier[x_depart][y_depart]
        echiquier[x_depart][y_depart] = '  '  # la case de départ est vide
    return echiquier


def sign(number):
    """donne le signe d'un nombre

    Args:
        number (flottant): nombre entré

    Returns:
        (int): 1, -1 ou 0 en fonction du signe
    """
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0


def mvt_tour(grille, depart, arrivee, lastmove, bool_roque):
    """effectue le mouvement de la tour, s'il est possible

    Args:
        grille (liste de listes de strings): configuration avant mvt
        depart (tuple de taille 2): les coordonnées de la pièce à déplacer
        arrivee (tuple de taille 2): les coordonnées de la case d'arrivée
        lastmove (liste de 2 tuples): les coordonnées du dernier coup
        bool_roque (dictionnaire de 6 booléens): si les tours/rois peuvent roquer

    Returns:
        echiquier (liste de listes de strings): grille de jeu après le mouvement
    """
    if mvt_tour_poss(grille, depart, arrivee, lastmove, bool_roque):
        # si le déplacement est valide
        # la tour remplace la case d'arrivée et la case de départ devient vide
        grille[depart[0]][depart[1]], grille[arrivee[0]
                                             ][arrivee[1]] = '  ', grille[depart[0]][depart[1]]
        return grille
    else:
        return grille


def mvt_tour_poss(grille, depart, arrivee, lastmove, bool_roque):
    """Indique si le mouvement de la tour est possible

    Args:
        grille (liste de listes de strings): configuration avant mvt
        depart (tuple de taille 2): les coordonnées de la pièce à déplacer
        arrivee (tuple de taille 2): les coordonnées de la case d'arrivée
        lastmove (liste de 2 tuples): les coordonnées du dernier coup
        bool_roque (dictionnaire de 6 booléens): si les tours/rois peuvent roquer

    Returns:
        booléen: possibilité ou non de mouvement
    """
    x_depart, y_depart = depart[0], depart[1]
    x_arrivee, y_arrivee = arrivee[0], arrivee[1]
    if x_depart == x_arrivee and y_depart != y_arrivee:
        # si seule la colonne change
        for i in range(1, abs(y_depart - y_arrivee)):
            if grille[x_depart][min(y_depart, y_arrivee) + i] != '  ':
                # si une case sur le chemin n'est pas vide
                return False
        if grille[x_arrivee][y_arrivee] == '  ' or grille[x_arrivee][y_arrivee][1] != grille[x_depart][y_depart][1]:
            # s'il n'y a pas de pièce de la même couleur sur la case d'arrivée
            return True
        else:
            return False
    elif x_depart != x_arrivee and y_depart == y_arrivee:
        # si seule la ligne change
        for i in range(1, abs(x_depart - x_arrivee)):
            if grille[min(x_depart, x_arrivee) + i][y_depart] != '  ':
                # si une case sur le chemin n'est pas vide
                return False
        if grille[x_arrivee][y_arrivee] == '  ' or grille[x_arrivee][y_arrivee][1] != grille[x_depart][y_depart][1]:
            # s'il n'y a pas de pièce de la même couleur sur la case d'arrivée
            return True
        else:
            return False
    else:
        return False


def mvt_fou(grille, depart, arrivee, lastmove, bool_roque):
    """effectue le mouvement du fou, s'il est possible

    Args:
        grille (liste de listes de strings): configuration avant mvt
        depart (tuple de taille 2): les coordonnées de la pièce à déplacer
        arrivee (tuple de taille 2): les coordonnées de la case d'arrivée
        lastmove (liste de 2 tuples): les coordonnées du dernier coup
        bool_roque (dictionnaire de 6 booléens): si les tours/rois peuvent roquer

    Returns:
        echiquier (liste de listes de strings): grille de jeu après le mouvement
    """

    if mvt_fou_poss(grille, depart, arrivee, lastmove, bool_roque):
        # si le déplacement est valide
        # le fou remplace la case d'arrivée et la case de départ devient vide
        grille[depart[0]][depart[1]], grille[arrivee[0]
                                             ][arrivee[1]] = '  ', grille[depart[0]][depart[1]]
        return grille
    else:
        return grille


def mvt_fou_poss(grille, depart, arrivee, lastmove, bool_roque):
    """Indique si le mouvement du fou est possible

    Args:
        grille (liste de listes de strings): configuration avant mvt
        depart (tuple de taille 2): les coordonnées de la pièce à déplacer
        arrivee (tuple de taille 2): les coordonnées de la case d'arrivée
        lastmove (liste de 2 tuples): les coordonnées du dernier coup
        bool_roque (dictionnaire de 6 booléens): si les tours/rois peuvent roquer

    Returns:
        booléen: possibilité ou non de mouvement
    """
    x_depart, y_depart = depart[0], depart[1]
    x_arrivee, y_arrivee = arrivee[0], arrivee[1]
    if abs(x_depart - x_arrivee) == abs(y_depart - y_arrivee):
        # si le déplacement est bien en diagoale
        for i in range(1, abs(x_depart - x_arrivee)):
            if grille[x_depart + sign(x_arrivee - x_depart) * i][y_depart + sign(y_arrivee - y_depart) * i] != '  ':
                # si une case sur le chemin n'est pas vide
                return False
        if grille[x_arrivee][y_arrivee] == '  ' or grille[x_arrivee][y_arrivee][1] != grille[x_depart][y_depart][1]:
            # s'il n'y a pas de pièce de la même couleur sur la case d'arrivée
            return True
        else:
            return False
    else:
        return False


def mvt_dame(grille, depart, arrivee, lastmove, bool_roque):
    """effectue le mouvement de la dame, s'il est possible

    Args:
        grille (liste de listes de strings): configuration avant mvt
        depart (tuple de taille 2): les coordonnées de la pièce à déplacer
        arrivee (tuple de taille 2): les coordonnées de la case d'arrivée
        lastmove (liste de 2 tuples): les coordonnées du dernier coup
        bool_roque (dictionnaire de 6 booléens): si les tours/rois peuvent roquer

    Returns:
        echiquier (liste de listes de strings): grille de jeu après le mouvement
    """
    if mvt_dame_poss(grille, depart, arrivee, lastmove, bool_roque):
        # si le déplacement est valide
        # la dame remplace la case d'arrivée et la case d'arrivée devient vide
        grille[depart[0]][depart[1]], grille[arrivee[0]
                                             ][arrivee[1]] = '  ', grille[depart[0]][depart[1]]
        return grille
    else:
        return grille


def mvt_dame_poss(grille, depart, arrivee, lastmove, bool_roque):
    """Indique si le mouvement de la dame est possible

    Args:
        grille (liste de listes de strings): configuration avant mvt
        depart (tuple de taille 2): les coordonnées de la pièce à déplacer
        arrivee (tuple de taille 2): les coordonnées de la case d'arrivée
        lastmove (liste de 2 tuples): les coordonnées du dernier coup
        bool_roque (dictionnaire de 6 booléens): si les tours/rois peuvent roquer

    Returns:
        booléen: possibilité ou non de mouvement
    """

    x_depart, y_depart = depart[0], depart[1]
    x_arrivee, y_arrivee = arrivee[0], arrivee[1]
    if x_depart == x_arrivee and y_depart != y_arrivee:
        # si le déplacement est en ligne droite sur une même ligne
        for i in range(1, abs(y_depart - y_arrivee)):
            if grille[x_depart][min(y_depart, y_arrivee) + i] != '  ':
                return False
        if grille[x_arrivee][y_arrivee] == '  ' or grille[x_arrivee][y_arrivee][1] != grille[x_depart][y_depart][1]:
            return True
        else:
            return False
    elif x_depart != x_arrivee and y_depart == y_arrivee:
        # si le déplacement est en ligne droite sur une même colonne
        for i in range(1, abs(x_depart - x_arrivee)):
            if grille[min(x_depart, x_arrivee) + i][y_depart] != '  ':
                return False
        if grille[x_arrivee][y_arrivee] == '  ' or grille[x_arrivee][y_arrivee][1] != grille[x_depart][y_depart][1]:
            return True
        else:
            return False
    elif abs(x_depart - x_arrivee) == abs(y_depart - y_arrivee):
        # si le déplacement est en diagonale
        for i in range(1, abs(x_depart - x_arrivee)):
            if grille[x_depart + sign(x_arrivee - x_depart) * i][y_depart + sign(y_arrivee - y_depart) * i] != '  ':
                return False
        if grille[x_arrivee][y_arrivee] == '  ' or grille[x_arrivee][y_arrivee][1] != grille[x_depart][y_depart][1]:
            return True
        else:
            return False
    else:
        return False


# le trait et la nature de la pièce sont vérifiée/filtrée en amont
# les cases sont forcément différentes et sur le plateau
# pas de prise en passant (pour l'instant)


def mvt_pion_poss(board, depart, arriv, lastmove, bool_roque):
    """Renvoie un booléen selon si le mouvement de la pièce
        de la case de départ jusqu'à la case d'arrivée est possible

    Args:
        board (liste de listes de strings): configuration avant mvt
        depart (tuple de taille 2): les coordonnées de la pièce à déplacer
        arriv (tuple de taille 2): les coordonnées de la case d'arrivée
        lastmove (liste de 2 tuples): les coordonnées du dernier coup
        bool_roque (dictionnaire de 6 booléens): si les tours/rois peuvent roquer
    """
    i1, j1, i2, j2 = depart[0], depart[1], arriv[0], arriv[1]
    color1, color2 = (board[i1][j1])[1], (board[i2][j2])[1]
    if color1 == 'b':  # si c'est un pion blanc
        if i2 == i1 - 1 and j2 == j1 and board[i2][j2] == '  ':
            # montée de 1 vers case vide
            return True
        elif i1 == 6 and i2 == i1 - 2 and j2 == j1 and board[i1-1][j2] == '  ' and board[i2][j2] == '  ':
            # montée de 2 vers case vide depuis rangée initiale
            return True
        elif i2 == i1 - 1 and (j2 == j1 - 1 or j2 == j1 + 1):
            if color2 == 'n':
                # prise d'une pièce noire
                return True
            if i1 == 3 and (lastmove[0][0], lastmove[0][1], lastmove[1][0]) == (1, j2, 3) and board[3][j2] == 'Pn':
                # prise en passant
                return True
        return False
    if color1 == 'n':  # si c'est un pion noir
        if i2 == i1 + 1 and j2 == j1 and board[i2][j2] == '  ':
            # descente de 1 vers case vide
            return True
        elif i1 == 1 and i2 == i1 + 2 and j2 == j1 and board[i1+1][j2] == '  ' and board[i2][j2] == '  ':
            # descente de 2 vers case vide depuis rangée initiale
            return True
        elif i2 == i1 + 1 and (j2 == j1 - 1 or j2 == j1 + 1):
            if color2 == 'b':
                # prise d'une pièce blanche
                return True
            if i1 == 4 and (lastmove[0][0], lastmove[0][1], lastmove[1][0]) == (6, j2, 4) and board[4][j2] == 'Pb':
                # prise en passant
                return True
        return False


def mvt_pion(board, depart, arriv, lastmove, bool_roque):
    """Renvoie le plateau une fois le pion déplacé du départ à l'arrivée
        (renvoie le plateau en argument si le mouvement est invalide)

    Args:
        board (liste de listes de strings): configuration avant mvt
        depart (tuple de taille 2): les coordonnées de la pièce à déplacer
        arriv (tuple de taille 2): les coordonnées de la case d'arrivée
        lastmove (liste de 2 tuples): les coordonnées du dernier coup
        bool_roque (dictionnaire de 6 booléens): si les tours/rois peuvent roquer
     """
    i1, j1, i2, j2 = depart[0], depart[1], arriv[0], arriv[1]
    if mvt_pion_poss(board, depart, arriv, lastmove, bool_roque):  # si le déplacement est valide
        if i2 == i1 - 1 and j2 != j1 and (board[i2][j2])[1] == ' ':
            # prise en passant d'un pion noir
            board[3][j2] = '  '
        if i2 == i1 + 1 and j2 != j1 and (board[i2][j2])[1] == ' ':
            # prise en passant d'un pion blanc
            board[4][j2] = '  '
        board[i2][j2] = board[i1][j1]
        board[i1][j1] = '  '  # la case de départ devient vide
    return board


mvt_dico_poss = {'R': mvt_roi_poss, 'D': mvt_dame_poss, 'C': mvt_cavalier_poss,
                 'F': mvt_fou_poss, 'T': mvt_tour_poss, 'P': mvt_pion_poss}

mvt_dico = {'R': mvt_roi, 'D': mvt_dame, 'C': mvt_cavalier,
            'F': mvt_fou, 'T': mvt_tour, 'P': mvt_pion}
