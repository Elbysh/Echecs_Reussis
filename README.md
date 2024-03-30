# Echecs à deux joueurs


## Lancement du jeu

Pour tester le MVP, il suffit d'exécuter le fichier **mvp.py**, du module **game_chess**. Chacun son tour, un joueur tape une case (a8, e5... la case de départ), tape Enter, tape y (ou n s'il veut en choisir une autre), tape Enter, tape une deuxième case (la case d'arrivée), Enter, et le coup est joué (s'il est possible). Voilà ! Les informations sur la partie en cours (trait, échec...) s'affichent directement dans le terminal utilisé.

Pour lancer le jeu, il suffit d'exécuter le fichier **main.py**, du module **game_chess**. Une fenêtre contenant un plateau d'échec s'ouvre. Pour jouer, il faut cliquer gauche sur une case (qui deviendra case de départ) et droit sur une autre (case d'arrivée), puis cliquer sur "Configurer" (ou Espace) pour effectuer le mouvement. Les informations sur la partie s'affichent dans la fenêtre. 
De plus, on peut parcourir les positions précédentes au moyen des flèches gauche (vers le passé) et droite (vers le présent) de la fenêtre, et revenir à la partie par "current". Pour quitter le jeu, cliquer sur Echap.


## Description

### Généralités

Ce programme fournit une interface graphique permettant à deux joueurs de jouer aux échecs dans le strict respect des règles du jeu, dont les modules se trouvent dans le dossier **game_chess**

Le module **game_mvt** contient toutes les fonctions controlant l'évolution des pièces (déplacement, prise). Il contient deux types de fonctions : 
``mvt_fou_poss`` indique si le mouvement demandé est possible suivant les critères de déplacement du fou, après avoir vérifié que la pièce déplacée est un fou. La fonction ``mvt_fou`` effectue le mouvement du fou demandé, après avoir appelé ``mvt_fou_poss`` pour vérifier qu'il était licite.

Le module **game_fin** contient les fonctions décrivant les situations particulières du jeu d'échec. 
La fonction ``roi`` est un outil indiquant les coordonnées des deux rois sur un plateau donné.
La fonction ``echec`` indique si un joueur (ou les deux) sont en échec sur un échiquier donné, quel qu'il soit.
La fonction ``echec_et_mat`` précise si un joueur est en situation d'échec et mat dans une situation de jeu donnée (les règles ne permettent pas que les deux joueurs le soient simultanément).
La fonction ``pat`` indique s'il y a pat, également dans une situation de jeu donnée.

### Minimal viable product (MVP)

Le module **board** gère la création du plateau d'échec sous forme d'une liste de listes de chaines de caractères de taille 8 par 8. Par exemple 'Cn' est un cavalier noir, 'Db' est une dame blanche. 
Elle permet également l'affichage d'une grille primitive, comme ``print`` d'une chaine de caractères.

Le module **game_input** permet la communication entre le jeu et les joueurs. 
Le dictionnaire ``echecs_vers_matrice`` convertit les commandes traditionnelles (a8, e5), en coordonnées dans un échiquier ((0, 0), (4, 4)).
La fonction ``read_player_command`` demande le coup du joueur sous forme traditionnelle, avec un input y ou n (yes ou no) pour valider ou invalider la case de départ et la case d'arrivée demandées.

Le module **mvp** permet le lancement du jeu au stade MVP dans la fonction ``game_play`` : affichage par ``print``, assemblage des fonctions-briques de base définies plus haut. Il n'applique que les règles de jeu basiques, la prise en passant et la promotion des pions ne sont pas possibles. 

### Jeu fini

Le module **main** est une refonte du module **mvp** en structure **tkinter**. ``create_chessboard`` affiche un plateau d'échecs selon les conventions classiques (chess.com, lichess.org). Les fonctions ``on_cell_click`` permettent la sélection des pièces à la souris en cliquant sur les pièces (clic gauche départ, clic droit arrivée), 
La fonction ``movements`` implémente toutes les règles et les applique aux coups demandés. La prise en passant et la promotion sont possibles. 
Les fonctions ``retour`` permettent de parcourir (en affichage seulement) les positions précédentes d'une partie en cours.

### Tests

Chaque fonction du MVP a été testée par une fonction d'un module du dossier **test**. Le fichier **test_board** permet le test des fonctions du module **board**, et ainsi de suite. Les tests permettent de vérifier chacune des boucles des fonctions. Certains tests ont nécessité un mock (dans le module **game_input**) pour simuler l'entrée de la commande d'un joueur. Les fonctions du module **main** (pour le jeu fini) étant copiées du MVP, et pour la plupart des fonctions d'affichages utilisant **tkinter**, n'ont pas été testées par l'algorithme.


## Répartition du travail

Toutes les fonctionnalités du MVP en été codées en parallèle, la création et l'affichage du plateau par Oscar, les évolutions de pièces (déplacements, prises) par Yi et Pierre, les situations particulières (échec, pat) par Raphaël, l'acquisition des commandes des joueurs par William, et les tests de toutes ces fonctions par Oscar et William. 
Les fonctionnalités du jeu fini ont nécessité une légère refonte de certaines fonctions de base (notamment des ajouts d'arguments aux fonctions). Ces refontes ont été effectuées par Pierre et Raphaël. Le roque et les promotions ont été codées par Yi. Oscar s'est chargé de l'affichage du jeu (module **main**) et de l'adaptation de ``game_play`` pour **tkinter**.


## Étapes de la programmation

**Sprint 1 :**
- Fonctionnalité 1 :
Création de la grille initiale
- Fonctionnalité 2 :
Afficher la grille en version MVP

**Sprint 2 :**
- Fonctionnalité 3 :
Gestion des déplacements

**Sprint 3 :**
- Fonctionnalité 4 :
Gestion des échecs et de l’échecs et mat   
- Fonctionnalité 5 :
Implémentation du Pat 

**Sprint 4 :**
- Fonctionnalité 6 :
Gestion des inputs des joueurs 	
- Fonctionnalité 7 :
Lancement du jeu

***Fin du MVP***

**Sprint 5 :**
- Fonctionnalité 8 :
Affichage d’un échiquier avec l’interface graphique plus évoluée
- Fonctionnalité 9 :
Mise en place de la configuration du jeu via l’interface graphique

**Sprint 6 :**
- Fonctionnalité 10 :
Implémentation du Roque 

**Sprint 7 :**
- Fonctionnalité 11 :
Implémentation des promotions 
- Fonctionnalité 12 :
Implémentation de la prise en passant 

***Fin du jeu***


## À l'avenir

Le projet permet de jouer aux échecs de façon presque complètement opérationnelle. Quelques dernières fonctionnalités pourraient être envisagées pour améliorer encore le produit :
- Le retournement de l'échiquier pour permettre au joueur qui a le trait d'avoir son côté en bas de la fenêtre
- La prise en compte des règles spécifiques aux matchs de compétitions (horloge, parties nulles...)
- La possibilité de configurer une grille de départ quelconque, de faire de la résolution de problèmes, etc.
- La possibilité de partager l'interface avec un serveur distant, pour pouvoir jouer sur deux appareils différents


## Documents divers

Pour plus de détails sur la rédaction du code, ou une démonstration du jeu, rendez-vous au le lien suivant :

https://drive.google.com/drive/folders/1vq7xJkFQFsbzg3vmdBjOief71Lbo_hKR?usp=sharing

![Un début de partie, sur le produit fini](/visuels/PF_initial.jpeg "début de partie")
![Un début de partie, sur le produit fini](/visuels/PF_en_cours.jpeg "début de partie")

Bon jeu !