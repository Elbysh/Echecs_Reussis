import tkinter as tk
from board import *
from game_fin import *
from game_input import *
from game_mvt import *

# from game_chess.board import *
# from game_chess.game_fin import *
# from game_chess.game_input import *
# from game_chess.game_mvt import *
# from pygame import mixer

# Variables globales pour stocker les coordonnées de la cellule sélectionnée
selected_row = None
selected_col = None
# Variables globales pour les clics de départ et d'arrivée
d = (0, 0)
a = (0, 0)
# Variable globale pour enregistrer le dernier coup joué
lastmove = [(0, 0), (0, 0)]
# Variable global pour déterminer le tour de jeu
tour = 'blancs'
# Variables globale pour les lignes
coord_dep = (0, 0)
coord_arr = (0, 0)
fleche_id = None
# La clé associe à la pièce la valeur True si celle-ci n'a pas été bougée depuis le debut de la partie
bool_roque = {"RoiN": True, "RoiB": True, "TourGaucheB": True,
              "TourGaucheN": True, "TourDroitB": True, "TourDroitN": True, }


def create_chessboard(canvas, square_size, board):
    """création du plateau de jeu

    Args:
        canvas (tk.Canvas): cellules du plateau
        square_size (int): taille des cellules du plateau
        board (list): liste de listes contenant les pièces
    """
    global entry_label
    columns = 8
    rows = 8
    for row in range(8):
        for col in range(8):
            x1 = (0.75+col) * square_size
            y1 = (0.5+row) * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size

            # On alterne la couleur des cases en fonction de la somme de la ligne et de la colonne pour avoir le damier
            color = "wheat" if (row + col) % 2 == 0 else "darkgoldenrod"

            canvas.create_rectangle(
                x1, y1, x2, y2, fill=color, tag=(row, col), outline='white')

            # On calcule le centre de la case pour y placer le texte
            center_x = (x1 + x2) // 2 + 0.07 * square_size
            center_y = (y1 + y2) // 2

            # On ajoute le texte avec les coordonnées de la case
            text_id = canvas.create_text(center_x, center_y,
                                         text=str(Pieces[board[row][col]]), fill="black", font=("Helvetica", int(square_size//2)), tags=(row, col))
            chessboard_values[(row, col)] = text_id

    # On ajoute des repères pour les coordonnées des lignes à gauche du chessboard
    for row in range(8):
        x = 0.5*square_size  # columns * square_size + 20
        y = (0.5+row) * square_size + square_size // 2
        label_text = str(rows - row)
        canvas.create_text(x, y, text=label_text,  anchor=tk.E,
                           fill="black", font=("Helvetica", 12, "bold"))

    # On ajoute des repères pour les coordonnées (converties en lettres) des colonnes en bas du chessboard
    for col in range(8):
        x = (0.75+col) * square_size + square_size // 2
        y = (0.75+rows) * square_size
        label_text = Alphabet[col + 1]
        canvas.create_text(x, y, text=label_text, fill="black",
                           font=("Helvetica", 12, "bold"))


def movements():
    """Modifie l'échiquier en fonction des commandes de l'utilisateur 

    Returns:
        None: Toujours None
    """
    global board  # Variable globale pour l'échiquier
    global d  # Variable globale pour les coordonnées de départ
    global a  # Variable globale pour les coordonnées d'arrivée
    global tour  # Variable globale pour le tour de jeu
    global logs  # Variable globale pour les logs
    global coup  # Variable globale pour les logs
    global n  # Variable globale pour les logs
    global coord_dep  # Variable globale pour la flèche de mouvement
    global coord_arr  # Variable globale pour la flèche de mouvement
    global lastmove  # Variable globale pour la prise en passant
    global bool_roque  # Variable globale pour les roques

    # On réinitialise les coordonées pour les flèches
    coord_dep = (0, 0)
    coord_arr = (0, 0)

    msg1_label.config(text='')
    board_copy = [[board[i][j]
                   for j in range(len(board))] for i in range(len(board))]  # copie de l'échiquier pour faire des tests
    # Initialisation des variables pour le programme
    dep = d
    arr = a
    i_dep, j_dep = dep
    i_arr, j_arr = arr
    piece = board[i_dep][j_dep]
    if piece[1] != tour[0]:
        # s'il y n'y a pas une pièce de la bonne couleur
        print("ce n'est pas la bonne couleur !")
        msg_label.config(text="Ce n'est pas la bonne couleur !")
        return None
    if dep == arr:
        # si la case de départ est la même que celle d'arrivée
        print("Pas de mouvement ! Recommencez")
        msg_label.config(text="Pas de mouvement ! Recommencez")
        return None
    newboard_copy = mvt_dico[piece[0]](
        board_copy, dep, arr, lastmove, bool_roque)  # On regarde comment le mouvement transforme l'échiquier
    if board == newboard_copy:
        # si le plateau reste le même ie si le coup est impossible
        print("Mouvement non valable ! Recommencez")
        msg_label.config(text="Mouvement non valable ! Recommencez")
        return None
    if echec(newboard_copy, lastmove, bool_roque)[tour[0]]:
        if echec(board, lastmove, bool_roque)[tour[0]]:
            # si le mouvement maintient en échec le joueur qui le joue
            print("Ce coup ne vous sort pas de l'échec ! Recommencez")
            msg_label.config(
                text="Ce coup vous ne vous sort pas de l'échec ! Recommencez")
            return None
        if not echec(board, lastmove, bool_roque)[tour[0]]:
            # si le mouvement met en échec le joueur qui le joue
            print("Ce coup vous met en échec ! Recommencez")
            msg_label.config(text="Ce coup vous met en échec ! Recommencez")
            return None
    # On effectue le mouvement maintenant qu'il a été validé
    board = mvt_dico[piece[0]](board, dep, arr, lastmove, bool_roque)
    # On met à jour bool_roque pour la suite de la partie
    if dep == (0, 0) or arr == (0, 0):
        bool_roque['TourGaucheN'] = False
    elif dep == (0, 4) or arr == (0, 4):
        bool_roque['RoiN'] = False
    elif dep == (0, 7) or arr == (0, 7):
        bool_roque['TourDroitN'] = False
    elif dep == (7, 7) or arr == (7, 7):
        bool_roque['TourDroitB'] = False
    elif dep == (7, 0) or arr == (7, 0):
        bool_roque['TourGaucheB'] = False
    elif dep == (7, 4) or arr == (7, 4):
        bool_roque['RoiB'] = False
    # On regarde (et on effectue) si il y a une promotion de pion possible
    promotion(board)
    if echec(board, lastmove, bool_roque)[adversaire(tour[0])]:
        # si le joueur adverse est en échec
        print('Les ' + dicocolor[adversaire(tour[0])] + ' sont en échec.')
        msg1_label.config(
            text='Les ' + dicocolor[adversaire(tour[0])] + ' sont en échec.', bg='yellow')
        if echec_et_mat(board, lastmove, bool_roque)[0]:
            # si le joueur adverse est en échec et mat
            print('Échec et mat !')
            msg1_label.config(text='Échec et mat !')
            print(f'La partie est finie, les {tour} ont gagné !')
            msg2_label.config(
                text=f'La partie est finie, les {tour} ont gagné !', bg='red')
            return None
    if pat(board, adversaire(tour[0]), lastmove, bool_roque):
        # s'il y a pat
        print('Il y a pat...')
        msg2_label.config(
            text="c'est fini, il y a pat...", bg='red')
        return None
    if tour == 'blancs':  # Passe au tour d'après
        tour = 'noirs'
    else:
        tour = 'blancs'

    # On modifie les labels du plateau et on met à jour les différentes variables globales
    entry_label.config(text=f'Traits aux {tour}', bg='snow')
    print("prochain tour")
    logs.append(promotion(newboard_copy))
    coup = len(logs) - 1
    n = len(logs) - 1
    msg_label.config(text="")
    msg4_label.config(text=f'coup {coup} sur {n} coup(s)')
    lastmove = [(i_dep, j_dep), (i_arr, j_arr)]


def promotion(board):
    """Demande au joueur de promouvoir son pion s'il atteint la rangée du fond
        et renvoie l'échiquier avec la pièce voulue à la place du pion

    Args:
        board (liste de 8 listes de 8 strings): configuration actuelle
    """
    global user_input
    for j in range(8):
        if board[0][j] == 'Pb':
            # si un pion blanc est dans la rangée du haut
            show_entry_window()  # On demande au joueur ce qu'il veut comme promotion
            promo = user_input.upper()
            while promo not in ['C', 'F', 'T', 'D']:
                show_entry_window()
                promo = user_input.upper()
            board[0][j] = promo + 'b'
            # la pièce blanche voulue remplace le pion
        if board[7][j] == 'Pn':
            # si un pion noir est dans la rangée du bas
            show_entry_window()
            promo = user_input.upper()
            # promo = input("Entrez l'initiale de la promotion (C, F, T ou D) :")
            while promo not in ['C', 'F', 'T', 'D']:
                show_entry_window()
                promo = user_input.upper()
            board[7][j] = promo + 'n'
            # la pièce noire voulue remplace le pion
    return board


def update_chessboard():
    """Mise à jour du plateau avec les mouvements des pièces à partir du bouton 'Configurer'
    """
    movements()
    create_chessboard(canvas, square_size, board)


def update_chessboard2(event):
    """Mise à jour du plateau avec les déplacements des pièces à partir de la souris

    Args:
        event (_type_): clic de la molette
    """
    movements()
    create_chessboard(canvas, square_size, board)


def on_cell_click_depart(event):
    """Modification des coordonnées de départ du déplacement

    Args:
        event (_type_): clic gauche de la souris
    """
    global d
    global coord_dep
    # Permet d'étendre la zone de détection du clic
    threshold = 1000

    # Identification de la cellule correspondant au clic
    item = canvas.find_closest(event.x, event.y)
    tags = canvas.gettags(item)

    # Si le clic ne permet pas de reconnaître une cellule
    if 'current' in tags and len(tags) == 1:
        print("Vous n'avez pas séléctionné une cellule")
    elif tags:
        # On récupère les tags que l'on a définis lors de la création des cellules (i.e. leurs coordonées)
        cell_tag = (int(tags[0]), int(tags[1]))
        selected_row = cell_tag[0]
        selected_col = cell_tag[1]

        # On calcule la distance entre le clic et le centre de la cellule
        center_x = (selected_col + 1) * square_size
        center_y = (selected_row + 1) * square_size
        distance = ((event.x - center_x)**2 + (event.y - center_y)**2)**0.5

        # On enregistre les coordonées
        coord_dep = ((selected_col + 1.5) * square_size,
                     (selected_row + 0.5) * square_size)

        # On regarde si le clic est dans la zone cliquable de la cellule
        if distance <= threshold:
            print((f'départ  {matrice_vers_echecs[cell_tag]}'))
            d = cell_tag  # On récupère le tag sur une variable globale
        else:
            print("Recliquez plus proche de la cellule")
    dep_label.config(text=f'départ  {matrice_vers_echecs[d]}', bg='snow')
    fleche_de_mvt()  # On crée la flèche de mouvement si possible


def on_cell_click_arrivee(event):
    """Modification des coordonnées d'arrivée du déplacement

    Args:
        event (_type_): clic droit de la souris
    """
    global a
    global coord_arr
    # Permet d'étendre la zone de détection du clic
    threshold = 1000

    # Identification de la cellule correspondant au clic
    item = canvas.find_closest(event.x, event.y)
    tags = canvas.gettags(item)

    # Si le clic ne permet pas de reconnaître une cellule
    if 'current' in tags and len(tags) == 1:
        print("Vous n'avez pas séléctionné une cellule")
    elif tags:
        # On récupère les tags que l'on a défini lors de la création des cellules (i.e. leurs coordonées)
        cell_tag = (int(tags[0]), int(tags[1]))
        selected_row = cell_tag[0]
        selected_col = cell_tag[1]

        # On calcule la distance entre le clic et le centre de la cellule
        center_x = (selected_col + 0.5) * square_size
        center_y = (selected_row + 0.5) * square_size
        distance = ((event.x - center_x)**2 + (event.y - center_y)**2)**0.5

        # On enregistre les coordonées
        coord_arr = ((selected_col + 1.5) * square_size, center_y)

        # On regarde si le clic est dans la zone cliquable de la cellule
        if distance <= threshold:
            print(f'arrivée {matrice_vers_echecs[cell_tag]}')
            a = cell_tag  # On récupère le tag sur une variable globale
        else:
            print("Recliquez plus proche de la cellule")
    arr_label.config(text=f'arrivée  {matrice_vers_echecs[a]}', bg='snow')
    fleche_de_mvt()  # On crée la flèche de mouvement si possible


def retour_en_arriere():
    """Afficher les coups précédents avec un bouton

    Returns:
        None
    """
    global logs
    global coup
    # On regarde si il est possible de revenir (encore) en arrière
    if coup > 0:
        coup = coup - 1
        msg3_label.config(text="")
        msg4_label.config(text=f'coup {coup} sur {n} coup(s)')
        create_chessboard(canvas, square_size, logs[coup])
        return None
    else:
        print("impossible")
        msg3_label.config(text="impossible")
        return None


def retour_en_arriere2(event):
    """Afficher les coups précédents avec le clavier

    Args:
        event (_type_): flèche gauche du clavier

    Returns:
        None
    """
    global logs
    global coup
    # On regarde si il est possible de revenir (encore) en arrière
    if coup > 0:
        coup = coup - 1
        msg3_label.config(text="")
        msg4_label.config(text=f'coup {coup} sur {n} coup(s)')
        create_chessboard(canvas, square_size, logs[coup])
        return None
    else:
        print("impossible")
        msg3_label.config(text="impossible")
        return None


def retour_en_avant():
    """Afficher les coups suivants si on est dans l'historique avec un bouton

    Returns:
        None
    """
    global logs
    global coup
    # On regarde si il y a des coups qui ont été joués après celui qui est affiché
    if coup < len(logs) - 1:
        coup = coup + 1
        msg3_label.config(text="")
        msg4_label.config(text=f'coup {coup} sur {n} coup(s)')
        create_chessboard(canvas, square_size, logs[coup])
        return None
    else:
        print("impossible")
        msg3_label.config(text="impossible")
        return None


def retour_en_avant2(event):
    """Afficher les coups suivants si on est dans l'historique avec un bouton

    Args:
        event (_type_): flèche gauche du clavier

    Returns:
        None: _description_
    """
    global logs
    global coup
    # On regarde si il y a des coups qui ont été joués après celui qui est affiché
    if coup < len(logs) - 1:
        coup = coup + 1
        msg3_label.config(text="")
        msg4_label.config(text=f'coup {coup} sur {n} coup(s)')
        create_chessboard(canvas, square_size, logs[coup])
        return None
    else:
        print("impossible")
        msg3_label.config(text="impossible")
        return None


def retour_a_zero():
    """Se remettre sur l'échiquier actuel avec un bouton

    Returns:
        None
    """
    global logs
    global coup
    coup = len(logs) - 1
    create_chessboard(canvas, square_size, logs[-1])
    msg3_label.config(text="")
    msg4_label.config(text=f'coup {coup} sur {n} coup(s)')
    return None


def retour_a_zero2(event):
    """Se remettre sur l'échiquier actuel avec le clavier

    Args:
        event (_type_): touche "entrée" du clavier

    Returns:
        None
    """
    global logs
    global coup
    coup = len(logs) - 1
    create_chessboard(canvas, square_size, logs[-1])
    msg3_label.config(text="")
    msg4_label.config(text=f'coup {coup} sur {n} coup(s)')
    return None


def fleche_de_mvt():
    """Afficher des flèches de déplacement entre le point de départ et le point d'arrivée de la pièce

    Returns:
        None
    """
    global coord_dep
    global coord_arr
    global fleche_id

    if fleche_id is not None:
        # On supprime la flèche actuelle si il y en a une
        canvas.delete(fleche_id)
    if coord_dep == (0, 0) or coord_arr == (0, 0) or coord_dep == coord_arr:
        # Si il n'y a pas encore eu une définition de la case d'arrivée et de la case de départ
        return None
    # On crée la flèche
    x1, y1 = coord_dep
    x2, y2 = coord_arr
    item = canvas.find_closest(x1, y1)
    x, y = canvas.gettags(item)[0:2]
    # on fait en sorte que la flèche parte et arrive au milieu d'une case
    fleche_id = canvas.create_line(
        x1 - 0.25 * square_size, y1 + 0.5 * square_size, x2 - 0.25 * square_size, y2 + 0.5 * square_size, arrow=tk.LAST, fill="green", width=4)
    return None


def show_entry_window():
    """On crée une fenêtre pour entrer les donées nécessaires à la promotion

    Returns:
        None
    """
    global entry_w, entry

    # On crée une nouvelle fenêtre lors de l'appel de cette fonction
    entry_w = tk.Toplevel(root)
    entry_w.title('Promotion')

    m_label = tk.Label(
        entry_w, text="Entrez l'initiale de la promotion (C, F, T ou D) :")
    m_label.pack()

    # On crée la zone de texte pour le joueur
    entry = tk.Entry(entry_w)
    entry.pack(padx=10, pady=10)

    # On crée le bouton "Valider" pour soumettre la saisie
    submit_button = tk.Button(
        entry_w, text="Valider (puis femer la fenêtre)", command=get_user_input)
    submit_button.pack(pady=10)

    # On bloque la fenêtre principale pour empêcher son interaction pendant la saisie
    entry_w.transient(root)
    entry_w.grab_set()
    root.wait_window(entry_w)
    return None


def get_user_input():
    """Récupère les données entrées par le joueur sur la fenêtre secondaire

    Returns:
        None
    """
    global user_input, entry
    user_input = entry.get()
    entry_w.destroy()
    print(f'a = {user_input}')
    return None


# Initialisation de l'échiquier
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

# Liste des logs
logs = [[[board[i][j]for j in range(len(board))] for i in range(len(board))]]
coup = len(logs) - 1
n = len(logs) - 1

# Alphabet
Alphabet = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}

# Dictionnaire pour l'affichage des pièces
Pieces = {'Pb': '♙ ', 'Tb': '♖ ', 'Cb': '♘ ', 'Fb': '♗ ', 'Db': '♕ ', 'Rb': '♔ ',
          'Pn': '♟ ', 'Tn': '♜ ', 'Cn': '♞ ', 'Fn': '♝ ', 'Dn': '♛ ', 'Rn': '♚ ', '  ': '  '}

# Mouvements pièces pour simplifier l'écriture des fonctions
mvt_dico = {'R': mvt_roi, 'D': mvt_dame, 'C': mvt_cavalier,
            'F': mvt_fou, 'T': mvt_tour, 'P': mvt_pion}
dicocolor = {'b': 'blancs', 'n': 'noirs'}

# Matrice vers échecs
matrice_vers_echecs = {value: key for key,
                       value in echecs_vers_matrice.items()}

# Création des widgets Tkinter en plein écran
root = tk.Tk()
root.title("Chessboard")
root.attributes("-fullscreen", True)

# Design des boutons
button_style = {'font': ('Helvetica', 12), 'width': 10,
                'height': 1, 'bg': '#8db596', 'fg': '#ffffff'}

# # Musique avec pygame
# mixer.init()
# mixer.music.load("../jeudéchec.mp3")
# mixer.music.play()

# Création du canva qui va contenir l'échiiquier
canvas_size = int(0.6 * root.winfo_screenheight())
square_size = canvas_size // 8

canvas = tk.Canvas(root, width=canvas_size + 100,
                   height=canvas_size + 100, bg="white")
canvas.pack()

chessboard_values = {}

# Création de l'échiquier initial
create_chessboard(canvas, square_size, board)

# On lie l'événement 'clic gauche de la souris' pour sélectionner le départ du mouvement
canvas.bind('<Button-1>', on_cell_click_depart)

# On lie l'événement 'clic droit de la souris' pour sélectionner l'arrivée du mouvement
canvas.bind('<Button-3>', on_cell_click_arrivee)

# Label pour le tour de jeu
entry_label = tk.Label(root, text=f'Traits aux {tour}', bg='snow')
entry_label.pack()

# Label pour les positions de départ et d'arrivée des pièces
dep_label = tk.Label(root, text=f'départ  {matrice_vers_echecs[d]}', bg='snow')
dep_label.pack()
arr_label = tk.Label(
    root, text=f'arrivée  {matrice_vers_echecs[a]}', bg='snow')
arr_label.pack()

# Label pour les différents messages
msg_label = tk.Label(root, text='')
msg_label.pack(side="top", padx=10, pady=0)
msg1_label = tk.Label(root, text='')
msg1_label.pack(side="left", padx=10, pady=0)
msg2_label = tk.Label(root, text='')
msg2_label.pack(side="left", padx=10, pady=0)
msg3_label = tk.Label(root, text='')
msg3_label.pack(side="top", padx=10, pady=0)
msg4_label = tk.Label(root, text=f'coup {coup} sur {n} coup(s)', **{'font': (
    'Helvetica', 12), 'width': 20, 'height': 1, 'bg': '#8db596', 'fg': '#ffffff'})
msg4_label.pack(side="left", padx=10, pady=0)


# Création de boutons pour pouvoir naviguer dans l'historique de la partie (logs)
left_button = tk.Button(
    root, text="<-", command=retour_en_arriere, **button_style)
left_button.pack(side="left", padx=0, pady=10)
mid_button = tk.Button(
    root, text="current", command=retour_a_zero, **button_style)
mid_button.pack(side="left", padx=0, pady=10)
right_button = tk.Button(
    root, text="->", command=retour_en_avant, **button_style)
right_button.pack(side="left", padx=0, pady=10)

# Bouton de création et configuration de la grille
configure_button = tk.Button(
    root, text="Configurer", command=update_chessboard, **button_style)
configure_button.pack(side="left", padx=10, pady=10)
# Alternative à ce bouton en cliquant sur la molette de la souris
canvas.bind('<Button-2>', update_chessboard2, add=True)
# Alternative à ce bouton en appuyant espace
root.bind('<KeyPress-space>', update_chessboard2, add=True)

# Navigation dans les logs mais avec des touches du clavier
root.bind('<Left>', retour_en_arriere2)
root.bind('<Right>', retour_en_avant2)
root.bind('<Return>', retour_a_zero2)


def fermer(event):
    """Fonction pour partir du plein écran et arrêter la partie
    """
    root.destroy()


# Partir du plein écran grâce à la touche 'Espace' du clavier
root.bind("<Escape>", fermer)


root.mainloop()
