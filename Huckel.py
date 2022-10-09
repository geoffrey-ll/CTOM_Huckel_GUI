import numpy
import argparse
import sys
#import blabla


ensemble_fichiers = []
nom_fichier_for_gui = []
donnees_atomes = {
                'C': {'structure': 'C R2', 'n': '1', 'ka': '0', 'kb': '1'},
                'B': {'structure': 'B R2', 'n': '0', 'ka': '-0.45', 'kb': '0.73'},
                'N2': {'stucture': 'N R2', 'n': '1', 'ka': '0.51', 'kb': '1.02'},
                'N3': {'stucture': 'N R3', 'n': '2', 'ka': '1.37', 'kb': '0.89'},
                'O2': {'structure': 'O R', 'n': '1', 'ka': '0.97', 'kb': '1.06'},
                'O3': {'structure': 'O R2', 'n': '2', 'ka': '2.09', 'kb': '0.66'},
                'F': {'structure': 'F R', 'n': '2', 'ka': '2.71', 'kb': '0.52'},
                'Si': {'structure': 'Si R3', 'n': '1', 'ka': '0', 'kb': '0.75'},     # ka silicium = 0 ????
                'P2': {'structure': 'P R2', 'n': '1', 'ka': '0.19', 'kb': '0.77'},
                'P3': {'structure': 'P R3', 'n': '2', 'ka': '0.75', 'kb': '0.76'},
                'S2': {'structure': 'S R', 'n': '1', 'ka': '0.46', 'kb': '0.81'},
                'S3': {'structure': 'S R2', 'n': '2', 'ka': '1.11', 'kb': '0.69'},
                'Cl': {'structure': 'Cl R', 'n': '2', 'ka': '1.48', 'kb': '0.62'},
                'Me': {'structure': 'Me R', 'n': '2', 'ka': '2.00', 'kb': '0.707'}
                  }
index_element_donnees_atomes = {
                                '0': 'C', '1': 'B', '2': 'N2', '3': 'N3', '4': 'O2', '5': 'O3', '6': 'F',
                                '7': 'Si', '8': 'P2', '9': 'P3', '10': 'S2', '11': 'S3', '12': 'Cl', '13': 'Me'


                                }
ATOME_GERER = ["C", "B", "N", "O", "F", "Si", "P", "S", "Cl", "Me"]
atome_gerer = ["c", "b", "n", "o", "f", "si", "p", "s", "cl", "me"]

def verif_hamilton_carre(nom_du_fichier):
    with open(nom_du_fichier) as f:
        lignes_fichier = f.readlines()
        n_hamilton = 0
        m_hamilton = 0

        #Determine la taille n de la matrice hamiltonienne du fichier
        for element in lignes_fichier[0]:
            if element == "1":
                n_hamilton = n_hamilton + 1
            if element == "0":
                n_hamilton = n_hamilton + 1
            for ATOME in ATOME_GERER:
                if element == ATOME:
                    n_hamilton = n_hamilton + 1
            for atome in atome_gerer:
                if element == atome:
                    n_hamilton = n_hamilton + 1

        #Determine la taille m de la matrice hamiltonienne du fichier
        for index in range(len(lignes_fichier)):
            for element in lignes_fichier[index][0]:
                if element == "1":
                    m_hamilton = m_hamilton + 1
                if element == "0":
                    m_hamilton = m_hamilton + 1
                for ATOME in ATOME_GERER:
                    if element == ATOME:
                        m_hamilton = m_hamilton + 1
                for atome in atome_gerer:
                    if element == atome:
                        m_hamilton = m_hamilton + 1

        #Determine la taille n de toutes les lignes du fichier
        n_hamilton_ligne = []
        for ligne in lignes_fichier:
            n_hamilton_local = 0
            for element in lignes_fichier[lignes_fichier.index(ligne)]:
                if element == "1":
                    n_hamilton_local = n_hamilton_local + 1
                elif element == "0":
                    n_hamilton_local = n_hamilton_local + 1
                else:
                    for ATOME in ATOME_GERER:
                        if element == ATOME:
                            n_hamilton_local = n_hamilton_local + 1
                    for atome in atome_gerer:
                        if element == atome:
                            n_hamilton_local = n_hamilton_local + 1
            n_hamilton_ligne.append(n_hamilton_local)

        #Determine la taille m de toutes les colones du fichier
        m_hamilton_colone = []
        len_ligne = []
        for ligne in lignes_fichier:
            len_ligne.append(len(lignes_fichier[lignes_fichier.index(ligne)]))
        for valeur in len_ligne:
            numero_colone = 0
            while numero_colone < valeur - 1:
                m_hamilton_local = 0
                for ligne in lignes_fichier:
                    index_ligne = lignes_fichier.index(ligne)
                    len_inde = len(lignes_fichier[lignes_fichier.index(ligne)])
                    for element in lignes_fichier[lignes_fichier.index(ligne)][numero_colone]:
                        if element == "1":
                            m_hamilton_local = m_hamilton_local + 1
                        elif element == "0":
                            m_hamilton_local = m_hamilton_local + 1
                        elif element == " ":
                            pass
                        else:
                            for ATOME in ATOME_GERER:
                                if element == ATOME:
                                    m_hamilton_local = m_hamilton_local + 1
                            for atome in atome_gerer:
                                if element == atome:
                                    m_hamilton_local = m_hamilton_local + 1
                numero_colone = numero_colone + 1
                if m_hamilton_local != 0:
                    m_hamilton_colone.append(m_hamilton_local)

        nbr_ligne = len(n_hamilton_ligne)
        nbr_colone = len(m_hamilton_colone)
        n_error = []
        m_error = []
        for i in range(nbr_ligne):
            if n_hamilton_ligne[i] == n_hamilton:
                return "ok"
            else:
                n_error.append(n_hamilton_ligne.index(i))
        for j in range(nbr_colone):
            if m_hamilton_colone[j] == m_hamilton:
                return "ok"
            else:
                m_error.append(m_hamilton_colone.index(j))
        if n_error != []:
            if len(n_error) <= 1:
                print('La taille de la ligne {} est differente de la premiere ligne'.format(n_error + 1))
            if len(n_error) > 1:
                print('La taille des lignes {}, sont differente de la premiere ligne'.format(n+1 for n in n_error))

        print("n hamilton : ", n_hamilton)
        print("m hamilton : ", m_hamilton)

        print("n ligne  : ", n_hamilton_ligne)
        print("m colone : ", m_hamilton_colone)
        
        if n_hamilton == m_hamilton:
            return "la matrice hamilton est carre"
        elif n_hamilton != m_hamilton:
            print('La matrice Hamiltonienne du fichier {} est de taille {}*{}.\nIl faut qu{}elle soit carre.'
                  .format(nom_du_fichier, n_hamilton, m_hamilton, "'"))


        n_error = []
        m_hamilton = []
        m_error = []



