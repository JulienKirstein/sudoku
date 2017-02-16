def commun(liste):
    for i in liste[1:]:
        liste[0] = list(set(liste[0]) & set(i))
    return liste[0]


def possi_lignes(tableau):
    r = []
    c = 0
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for a in tableau:
        for i in a:
            if i in l:
                r += [i]
        while c < len(a):
            if a[c] not in r:
                a[c] = list(set(l) - set(r))
            c += 1
        r = []
        c = 0
    return tableau


def afficher(tableau):
    for i in tableau:
        print(i)


def colonne(tableau):
    liste = [[], [], [], [], [], [], [], [], []]
    for i in tableau:
        c = 0
        while c < 9:
            liste[c] += [i[c]]
            c += 1
    return liste


def additionner(liste, val):
    c = 0
    while c < 9:
        liste[c] += val
        c += 1
    return liste


def tableau_vers_liste(tableau):
    lis = []
    for i in tableau:
        lis += i
    return lis


def liste_vers_tableau(l):
    lis = []
    lisend = []
    d = 0
    while d < 9:
        c = 0 + d *9
        while c  < 9 + 9*d:
            lis += [l[c]]
            c += 1
        lisend += [lis]
        lis = []
        d += 1
    return lisend


def carré(tableau):
    l = []
    liste = []
    for i in [0, 3, 6, 27, 30, 33, 54, 57, 60]:
        liste += additionner([0, 1, 2, 9, 10, 11, 18, 19, 20], i)
    for i in liste:
        l += [tableau_vers_liste(tableau)[i]]
    total = []
    liste = []
    d = 1
    while d < 10:
        c = 0 + (d - 1) * 9
        while c < 9 * d:
            liste += [l[c]]
            c += 1
        total += [liste]
        liste = []
        d += 1
    return (total)


def carré_vers_tableau(tableau, x):
    o = [0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = []
    liste = []
    for i in [0, 3, 6, 27, 30, 33, 54, 57, 60]:
        liste += additionner([0, 1, 2, 9, 10, 11, 18, 19, 20], i)

    for i in liste:
        l += [tableau_vers_liste(tableau)[i]]

    l2 = tableau_vers_liste(x)

    c = 0
    while c < len(liste):
        o[liste[c]] = l2[c]
        c += 1

    total = []
    liste = []
    d = 1
    while d < 10:
        c = 0 + (d - 1) * 9
        while c < 9 * d:
            liste += [o[c]]
            c += 1
        total += [liste]
        liste = []
        d += 1
    return (total)


def vers_bon_format(l):
    d = 0
    c = 0
    while c < 9:
        while d < 9:
            if "[" not in str(l[c][d]):
                l[c][d] = [l[c][d]]
            d += 1
        d = 0
        c += 1
    return l


def fusion(l1, l2, l3):
    nul = [[[], [], [], [], [], [], [], [], []],
           [[], [], [], [], [], [], [], [], []],
           [[], [], [], [], [], [], [], [], []],
           [[], [], [], [], [], [], [], [], []],
           [[], [], [], [], [], [], [], [], []],
           [[], [], [], [], [], [], [], [], []],
           [[], [], [], [], [], [], [], [], []],
           [[], [], [], [], [], [], [], [], []],
           [[], [], [], [], [], [], [], [], []]]
    d = 0
    c = 0
    while c < 9:
        while d < 9:
            nul[c][d] += [l3[c][d]] + [l2[c][d]] + [l1[c][d]]
            d += 1
        d = 0
        c += 1
    return nul


def fonction(tableau):

    l1 = possi_lignes(tableau)
    l2 = colonne(possi_lignes(colonne(tableau)))
    l3 = carré_vers_tableau(tableau, possi_lignes(carré(tableau)))
    nul = fusion(vers_bon_format(l1), vers_bon_format(l2), vers_bon_format(l3))
    d = 0
    c = 0
    while d < 9:
        while c < len(nul[d]):
            nul[d][c] = commun(nul[d][c])
            c += 1
        c = 0
        d += 1
    #print(nul)
    # on a simplifié jusqu'ici ceux que l'on pouvais , il faut donc tout recommencer en commencer par actualiser le tableau
    # afficher(nul) ====> grille "semi-résolue"
    d = 0
    c = 0
    while d < 9:
        while c < len(nul[d]):
            if len(nul[d][c]) != 1:
                nul[d][c] = 0
            else:
                nul[d][c] = nul[d][c][0]
            c += 1
        c = 0
        d += 1
    # afficher(nul) ===> grille "semi-résolue" du meme format que celle initiale
    tableau = nul
    return tableau


tableau = [[1, 0, 6, 0, 0, 0, 0, 0, 0],
           [0, 9, 0, 1, 4, 7, 0, 0, 0],
           [0, 2, 7, 0, 8, 0, 0, 0, 0],
           [3, 7, 0, 2, 0, 0, 9, 0, 0],
           [2, 0, 0, 0, 0, 0, 0, 0, 6],
           [0, 0, 5, 0, 0, 9, 0, 2, 3],
           [0, 0, 0, 0, 2, 0, 8, 7, 0],
           [0, 0, 0, 3, 5, 6, 0, 1, 0],
           [0, 0, 0, 0, 0, 0, 6, 0, 5]]

afficher(tableau)
print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
afficher(fonction(tableau))
print("eeeeeeeeeeeeeeeeeeee")
afficher(tableau)