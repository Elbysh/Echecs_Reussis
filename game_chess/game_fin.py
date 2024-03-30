from .game_mvt import *
# from game_chess.game_mvt import *

mvt_dico_poss = {'R': mvt_roi_poss, 'D': mvt_dame_poss, 'C': mvt_cavalier_poss,
                 'F': mvt_fou_poss, 'T': mvt_tour_poss, 'P': mvt_pion_poss}

mvt_dico = {'R': mvt_roi, 'D': mvt_dame, 'C': mvt_cavalier,
            'F': mvt_fou, 'T': mvt_tour, 'P': mvt_pion}


def rois(echiquier):
    """Renvoie un dictionnaire associant la couleur des rois
        à leurs coordonnées (tuple de taille 2) 

    Args:
        echiquier (liste de listes de strings): grille de jeu actuelle

    Returns:
        (dictionnaire): en 'b', le couple des coordonnées du blanc, en 'n' le noir
    """
    positions = {'b': (0, 0), 'n': (0, 0)}
    # on parcourt l'échiquier case par case pour trouver les rois
    for i in range(8):
        for j in range(8):
            if echiquier[i][j] == 'Rb':
                positions['b'] = (i, j)
            if echiquier[i][j] == 'Rn':
                positions['n'] = (i, j)
    return positions


# on mettra rois(echiquier)[0], rois(echiquier)[1] en parametre


def echec(echiquier, lastmove, bool_roque):
    """caractérise une situation d'échec

    Args:
        echiquier (liste de 8 listes de 8 strings): configuration actuelle
        lastmove (liste de 2 tuples): les coordonnées du dernier coup
        bool_roque (dictionnaire de 6 booléens): si les tours/rois peuvent roquer
    Returns:
        ((booléen, string)) : (False, '') sans échec, True et la couleur en échec sinon
    """
    # cherche les positions des rois
    positions_rois = {0: (0, 0), 1: (0, 0)}
    for i in range(8):
        for j in range(8):
            if echiquier[i][j] == 'Rb':
                positions_rois[0] = (i, j)
            if echiquier[i][j] == 'Rn':
                positions_rois[1] = (i, j)

    roi_blanc, roi_noir = positions_rois[0], positions_rois[1]

    dico_echec = {'b': False, 'n': False}

    # on parcourt l'échiquier case par case
    for i in range(8):
        for j in range(8):
            # pour voir si une pièce blanche met en échec le roi noir
            if echiquier[i][j][1] == 'b':
                if mvt_dico_poss[echiquier[i][j][0]](echiquier, (i, j), roi_noir, lastmove, bool_roque):
                    dico_echec['n'] = True
            # pour voir si une pièce noire met en échec le roi blanc
            if echiquier[i][j][1] == 'n':
                if mvt_dico_poss[echiquier[i][j][0]](echiquier, (i, j), roi_blanc, lastmove, bool_roque):
                    dico_echec['b'] = True
    return dico_echec


def echec_et_mat(echiquier, lastmove, bool_roque):
    """caractérise une situation d'échec et mat, appelée seulement si échec

    Args:
        echiquier (liste de 8 listes de 8 strings): configuration actuelle
        lastmove (liste de 2 tuples): les coordonnées du dernier coup
        bool_roque (dictionnaire de 6 booléens): si les tours/rois peuvent roquer
    Returns:
       ((booléen, string)) : (False, '') sans échec et mat, True et la couleur en échec et mat sinon
    """
    cases = [(i, j) for i in range(8) for j in range(8)]
    copie_echiquier = [[elem for elem in line] for line in echiquier]
    # couleur du roi en échec (appelée qu'en situation d'échec)
    if echec(echiquier, lastmove, bool_roque)['b']:
        defenseur = 'b'
    elif echec(echiquier, lastmove, bool_roque)['n']:
        defenseur = 'n'
    # on parcourt l'échiquier case par case
    for i in range(8):
        for j in range(8):
            # pour voir où sont les pièces du défenseur
            if echiquier[i][j][1] == defenseur:
                # on reparcourt l'échiquier case par case
                for k in range(8):
                    for l in range(8):
                        # pour voir où peuvent aller les pièces du défenseur
                        if (i, j) != (k, l) and mvt_dico_poss[echiquier[i][j][0]](echiquier, (i, j), (k, l), lastmove, bool_roque):
                            copie_echiquier = [[elem for elem in line]
                                               for line in echiquier]
                            # et si ces mouvements permettent de sortir de l'échec
                            if not echec(mvt_dico[echiquier[i][j][0]](copie_echiquier, (i, j), (k, l), defenseur, bool_roque), lastmove, bool_roque)[defenseur]:
                                return False, ''
    return True, defenseur


def pat(echiquier, trait, lastmove, bool_roque):
    """caractérise l'état de pat

    Args:
        echiquier (liste de 8 listes de 8 strings): configuration actuelle
        trait (string): couleur qui devrait joueur le prochain coup
        lastmove (liste de 2 tuples): les coordonnées du dernier coup
        bool_roque (dictionnaire de 6 booléens): si les tours/rois peuvent roquer

    Returns:
        (booléen) : true s'il y a pat
    """
    # si le joueur au trait est en échec, il n'y a pas pat
    if echec(echiquier, lastmove, bool_roque)[trait]:
        return False
    # on parcourt l'échiquier case par case
    for i in range(8):
        for j in range(8):
            # pour voir où sont les pièces du joueur au trait
            if echiquier[i][j][1] == trait:
                # on reparcourt l'échiquier case par case
                for k in range(8):
                    for l in range(8):
                        # pour voir où peuvent aller les pièces du joueur au trait
                        if (i, j) != (k, l) and mvt_dico_poss[echiquier[i][j][0]](echiquier, (i, j), (k, l), lastmove, bool_roque):
                            # et effectuer chaque mouvement possible
                            copie_echiquier = [[elem for elem in line]
                                               for line in echiquier]
                            echiquier_apres = mvt_dico[echiquier[i][j][0]](
                                copie_echiquier, (i, j), (k, l), trait, bool_roque)
                            # cherche une piece adverse qui mettrait en échec le joueur qui doit jouer, après le mouvement testé
                            echec_ici = False
                            for m in range(8):
                                for n in range(8):
                                    if echiquier_apres[m][n][1] == adversaire(trait):
                                        positions = rois(echiquier_apres)
                                        roi_trait = positions[trait]
                                        # si on trouve une pièce adverse, alors le pat n'est pas nié, on cherchera un autre (k, l)
                                        if mvt_dico_poss[echiquier_apres[m][n][0]](echiquier_apres, (m, n), roi_trait, lastmove, bool_roque):
                                            echec_ici = True

                            if not echec_ici:
                                return False
    # si pour toute piece blanche, aucun mouvement possible n'empeche un echec
    return True


def adversaire(trait):
    """détermine l'adversaire de celui qui a le trait

    Args:
        trait (string): couleur qui a le trait

    Returns:
        string: couleur qui n'a pas le trait
    """
    if trait == 'b':
        return 'n'
    else:
        return 'b'