def lecture_fichier(nom_du_fichier):
    # lecture_fichier permet de transformer un fichier texte
    # en tableau qu'on nomme array
    with open(nom_du_fichier) as f:
        lignes_fichier = f.readlines()
        array_fichier_non_modifie = []
        array_str = []
        num_ligne_erreur = []
        list_atome_C = []
        list_atome_B = []
        list_atome_N2 = []
        list_atome_N3 = []
        list_atome_O2 = []
        list_atome_O3 = []
        list_atome_F = []
        list_atome_Si = []
        list_atome_P2 = []
        list_atome_P3 = []
        list_atome_S2 = []
        list_atome_S3 = []
        list_atome_Cl = []
        list_atome_Me = []
        list_atome_X = [list_atome_C, list_atome_B, list_atome_N2, list_atome_N3, list_atome_O2, list_atome_O3,
                        list_atome_F, list_atome_Si, list_atome_P2, list_atome_P3, list_atome_S2, list_atome_S3,
                        list_atome_Cl, list_atome_Me]

        # Boucle qui recopie le fichier texte dans le tableau array_fichier_non_modifie en class str
        # Utile pour l'indice de liaison. On ce refere a la valeur "1" pour des atomes lies, et au valeur "X" et "0"
        # pour des atomes pas lies
        for line in lignes_fichier:
            split_line_array_fichier_non_modifie = line.split()
            array_fichier_non_modifie.append(split_line_array_fichier_non_modifie)

        try:
            for line in lignes_fichier:
                split_line_str = line.split()
                array_str.append(split_line_str)        # Ajoute toutes les lignes dans le tableau array_str
            for lignes in array_str:        # Permet d'identifier la nature de l'atome de la ligne
                index_ligne_array_str = array_str.index(lignes)

                # Differentes conditions qui verifient s'il manque l'hybridation pour un atome et qui identifient
                # chaque lignes de array_str a une espece atomique
                for element in lignes:

                    # Conditions qui permet le renvoi d'une erreur (apres lecture de toutes les ligens pour identifier
                    # toutes les erreurs) a l'utilisateur si l'hybridation de l'atome n'est pas indiquer. Les elements
                    # pour lesquelles il faut indiquer l'hybridation sont : N ; O ; P et S
                    if element == "N" or element == "n":
                        num_ligne_erreur.append(index_ligne_array_str + 1)
                    if element == "O" or element == "o":
                        num_ligne_erreur.append(index_ligne_array_str + 1)
                    if element == "P" or element == "p":
                        num_ligne_erreur.append(index_ligne_array_str + 1)
                    if element == "S" or element == "s":
                        num_ligne_erreur.append(index_ligne_array_str + 1)

                    # Conditions qui affecte l'index de la ligne de array_str a une liste (list_atome_X) selon la
                    # nature de l'atome.
                    if element == "C" or element == "c":
                        list_atome_C.append(index_ligne_array_str)
                    if element == "B" or element == "b":
                        list_atome_B.append(index_ligne_array_str)
                    if element == "N2" or element == "n2":
                        list_atome_N2.append(index_ligne_array_str)
                    if element == "N3" or element == "n3":
                        list_atome_N3.append(index_ligne_array_str)
                    if element == "O2" or element == "o2":
                        list_atome_O2.append(index_ligne_array_str)
                    if element == "O3" or element == "o3":
                        list_atome_O3.append(index_ligne_array_str)
                    if element == "F" or element == "f":
                        list_atome_F.append(index_ligne_array_str)
                    if element == "SI" or element == "Si" or element == "sI" or element == "si":
                        list_atome_Si.append(index_ligne_array_str)
                    if element == "P2" or element == "p2":
                        list_atome_P2.append(index_ligne_array_str)
                    if element == "P3" or element == "p3":
                        list_atome_P3.append(index_ligne_array_str)
                    if element == "S2" or element == "s2":
                        list_atome_S2.append(index_ligne_array_str)
                    if element == "S3" or element == "s3":
                        list_atome_S3.append(index_ligne_array_str)
                    if element == "CL" or element == "Cl" or element == "cL" or element == "cl":
                        list_atome_Cl.append(index_ligne_array_str)
                    if element == "ME" or element == "Me" or element == "mE" or element == "me":
                        list_atome_Me.append(index_ligne_array_str)

            # Condition qui renvoi le message d'erreur si il manque l'hybridation pour l'un des elements concernes.
            # Indique la ligne correspondante et interrompt le programme
            if num_ligne_erreur != []:
                print("-" * 50, "\n", '{:^45}'.format("Le fichier est illisible\n"))
                for num_entite in range(len(num_ligne_erreur)):
                    print(('Lignes {} : {}\n{:11}{}\n{:11}{}').format(num_ligne_erreur[num_entite],
                                                                    "preciser la nature de l'atome :",
                                                                    " ", "X2 pour atome X sp2",
                                                                    " ", "X3 pour atome X sp3"))
                sys.exit()

            # Deroulement normale du programme.
            # Pour chaque element, modifie la chaine de caractere correspondant par sa valeur ka et modifie les
            # valeurs 1 qui les lie aux autres atomes, par leurs valeurs de kb

            # Boucle pour changer les valeurs des atomes de carbones
            index_element = 0
            for ligne_atome_C in list_atome_C:
                for element in array_str[ligne_atome_C]:
                    if element == "C" or element == "c":
                        array_str[ligne_atome_C][index_element] = donnees_atomes['C']['ka']
                    if element == "1":
                        array_str[ligne_atome_C][index_element] = donnees_atomes['C']['kb']
                    index_element = index_element +1
                index_element = 0
                for valeur in range(len(array_str)):
                    array_float = float(array_str[valeur][ligne_atome_C])
                    if array_float == 1:
                            array_str[valeur][ligne_atome_C] = donnees_atomes['C']['kb']

            # Boucle pour changer les valeurs des atomes de bore
            index_element = 0
            for ligne_atome_B in list_atome_B:
                for element in array_str[ligne_atome_B]:
                    if element == "B" or element == "b":
                        array_str[ligne_atome_B][index_element] = donnees_atomes['B']['ka']
                    if element == "1":
                        array_str[ligne_atome_B][index_element] = donnees_atomes['B']['kb']
                    index_element = index_element +1
                index_element = 0
                for valeur in range(len(array_str)):
                    array_float = float(array_str[valeur][ligne_atome_B])
                    if array_float == 1:
                            array_str[valeur][ligne_atome_B] = donnees_atomes['B']['kb']

            # Boucle pour changer les valeurs des atomes d'azote sp2
            index_element = 0
            for ligne_atome_N2 in list_atome_N2:
                for element in array_str[ligne_atome_N2]:
                    if element == "N2" or element == "n2":
                        array_str[ligne_atome_N2][index_element] = donnees_atomes['N2']['ka']
                    if element == "1":
                        array_str[ligne_atome_N2][index_element] = donnees_atomes['N2']['kb']
                    index_element = index_element +1
                index_element = 0
                for valeur in range(len(array_str)):
                    array_float = float(array_str[valeur][ligne_atome_N2])
                    if array_float == 1:
                            array_str[valeur][ligne_atome_N2] = donnees_atomes['N2']['kb']

            # Boucle pour changer les valeurs des atomes d'azote sp3
            index_element = 0
            for ligne_atome_N3 in list_atome_N3:
                for element in array_str[ligne_atome_N3]:
                    if element == "N3" or element == "n3":
                        array_str[ligne_atome_N3][index_element] = donnees_atomes['N3']['ka']
                    if element == "1":
                        array_str[ligne_atome_N3][index_element] = donnees_atomes['N3']['kb']
                    index_element = index_element +1
                index_element = 0
                for valeur in range(len(array_str)):
                    array_float = float(array_str[valeur][ligne_atome_N3])
                    if array_float == 1:
                            array_str[valeur][ligne_atome_N3] = donnees_atomes['N3']['kb']

            # Boucle pour changer les valeurs des atomes d'oxygene sp2
            index_element = 0
            for ligne_atome_O2 in list_atome_O2:
                for element in array_str[ligne_atome_O2]:
                    if element == "O2" or element == "o2":
                        array_str[ligne_atome_O2][index_element] = donnees_atomes['O2']['ka']
                    if element == "1":
                        array_str[ligne_atome_O2][index_element] = donnees_atomes['O2']['kb']
                    index_element = index_element + 1
                index_element = 0
                for valeur in range(len(array_str)):
                    array_float = float(array_str[valeur][ligne_atome_O2])
                    if array_float == 1:
                            array_str[valeur][ligne_atome_O2] = donnees_atomes['O2']['kb']

            # Boucle pour changer les valeurs des atomes d'oxygene sp3
            index_element = 0
            for ligne_atome_O3 in list_atome_O3:
                for element in array_str[ligne_atome_O3]:
                    if element == "O3" or element == "o3":
                        array_str[ligne_atome_O3][index_element] = donnees_atomes['O3']['ka']
                    if element == "1":
                        array_str[ligne_atome_O3][index_element] = donnees_atomes['O3']['kb']
                    index_element = index_element + 1
                index_element = 0
                for valeur in range(len(array_str)):
                    array_float = float(array_str[valeur][ligne_atome_O3])
                    if array_float == 1:
                        array_str[valeur][ligne_atome_O3] = donnees_atomes['O3']['kb']

            # Boucle pour changer les valeurs des atomes de fluor
            index_element = 0
            for ligne_atome_F in list_atome_F:
                for element in array_str[ligne_atome_F]:
                    if element == "F" or element == "f":
                        array_str[ligne_atome_F][index_element] = donnees_atomes['F']['ka']
                    if element == "1":
                        array_str[ligne_atome_F][index_element] = donnees_atomes['F']['kb']
                    index_element = index_element +1
                index_element = 0
                for valeur in range(len(array_str)):
                    array_float = float(array_str[valeur][ligne_atome_F])
                    if array_float == 1:
                        array_str[valeur][ligne_atome_F] = donnees_atomes['F']['kb']

            # Boucle pour changer les valeurs des atomes de silicium
            index_element = 0
            for ligne_atome_Si in list_atome_Si:
                for element in array_str[ligne_atome_Si]:
                    if element == "Si" or element == "si":
                        array_str[ligne_atome_Si][index_element] = donnees_atomes['Si']['ka']
                    if element == "1":
                        array_str[ligne_atome_Si][index_element] = donnees_atomes['Si']['kb']
                    index_element = index_element +1
                index_element = 0
                for valeur in range(len(array_str)):
                    array_float = float(array_str[valeur][ligne_atome_Si])
                    if array_float == 1:
                            array_str[valeur][ligne_atome_Si] = donnees_atomes['Si']['kb']

            # Boucle pour changer les valeurs des atomes de phosphore sp2
            index_element = 0
            for ligne_atome_P2 in list_atome_P2:
                for element in array_str[ligne_atome_P2]:
                    if element == "P2" or element == "p2":
                        array_str[ligne_atome_P2][index_element] = donnees_atomes['P2']['ka']
                    if element == "1":
                        array_str[ligne_atome_P2][index_element] = donnees_atomes['P2']['kb']
                    index_element = index_element +1
                index_element = 0
                for valeur in range(len(array_str)):
                    array_float = float(array_str[valeur][ligne_atome_P2])
                    if array_float == 1:
                            array_str[valeur][ligne_atome_P2] = donnees_atomes['P2']['kb']

            # Boucle pour changer les valeurs des atomes de phosphore sp3
            index_element = 0
            for ligne_atome_P3 in list_atome_P3:
                for element in array_str[ligne_atome_P3]:
                    if element == "P3" or element == "p3":
                        array_str[ligne_atome_P3][index_element] = donnees_atomes['P3']['ka']
                    if element == "1":
                        array_str[ligne_atome_P3][index_element] = donnees_atomes['P3']['kb']
                    index_element = index_element +1
                index_element = 0
                for valeur in range(len(array_str)):
                    array_float = float(array_str[valeur][ligne_atome_P3])
                    if array_float == 1:
                            array_str[valeur][ligne_atome_P3] = donnees_atomes['P3']['kb']

            # Boucle pour changer les valeurs des atomes de souffre sp2
            index_element = 0
            for ligne_atome_S2 in list_atome_S2:
                for element in array_str[ligne_atome_S2]:
                    if element == "S2" or element == "s2":
                        array_str[ligne_atome_S2][index_element] = donnees_atomes['S2']['ka']
                    if element == "1":
                        array_str[ligne_atome_S2][index_element] = donnees_atomes['S2']['kb']
                    index_element = index_element +1
                index_element = 0
                for valeur in range(len(array_str)):
                    array_float = float(array_str[valeur][ligne_atome_S2])
                    if array_float == 1:
                            array_str[valeur][ligne_atome_S2] = donnees_atomes['S2']['kb']

            # Boucle pour changer les valeurs des atomes de souffre sp3
            index_element = 0
            for ligne_atome_S3 in list_atome_S3:
                for element in array_str[ligne_atome_S3]:
                    if element == "S3" or element == "s3":
                        array_str[ligne_atome_S3][index_element] = donnees_atomes['S3']['ka']
                    if element == "1":
                        array_str[ligne_atome_S3][index_element] = donnees_atomes['S3']['kb']
                    index_element = index_element +1
                index_element = 0
                for valeur in range(len(array_str)):
                    array_float = float(array_str[valeur][ligne_atome_S3])
                    if array_float == 1:
                            array_str[valeur][ligne_atome_S3] = donnees_atomes['S3']['kb']

            # Boucle pour changer les valeurs des atomes de chlore sp3
            index_element = 0
            for ligne_atome_Cl in list_atome_Cl:
                for element in array_str[ligne_atome_Cl]:
                    if element == "Cl" or element == "cl":
                        array_str[ligne_atome_Cl][index_element] = donnees_atomes['Cl']['ka']
                    if element == "1":
                        array_str[ligne_atome_Cl][index_element] = donnees_atomes['Cl']['kb']
                    index_element = index_element +1
                index_element = 0
                for valeur in range(len(array_str)):
                    array_float = float(array_str[valeur][ligne_atome_Cl])
                    if array_float == 1:
                            array_str[valeur][ligne_atome_Cl] = donnees_atomes['Cl']['kb']

            # Boucle pour changer les valeurs des atomes de methyl
            index_element = 0
            for ligne_atome_Me in list_atome_Me:
                for element in array_str[ligne_atome_Me]:
                    if element == "Me" or element == "me":
                        array_str[ligne_atome_Me][index_element] = donnees_atomes['Me']['ka']
                    if element == "1":
                        array_str[ligne_atome_Me][index_element] = donnees_atomes['Me']['kb']
                    index_element = index_element +1
                index_element = 0
                for valeur in range(len(array_str)):
                    array_float = float(array_str[valeur][ligne_atome_Me])
                    if array_float == 1:
                            array_str[valeur][ligne_atome_Me] = donnees_atomes['Me']['kb']

##### Print provisoire
#            print("\narray_str avec valeur remplacer :\n")
#            for ligne in range(len(array_str)):
#                print('{}'.format(array_str[ligne]))
#####


        except:

            print("-" * 50, "\n", '{:^45}'.format("Fin du programme"))


        # Boucle transformant le array_str en array_float
        array_float = array_str
        for ligne in array_str:
            index_ligne = array_str.index(ligne)
            for valeur in ligne:
                index_valeur = ligne.index(valeur)
                array_float[index_ligne][index_valeur] = float(valeur)

        return array_float, list_atome_X, array_fichier_non_modifie

##### print provisoire
#        print('{}\n{}\n\nLe array flottant :\n'.format("-" * 50, "-" * 50))
#        for element in range(len(array_float)):
#            print('{}'.format(array_float[element]))
#####



#                split_line_float = [float(i) for i in split_line_str]  # conversion de string vers flottant
#                array.append(split_line_float)
#            for ligne in array:
#                for valeur in ligne:
#                    if valeur != 1 and valeur != 0:     # Exclue du programme tous les fichiers contenant des nombres
#                                                        # differents de 1 ou de 0
#                        print('\nLe fichier {} est illisible\nLe fichier ne doit contenir que des 0 et des '
#                              '1 separes par des espaces\n'.format(nom_du_fichier))
#                        return "Erreur #404"
#        except:
#                # Exclue du programme tous les fichiers contenant des elements qui ne seraient pas des nombres
#            print('\nLe fichier {} est illisible\nLe fichier ne doit contenir que des 0 et des '
#                                  '1 separes par des espaces\n'.format(nom_du_fichier))
#            return "Erreur #404"
#    return array


def transforme_array(nom_du_fichier):
    # transforme_array transforme le tableau du fichier texte en matrice numpy
    # qu'on nomme matrix
    inter1, inter11, inter12 = lecture_fichier(nom_du_fichier)    # inter1 est une variable intermediaire
                        # inter1 = array_float      inter11 = list_atome_X      inter12 = array_fichier_non_modifie
    matrix = numpy.matrix(inter1)
    return matrix


def diagonalisation_matrix(nom_du_fichier):
    # diagonalisation_matrix : diagonalise la matrice numpy nommé matrix
    # et on la nomme matrix_diag
    inter2 = transforme_array(nom_du_fichier)   # inter2 est une variable intermediaire     inter2 = matrix
                                                # correspondant a l'execution du
                                                # def precedent
    E, V = numpy.linalg.eigh(inter2)
    # E est la valeur propre de la diagonalisation de la matrice
    # V est le vecteur propre de la diag
    # E représente l'énergie de l'électron du carbone ième élément
    # V représente la forme des kk de la molécule
    OM = numpy.transpose(V) # permet l'affichage des kk en lignes
                            # ainsi les kk sont des éléments de transpose(V)
    return E, OM


def forme_OM(nom_du_fichier):
    # cette fonction ordonne les éléments E et V définit
    # On ordonne E par ordre croissant
    # la fonction zip() permet de d'associer chaque V à sa valeur de E
    # ainsi les V sont ordonner selon les énergies croissant des orbitals pz(pi) de la molécule
    inter3, inter4 = diagonalisation_matrix(nom_du_fichier) # inter3 = E      inter4 = OM
    EOM = zip(inter3, inter4)   # les valeurs des OM sont associées à leur valeurs E correspondantes
    E_tri_decroi_and_OM_associe = sorted(EOM, reverse = True) # dans la notation Huckel, les beta sont négatives. Comme les beta dans le fichier
                                    # n'ont pas été multiplié par (-1), on ordonne les E dans le sens décroissants
    nOM = nOA = len(E_tri_decroi_and_OM_associe)

    print('{:^45}\n'.format("Orbitales moleculaires"))
    print(('{}').format(" " * 9), end='')
    for i in range(nOM):
        print(('{:11d}C  ').format(i + 1), end='')
    print()
    for iOM in range(nOM):
        print('\u03a8 {:<3} ='.format(iOM + 1), end='')
        for iOA in range(nOA):
            print((' {:=+9.5f} pz{:1}'.format(E_tri_decroi_and_OM_associe[iOM][1].item(iOA), iOA + 1)), end='')
        print()
    print("\n")

#Determine le nombre d'electron par orbitale moleculaire selon le nombre d'electron pz apporter par l'ensemble des
# atomes de la molecule
def repartition_electron(nom_du_fichier):
    increment_electron = []
    inter7, inter8, inter9 = lecture_fichier(nom_du_fichier)    # inter7 = array_float  inter8 = list_atome_X
    list_atome_X = inter8                                   # inter 9 = array_fichier_non_modifie

    # Boucle permettant de connaitre le nombre d'electron pz de la molecule.
    # cad le nbr d'atome X dans la molecule **
    # le nbre d'electron pz que l'atome X apporte (indiquer dans la biblio donnees_atomes[i]['n']
    for list_atome in list_atome_X:
        index_atome = list_atome_X.index(list_atome)
        nbr_atome = len(list_atome)
        if index_atome == 0:
            increment_electron.append(nbr_atome * float(donnees_atomes['C']['n']))
        if index_atome == 1:
            increment_electron.append(nbr_atome * float(donnees_atomes['B']['n']))
        if index_atome == 2:
            increment_electron.append(nbr_atome * float(donnees_atomes['N2']['n']))
        if index_atome == 3:
            increment_electron.append(nbr_atome * float(donnees_atomes['N3']['n']))
        if index_atome == 4:
            increment_electron.append(nbr_atome * float(donnees_atomes['O2']['n']))
        if index_atome == 5:
            increment_electron.append(nbr_atome * float(donnees_atomes['O3']['n']))
        if index_atome == 6:
            increment_electron.append(nbr_atome * float(donnees_atomes['F']['n']))
        if index_atome == 7:
            increment_electron.append(nbr_atome * float(donnees_atomes['Si']['n']))
        if index_atome == 8:
            increment_electron.append(nbr_atome * float(donnees_atomes['P2']['n']))
        if index_atome == 9:
            increment_electron.append(nbr_atome * float(donnees_atomes['P3']['n']))
        if index_atome == 10:
            increment_electron.append(nbr_atome * float(donnees_atomes['S2']['n']))
        if index_atome == 11:
            increment_electron.append(nbr_atome * float(donnees_atomes['S3']['n']))
        if index_atome == 12:
            increment_electron.append(nbr_atome * float(donnees_atomes['Cl']['n']))
        if index_atome == 13:
            increment_electron.append(nbr_atome * float(donnees_atomes['Me']['n']))


    inter3, inter4 = diagonalisation_matrix(nom_du_fichier)  # inter3 = E      inter4 = OM
    EOM = zip(inter3, inter4)  # les valeurs des OM sont associées à leur valeurs E correspondantes
    c = sorted(EOM, reverse=True)
    n_electron_total = sum(increment_electron)
    n_electron_a_distrib = n_electron_total
    n_electron_OM = []

    # Boucle indiquant le nombre d'electron par OM
    for i_Orbitale_Moleculaire in range(len(c)):
        for OM in c[i_Orbitale_Moleculaire][1]:
            if n_electron_a_distrib >= 2:
                n_electron_OM.append(2)
                n_electron_a_distrib = n_electron_a_distrib - 2
            elif n_electron_a_distrib == 1:
                n_electron_OM.append(1)
                n_electron_a_distrib = n_electron_a_distrib - 1
            elif n_electron_a_distrib == 0:
                n_electron_OM.append(0)
                n_electron_a_distrib = n_electron_a_distrib - 0

    return n_electron_OM









# Indique l'énergie de chaque OM
def energie_OM(nom_du_fichier):
    inter5, inter6 = diagonalisation_matrix(nom_du_fichier)
    E = sorted(inter5, reverse = True)  # E est l'énergie (valeur propre de la diag) ordonner par ordre décroissant car
                                        # beta<0 dans la convention de Huckel

    inter7 = repartition_electron(nom_du_fichier)       # inter7 = n_electron_OM
    n_electron_OM = inter7
    n_electron_total = sum(n_electron_OM)

    nOM = len(E)
    print('{:^20}\n'.format("Energies"))
    E_des_OM = []

    for iOM in range(nOM):
        E_des_OM.append(n_electron_OM[iOM] * E[iOM])
        print("\u03b5 {:<3} = ".format(iOM+1), end='')       # alpha = \u03b1    beta = \u03b2   epsilon = \u03b5
        print("\u03b1 {:=+9.5f} \u03b2".format(E[iOM]))

    print("\n\u03b5 total = {} \u03b1 + {:.5f} \u03b2".format(n_electron_total, sum(E_des_OM))) # sum() somme les élément d'une liste
    print("\n")

    return E, E_des_OM, n_electron_OM, n_electron_total


# Indique l'énergie total de tous les fichiers traiter
def list_en_ensemble_fichier(nom_du_fichier):

    inter5, inter6 = diagonalisation_matrix(nom_du_fichier)
    E = sorted(inter5, reverse=True)  # E est l'énergie (valeur propre de la diag ordonnee par ordre décroissant car
    # beta<0 dans la convention de Huckel

    inter7 = repartition_electron(nom_du_fichier)   # inter7 = n_electron_OM
    n_electron_OM = inter7

    n_electron_total = sum(n_electron_OM)
    E_des_OM = []
    nOM = len(E)

    for iOM in range(nOM):
        E_des_OM.append(n_electron_OM[iOM] * E[iOM])
    try:
        print("\n\u03b5({}) total = {}\u03b1 + {:.5f} \u03b2".format(nom_du_fichier, n_electron_total, sum(E_des_OM)))
    except:
        print("je ne veux pas te donner l'info !!!!")




#Pour comparer les en de plusieurs fichiers entre eux
def comparaison_en(nom_du_fichier):

    tous_les_E = []
    tous_les_E_des_OM = []
    E, E_des_OM = energie_OM(nom_du_fichier)
    tous_les_E.append(E)
    tous_les_E_des_OM.append(E_des_OM)

    #print("684", "E", E, "\n", "E om", E_des_OM)
    print("688", "ts E",  tous_les_E, "\nts E om", tous_les_E_des_OM)








def indice_liaison(nom_du_fichier):
    inter3, inter4 = diagonalisation_matrix(nom_du_fichier)  # inter3 = E      inter4 = OM
    EOM = zip(inter3, inter4)  # les valeurs des OM sont associées à leur valeurs E correspondantes
    c = sorted(EOM, reverse=True)   # dans la notation Huckel, les beta sont négatives. Comme les beta dans le fichier
                                    # n'ont pas été multiplié par (-1), on ordonne les E dans le sens décroissants
    inter5 = repartition_electron(nom_du_fichier)   # inter5 = n_electron_OM
    n_electron_OM = inter5

    inter6, inter7, inter8 = lecture_fichier(nom_du_fichier)
    # inter6 = array_str    inter7 = list_atome_X   inter8 = array_fichier_non_modifie
    array_fichier_non_modifie = inter8

    IL = []
    IL_prov = []        # Quand deux atomes sont lies, cad quand on a une valeur = 1 dans le texte alors on calcul IL
                        # pour les atomes correspondant. Comme il s'agit d'une somme de produit, on stocke les valeurs
                        # succesive des produits dans une liste. Pour ensuite utiliser la fonction sum() qui marche
                        # pour une liste mais qui ne marche pas pour une liste de liste.
    print('{:^45}\n'.format("indice de liaison"))
    print(('{}').format(" " * 11), end='')
    for i in range(len(c)):
        print(('{:7}C   ').format(i+1), end = '')
    print()
    for i in range(len(c)):     # i est le numero de lignes du tableau texte nomme array_fichier_non_modifie
        for j in range(len(c)): # j est le numero de colones du tableau texte nomme array_fichier_non_modifie
                if array_fichier_non_modifie[i][j] == "0":
                    IL.append(0)        # Les atomes array_fichier_non_modifie [lignes][valeur] ne sont pas lies
                elif array_fichier_non_modifie[i][j] != "0" and array_fichier_non_modifie[i][j] != "1":
                    IL.append(0)
                elif array_fichier_non_modifie[i][j] == "1":
                    atome_A = i         # Les atomes array_fichier_non_modifie[lignes][valeur] sont lies
                    atome_B = j
                    for i_OM in range(len(c)):
                        for OM in c[i_OM][1]:
                            IL_prov.append(n_electron_OM[i_OM] * c[i_OM][1].item(atome_A) * c[i_OM][1].item(atome_B))
                    IL.append(sum(IL_prov))
                    IL_prov[:] = []     # Une fois la valeur de IL determiner on reinitialise la liste IL_prov pour le
                                        # prochain calcul.
                        # Comme IL n'est pas une liste de listes, on ne peut pas appeler la valeur de IL selon son index
                        # donc on utilise une methode alternative on se servant de la varible machin.
    machin = 0          # machin est la variable qui permet de recuperer le bon index de IL
    for k in range(len(c)):
        print(('IL {:<3} :'.format(k+1)), end='')
        for i in range(len(c)):
            print(((' {:=+9.5f}').format(IL[machin])), end = '')
            machin = machin + 1     # k vaut len(c) et i vaut len(c) donc la boucle dans la boucle permet d'obtenir
                                    # machin = k*i = len(IL)
        print()
    print("\n")


def charge_atome(nom_du_fichier):
    # cette fonction ordonne les éléments E et V définit
    # On ordonne E par ordre croissant
    # la fonction zip() permet de d'associer chaque V à sa valeur de E
    # ainsi les V sont ordonner selon les énergies croissant des orbitals pz(pi) de la molécule
    inter3, inter4 = diagonalisation_matrix(nom_du_fichier) # inter3 = E      inter4 = OM
    EOM = zip(inter3, inter4)   # les valeurs des OM sont associées à leur valeurs E correspondantes
    c = sorted(EOM, reverse = True) # dans la notation Huckel, les beta sont négatives. Comme les beta dans le fichier
                                    # n'ont pas été multiplié par (-1), on ordonne les E dans le sens décroissants

    inter5 = repartition_electron(nom_du_fichier)       # inter5 = n_electron_OM
    n_electron_OM = inter5      # nombre d'electron par OM
    nOM = nOA = n_total_electron = len(c)

    inter6, inter7, inter8 = lecture_fichier(nom_du_fichier)
    # inter6 = array_float      inter7 = list_atome_X       inter8 = array_fichier_non_modifie
    list_atome_X = inter7

    num_atome_X = []
    nbr_e_X = []
    # num_atome_X = numero de l'atome X dans la molecule (= son numero de ligne dans le fichier texte)
    # nbr_e_X = le nombre d'electron que l'atome X apporte en pz dans la molecule (= donnees_atomes['X']['n'])

    # Boucle permettant d'associer a chaque atome d'indice(numero de ligne) le nombre d'electron pz qu'il apporte
    # dans la molecule
    for list_atome in list_atome_X:
        index_list = list_atome_X.index(list_atome)
        for num_ligne_atome_X in list_atome:
            if index_list == 0:
                num_atome_X.append(num_ligne_atome_X)
                nbr_e_X.append(donnees_atomes['C']['n'])
            if index_list == 1:
                num_atome_X.append(num_ligne_atome_X)
                nbr_e_X.append(donnees_atomes['B']['n'])
            if index_list == 2:
                num_atome_X.append(num_ligne_atome_X)
                nbr_e_X.append(donnees_atomes['N2']['n'])
            if index_list == 3:
                num_atome_X.append(num_ligne_atome_X)
                nbr_e_X.append(donnees_atomes['N3']['n'])
            if index_list == 4:
                num_atome_X.append(num_ligne_atome_X)
                nbr_e_X.append(donnees_atomes['O2']['n'])
            if index_list == 5:
                num_atome_X.append(num_ligne_atome_X)
                nbr_e_X.append(donnees_atomes['O3']['n'])
            if index_list == 6:
                num_atome_X.append(num_ligne_atome_X)
                nbr_e_X.append(donnees_atomes['F']['n'])
            if index_list == 7:
                num_atome_X.append(num_ligne_atome_X)
                nbr_e_X.append(donnees_atomes['Si']['n'])
            if index_list == 8:
                num_atome_X.append(num_ligne_atome_X)
                nbr_e_X.append(donnees_atomes['P2']['n'])
            if index_list == 9:
                num_atome_X.append(num_ligne_atome_X)
                nbr_e_X.append(donnees_atomes['P3']['n'])
            if index_list == 10:
                num_atome_X.append(num_ligne_atome_X)
                nbr_e_X.append(donnees_atomes['S2']['n'])
            if index_list == 11:
                num_atome_X.append(num_ligne_atome_X)
                nbr_e_X.append(donnees_atomes['S3']['n'])
            if index_list == 12:
                num_atome_X.append(num_ligne_atome_X)
                nbr_e_X.append(donnees_atomes['Cl']['n'])
            if index_list == 13:
                num_atome_X.append(num_ligne_atome_X)
                nbr_e_X.append(donnees_atomes['Me']['n'])

    # num_atome_X__nbr_e_X = est le tuple associant le numero de ligne et le nombre d'electron apporte par cet atome
    # num_atome_X__nbr_e_X__ordonner = est le tri du tuple par ordre croissant du numero de ligne
    num_atome_X__nbr_e_X = zip(num_atome_X, nbr_e_X)
    num_atome_X__nbr_e_X__ordonner = sorted(num_atome_X__nbr_e_X)


    # Boucle affichant la charge electronique de chaque atome
    q_prov = []
    print('{:^45}\n'.format("charge electronique des atomes"))
    for j_atome in range(len(c)):
        for i_OM in range(len(c)):
            for OM in c[i_OM][1]:
                q_prov.append(n_electron_OM[i_OM] * c[i_OM][1].item(j_atome) * c[i_OM][1].item(j_atome))
        electron_X_pz = num_atome_X__nbr_e_X__ordonner[j_atome][1]
        q_atome = float(electron_X_pz) - sum(q_prov)
        print('q {:<3} = {:7.5f}'.format(j_atome + 1, q_atome))
        q_prov[:] = []
    print()


#def list_OM(nom_du_fichier):
#    list_OM =  "Affiche toutes les OM"
#    return list_OM
#    print('{:^45}\n'.format("Ensemble des OM"))
#    print('{:5} : {:^30}'.format("OM de", nom_du_fichier))
#    forme_OM(nom_du_fichier)
#    print('{}'.format("-" * 50))



def main():

    ##### Fonction main coder en souple pour utiliser le programme depuis le cmd #####

    # Traitement des arguments
    # Un argument obligatoires, le nom du fichier qui doit etre lu. Les autres arguments renvois les differents
    # resultats sont des arguments optionnelles
    description_prog = ('\n{:^60}\n\n{}\n{}')\
                        .format("Programme Huckel", "permet de caluler les OM, les energies,"
                                    "les indices de liaisons", "et les charges electroniques des atomes")
    parser = argparse.ArgumentParser(description = description_prog)
    parser.add_argument('fichier', help='Nom du fichier', nargs = '*',
                        default = ('\n{:^45}\n'.format("Entrer le(s) nom(s) du(es) fichier(s)")))

        # nargs = '*' Tous les arguments de la ligne de commande sont groupes dans une liste.
        # Il permet aussi d'ajouter une valeur par default si aucun argument n'est entrer dans la ligne de commande.
        # nargs = '?' permet aussi de traiter plusieurs arguments en ligne de commande mais ne renvoi rien
        # en cas si aucun argument n'est entrer
        # nargs = '+' permet aussi de traiter plusieurs arguments ne ligne de commande et de renvoiyer la valeur
        # default si aucun argument n'est entrer mais ajoute également un message d'erreur (celui qui liste les
        # arguments positionnels et optionnelles
    parser.add_argument('-om', help = "Orbitales moleculaires", action = "store_true")
    parser.add_argument('-en', help = "Energies des differents carbones de la molecule", action = "store_true")
    parser.add_argument('-il', help = "Indices de liaisons entre les carbones lies entre eux", action = "store_true")
    parser.add_argument('-q', help = "Charge electronnique des carbones", action = "store_true")
    parser.add_argument('-list_en', help = "Affiche l'energie total des differentes molecules"
                        , action = "store_true")
    parser.add_argument('-com_en', help = "Compare l'energies des differentes molecules", action = "store_true")
    parser.add_argument('-gui', help = "Interface graphique affichant la matrice hamiltonienne de la molecule "
                                       "et son energie, qu'il est ensuite possible de comparer avec une matrice "
                                       "hamiltonienne modifier", action = "store_true")
    parser.add_argument('-tout', help = "Toutes les proprietes", action = "store_true")

#    parser.add_argument('-list_om', help = "Affiche les OM de tous les fichiers", action = "store_true")
    args = parser.parse_args()
    ensemble_fichiers = args.fichier

    # On traite la list_en_ensemble_fichier des energies de façon particuliere pour un souci d'esthetique. Si seul -list_en est
    # demandee, cela permet d'afficher que ça. Et si autre chose est demande, de le faire preceder par les resultats
    # des calculs detailles molecules par molecules
#   if args.list_om == True:
#     for nom_du_fichier in args.fichier:
#       list_OM(nom_du_fichier)


    if args.om == False and args.en == False and args.il == False \
                    and args.q == False and args.tout == False and args.list_en == True and len(args.fichier) >= 2:
                    # Si tous les arguments sont absents sauf -list_en et que plusieurs noms de fichiers ont ete entrer
                    # en ligne de commande alors le programme n'affiche que la list_en_ensemble_fichier des energies
        print('{}'.format("-" * 50))
        print('\n{:^50}'.format("Energie total des differentes molecules"))
        for nom_du_fichier in ensemble_fichiers:
            if args.list_en:
                list_en_ensemble_fichier(nom_du_fichier)
                print()
    elif args.om == False and args.en == False and args.il == False \
                    and args.q == False and args.tout == False and args.list_en == True and len(args.fichier) <= 2:
        print('\n\n{:^55}'.format("Veuillez indiquer au moins deux fichiers\n"))
        print("-" * 50, "\n")
        print('{:^45}'.format("Fin du programme"))
        sys.exit()


    else:       # Dans ce cas le programme affiche tous ce qui est demande en le detaillant molecules par molecules
                # puit affiche la list_en_ensemble_fichier des energie si elle est demandee

        for nom_du_fichier in ensemble_fichiers:
            if lecture_fichier(nom_du_fichier) == "Erreur #404":
                # Erreur #404 signifie que le fichier n'est pas lisible
                # dans la fonction lecture_fichier(nom_du_fichier)
                print("-" * 50, "\n")
                print('{:^45}'.format("Fin du programme"))  # Annonce le message d'erreur #404 de la fonction
                # lecture_fichier et la fin du programme
            else:
                print("\n", "-" * 50, "\n")  # Deroulement normal du programme
                print('{:^45}\n'.format(nom_du_fichier))

                if args.om == False and args.en == False and args.il == False and args.q == False \
                        and args.tout == False \
                        and args.list_en == False \
                        and args.com_en == False\
                        and args.gui == False:

                    print('{:^49}'.format("Que souhaitez-vous calculer ?\n"))
                    print((('{:8} : {:}\n' * 6).format("-om", "Orbitales moleculaires",
                                                     "-en", "Energies des differents carbones de la molecule",
                                                     "-il", "Indices de liaisons entre les carbones lies entre eux",
                                                     "-q", "Charge electronique des carbones",
                                                     "-list_en", "Energie total des differentes molecules",
                                                     "-tout", "Toutes les proprietes ci-dessus",)),
                                ('\n{:8} : {:}'.format("-gui", "Interface graphique pour la comparaison des energies",)),
                                ('\n{:11}{}\n'.format(" ", "de la molecule avec une structure modifier de celle-ci")))
                    # Si aucun arguments optionnelles ne entres apres le nom du fichier cette condition renvoi un message
                    # a l'utilisateur demandant ce qu'ils doit etre calcules
                if args.om:  # Affiche les OM
                    forme_OM(nom_du_fichier)
                if args.en:  # Affiche les enengies
                    energie_OM(nom_du_fichier)
                if args.com_en: #Compare les energie des differentes molecules
                    for n_fichier in range(len(args.fichier)):
                        nom_du_fichier = args.fichier[n_fichier]
                        comparaison_en(nom_du_fichier)
                if args.il:  # Affiche les indices de liaisons
                    indice_liaison(nom_du_fichier)
                if args.q:  # Affiche les charges electronique
                    charge_atome(nom_du_fichier)
                if args.gui:

                    nom_fichier_for_gui.append(nom_du_fichier)

                if args.tout:  # Affiche tout
                    forme_OM(nom_du_fichier)
                    energie_OM(nom_du_fichier)
                    indice_liaison(nom_du_fichier)
                    charge_atome(nom_du_fichier)
        if nom_fichier_for_gui != []:
            import gui_Huckel
        if len(args.fichier) >= 2 and args.list_en == True or len(args.fichier) >=2 and args.tout == True:
            # Cette condition permet d'afficher
            # la list_en_ensemble_fichier des energies dans le cas ou ce n'est
            # pas la seul chose qui est demande
            print('{}'.format("-" * 50))
            print('\n{:^50}'.format("Energie total des differentes molecules"))
            for nom_du_fichier in ensemble_fichiers:
                if args.list_en or args.tout:
                    list_en_ensemble_fichier(nom_du_fichier)
                    print()
    print("-" * 50, "\n")
    print('{:^45}'.format("Fin du programme"))
    if "Erreur #404" == False:
        print("-" * 50, "\n")
        print('{:^45}'.format("Fin du programme"))


    ##### Fonction main code en dur pour utiliser le programme dans python #####
def main_construction():
    # ensemble_fichiers_a_traiter : permet de traiter plusieurs fichiers dans la meme execution
    # ensemble_fichiers_a_traiter[0] : nom_du_fichier
    # ensemble_fichiers_a_traiter[1] : "OM:oui" si on veux les OM
    # ensemble_fichiers_a_traiter[2] : "energie:oui" si on veux les energies
    # ensemble_fichiers_a_traiter[3] : "IL:oui" si on veux les indices de liaisons
    # ensemble_fichiers_a_traiter[4] : "q:oui" si on veux les charges electroniques des atomes de la molecule
    ensemble_fichiers_a_traiter = []
#    ensemble_fichiers_a_traiter.append(["c2h4", "OM:oui", "energie:oui", "IL:oui", "q:oui"])
 #   ensemble_fichiers_a_traiter.append(["c4h6", "OM:oui", "energie:oui", "IL:oui", "q:oui"])
  #  ensemble_fichiers_a_traiter.append(["c5h7", "OM:oui", "energie:oui", "IL:oui", "q:oui"])
   # ensemble_fichiers_a_traiter.append(["c6h8", "OM:oui", "energie:oui", "IL:oui", "q:oui"])
    #ensemble_fichiers_a_traiter.append(["c5h5", "OM:oui", "energie:oui", "IL:oui", "q:oui", "com_en:non"])
    #ensemble_fichiers_a_traiter.append(["test2", "OM:oui", "energie:oui", "IL:oui", "q:oui", "com_en:non"])
#    ensemble_fichiers_a_traiter.append(["c6h6", "OM:oui", "energie:oui", "IL:oui", "q:oui"])
 #   comparaison_energie = "non"
    for liste in ensemble_fichiers_a_traiter:
        nom_du_fichier = liste[0]
        print('{:^45}\n'.format(nom_du_fichier))
   #     if liste[1] == "OM:oui": # execute
    #        forme_OM(nom_du_fichier)
        if liste[2] == "energie:oui":
            energie_OM(nom_du_fichier)
       # if liste[3] == "IL:oui":
        #    indice_liaison(nom_du_fichier)
#        if liste[4] == "q:oui":
 #           charge_atome(nom_du_fichier)
  #      print("-" * 50, "\n")
   # if comparaison_energie == "oui":
    #    print('{:^45}'.format("Energie de l'ensemble des fichiers"))
     #   for liste in ensemble_fichiers_a_traiter:
      #      nom_du_fichier = liste[0]
       #     list_en_ensemble_fichier(nom_du_fichier)
        #print("-"* 50, "\n")
#    print('{:^45}'.format("Fin du programme"))
        if liste[5] == "com_en:oui":
            comparaison_en(nom_du_fichier)





def main_2():
    parser = argparse.ArgumentParser()
    parser.add_argument('fichier', help = "Nom du fichier", nargs = "*", default = "voila")
    args = parser.parse_args()
    ensemble_fichiers = args.fichier
    for nom_du_fichier in ensemble_fichiers:
        repartition_electron(nom_du_fichier)


def main_3():
    ensemble_des_fichier = []
    ensemble_des_fichier.append("test2")
    ensemble_des_fichier.append("c2h4")
    for entree in ensemble_des_fichier:
        fichier = ensemble_des_fichier.index(entree)
        nom_du_fichier = ensemble_des_fichier[fichier]
#    nom_du_fichier = "c2h4"
#    nom_du_fichier = "C3H5O2"
#    nom_du_fichier = "tous_les_element_no_error"
    #lecture_fichier(nom_du_fichier)
    #verif_hamilton_carre(nom_du_fichier)
        comparaison_en(nom_du_fichier)


main()
#main_2()
#main_3()
#main_construction()