from tkinter import *
import numpy
import Huckel


ensemble_fichiers = Huckel.nom_fichier_for_gui

fenetre = Tk()

#def sp_nom_fichier_command():

def affichage_noms_fichiers():

    for nom_du_fichier in ensemble_fichiers:
        titre = StringVar()
        titre.set(nom_du_fichier)
        lab_titre = Label(fenetre)
        sp_nom_du_fichier = Spinbox(lab_titre)
        sp_nom_du_fichier.configure(textvariable=titre)
        lab_titre.grid(row=1, column=1)
        sp_nom_du_fichier.grid(row=1, column=1)


def LA_fonction():

    for nom_du_fichier in ensemble_fichiers:
        #nom_du_fichier = "c2h4"

    # mat=array_float de lecture_fichier


        mat, list_atome_X, array_fichier_non_modifie = Huckel.lecture_fichier(nom_du_fichier)

        matrix_non_modifiable = mat.copy()
        matrix_modifiable = mat.copy()
        taille_matrix = len(matrix_modifiable)
        taille_matrix_plus1 = taille_matrix + 1

    # Definition fenetre principale


# Definition de variables
 ###########       titre = StringVar()

# Definition de valeur initiale
  ############      titre.set(nom_du_fichier)

# Definition de label
  ############      lab_titre = Label(fenetre)
        lab_espace_vide_apres_titre = Label(fenetre, text=" ")
        lab_nom_du_fichier = Label(fenetre)

        lab_numero_atome_ligne = Label(lab_nom_du_fichier)
        lab_numero_atome_colone = Label(lab_nom_du_fichier)
        lab_hamilton = Label(lab_nom_du_fichier)
        lab_nouveau_hamilton = Label(lab_nom_du_fichier)
        lab_numero_atome_ligne_nouveau_hamilton = Label(lab_nom_du_fichier)
        lab_numero_atome_colone_nouveau_hamilton = Label(lab_nom_du_fichier)
        lab_energie = Label(lab_nom_du_fichier)
        lab_nouvelle_energie = Label(lab_nom_du_fichier)
        lab_titre_spinbox = Label(lab_nom_du_fichier, text="Atome ligne\nAtome colone\n\n")
        lab_spinbox = Label(lab_nom_du_fichier)
        lab_espace_vide_avant_en = Label(lab_nom_du_fichier, text=" ")
        lab_espace_vide_vertical_avant_scroll = Label(fenetre, text=" ")
        lab_espace_vide_horizontal_avant_scroll = Label(fenetre, text=" ")


# Definition de spinbox
   ################     sp_nom_du_fichier = Spinbox(lab_titre)
        sp_atome_x = Spinbox(lab_spinbox)
        sp_atome_y = Spinbox(lab_spinbox)

# Definition de boutons
        bo_liaison_choisi = Button(lab_spinbox)
        bo_lancer_calcul_en = Button(lab_nom_du_fichier)

# Definition des scrollbar
        scroll_horizontal = Scrollbar(fenetre, orient="horizontal")
        scroll_vertical = Scrollbar(fenetre, orient="vertical")


##### Fonctions #####
        def numerotation_atome_ligne():
            for n in range(taille_matrix):
                numero_atome_ligne = StringVar()
                lab_numerotation_atome_ligne = Label(lab_numero_atome_ligne, textvariable=numero_atome_ligne)
                lab_numerotation_atome_ligne.configure(width=3)
                numero_atome_ligne.set('{}\n{}'.format("R", str(n + 1)))
                lab_numerotation_atome_ligne.grid(row=1, column=n)

        def numerotation_atome_colone():
            for m in range(taille_matrix):
                numero_atome_colone = StringVar()
                lab_numerotation_atome_colone = Label(lab_numero_atome_colone, textvariable=numero_atome_colone)
                numero_atome_colone.set('{} {}'.format((str(m + 1)), "R"))
                lab_numerotation_atome_colone.grid(row=m, column=1, sticky=E)

        def affichage_hamilton(nom_du_fichier):
            for n in range(taille_matrix):
                for m in range(taille_matrix):
                    valeur_hamilton = StringVar()
                    lab_affichage_hamilton = Label(lab_hamilton, textvariable=valeur_hamilton)
                    if matrix_non_modifiable[n][m] != 0:
                        valeur_hamilton.set(str('{:.2f}'.format(matrix_non_modifiable[n][m])))
                        lab_affichage_hamilton.configure(fg="red", width=3)
                    elif matrix_non_modifiable[n][m] == 0:
                        valeur_hamilton.set(str('{:.2f}'.format(matrix_non_modifiable[n][m])))
                        lab_affichage_hamilton.configure(fg="blue", width=3)
                    lab_affichage_hamilton.grid(row=n, column=m)
            numerotation_atome_colone()
            numerotation_atome_ligne()

        def numerotation_atome_ligne_nouveau_hamilton():
            for n in range(taille_matrix):
                numero_atome_ligne_nouveau_hamilton = StringVar()
                lab_numerotation_atome_ligne_nouveau_hamilton = Label(lab_numero_atome_ligne_nouveau_hamilton,
                                                                      textvariable=numero_atome_ligne_nouveau_hamilton)
                lab_numerotation_atome_ligne_nouveau_hamilton.configure(width=3)
                numero_atome_ligne_nouveau_hamilton.set('{}\n{}'.format("R", (str(n + 1))))
                lab_numerotation_atome_ligne_nouveau_hamilton.grid(row=1, column=n, sticky=E)

        def numerotation_atome_colone_nouveau_hamilton():
            for m in range(taille_matrix):
                numero_atome_colone_nouveau_hamilton = StringVar()
                lab_numerotation_atome_colone_nouveau_hamilton = Label(lab_numero_atome_colone_nouveau_hamilton,
                                                                       textvariable=numero_atome_colone_nouveau_hamilton)
                numero_atome_colone_nouveau_hamilton.set('{} {}'.format(str(m + 1), "R"))
                lab_numerotation_atome_colone_nouveau_hamilton.grid(row=m, column=1)

        def affichage_nouveau_hamilton():
            for n in range(taille_matrix):
                for m in range(taille_matrix):
                    valeur_nouveau_hamilton = StringVar()
                    lab_affichage_nouveau_hamilton = Label(lab_nouveau_hamilton, textvariable=valeur_nouveau_hamilton)
                    if matrix_modifiable[n][m] != 0:
                        valeur_nouveau_hamilton.set(str('{:.2f}'.format(matrix_modifiable[n][m])))
                        lab_affichage_nouveau_hamilton.configure(fg="red", width=3)
                    elif matrix_modifiable[n][m] == 0:
                        valeur_nouveau_hamilton.set(str('{:.2f}'.format(matrix_modifiable[n][m])))
                        lab_affichage_nouveau_hamilton.configure(fg="blue", width=3)
                    lab_affichage_nouveau_hamilton.grid(row=n, column=m)
            numerotation_atome_ligne_nouveau_hamilton()
            numerotation_atome_colone_nouveau_hamilton()
            return matrix_modifiable

        def change_hamilton():
            n = int(float(sp_atome_x.get()) - 1)
            m = int(float(sp_atome_y.get()) - 1)
            if matrix_modifiable[n][m] == 1:
                matrix_modifiable[n][m] = 0
            elif matrix_modifiable[n][m] == 0:
                matrix_modifiable[n][m] = 1
            #elif matrix_modifiable[n][m] != 1 and matrix_modifiable[n][m] != 0:
           #     matrix_modifiable[n][m] = 0
            affichage_nouveau_hamilton()

        def affichage_en(nom_du_fichier):
            E, E_des_OM, n_electron_OM, n_electron_total = Huckel.energie_OM(nom_du_fichier)
            nOM = len(E)
            row_en_pour_chaque_OM = 1
            for iOM in range(nOM):
                en_pour_chaque_OM = StringVar()
                lab_affichage_en = Label(lab_energie, textvariable=en_pour_chaque_OM)
                en_pour_chaque_OM.set("\u03b5 " + str('{:3d}'.format(iOM + 1)) + " = \u03b1 + " +
                                      str('{:8.5f}'.format(E[iOM])) + " \u03b2")
                lab_affichage_en.grid(row=row_en_pour_chaque_OM, column=1)
                row_en_pour_chaque_OM = row_en_pour_chaque_OM + 1
            en_total = StringVar()
            lab_affichage_en_total = Label(lab_energie, textvariable=en_total)
            en_total.set(
                "\n\u03b5 total = " + str(n_electron_total) + " \u03b1 + " + str(
                    '{:.5f}'.format(sum(E_des_OM))) + " \u03b2")
            lab_affichage_en_total.grid(row=row_en_pour_chaque_OM + 1, column=1)





        def ecriture_matrix_modifier():

            matrix_modifiable = affichage_nouveau_hamilton()
            with open("matrix_modifier", "w") as ligne:
                    for n in range(len(matrix_modifiable)):
                        ligne_new_fichier = []
                        for m in range(len(matrix_modifiable)):
                            if n == m:
                                ligne_new_fichier.append("C")
                            elif n != m:
                                ligne_new_fichier.append(str(int(matrix_modifiable[n][m])))
                            if m < len(matrix_modifiable) - 1:
                                ligne_new_fichier.append(" ")
                        ligne.writelines(ligne_new_fichier)
                        if n < len(matrix_modifiable) - 1:
                            ligne.writelines("\n")


        def affichage_nouveau_en():
            nom_du_fichier = "matrix_modifier"
            E, E_des_OM, n_electron_OM, n_electron_total = Huckel.energie_OM(nom_du_fichier)
            nOM = len(E)
            row_en_pour_chaque_OM = 1
            for iOM in range(nOM):
                en_pour_chaque_OM = StringVar()
                lab_affichage_nouveau_en = Label(lab_nouvelle_energie, textvariable=en_pour_chaque_OM)
                en_pour_chaque_OM.set("\u03b5 " + str('{:3d}'.format(iOM + 1)) + " = \u03b1 + " +
                                      str('{:8.5f}'.format(E[iOM])) + " \u03b2")
                lab_affichage_nouveau_en.grid(row=row_en_pour_chaque_OM, column=1)
                row_en_pour_chaque_OM = row_en_pour_chaque_OM + 1
            en_total = StringVar()
            lab_affichage_nouveau_en_total = Label(lab_nouvelle_energie, textvariable=en_total)
            en_total.set(
                "\n\u03b5 total = " + str(n_electron_total) + " \u03b1 + " + str(
                    '{:.5f}'.format(sum(E_des_OM))) + " \u03b2")
            lab_affichage_nouveau_en_total.grid(row=row_en_pour_chaque_OM + 1, column=1)


        def calcul_des_en():
            ecriture_matrix_modifier()
            affichage_nouveau_en()



# Configuration d'objets graphiques
    ################    sp_nom_du_fichier.configure(textvariable=titre)
        sp_atome_x.configure(from_=1, to=taille_matrix, selectbackground="grey", justify=RIGHT)
        sp_atome_y.configure(from_=1, to=taille_matrix, selectbackground="grey", justify=RIGHT)
        lab_titre_spinbox.configure(justify=LEFT)
        bo_liaison_choisi.configure(text="ok", command=change_hamilton)
        bo_lancer_calcul_en.configure(text="Calculer les en", command=calcul_des_en)
        scroll_vertical.configure(command=(('scroll', -1, 'units'), ('scroll', 1, 'units')))



####Configurations de grille####
###Configuration de grille de fenetre
        fenetre.rowconfigure(1, weight=0)
        fenetre.rowconfigure(2, pad=20, weight=0)
        fenetre.rowconfigure(3, weight=1)
        fenetre.rowconfigure(4, weight=0)
        fenetre.rowconfigure(5, weight=0)

        fenetre.columnconfigure(1, weight=1)
        fenetre.columnconfigure(2, pad=10, weight=0)
        fenetre.columnconfigure(3, weight=0)
###Configuration de grille de lab_nom_du_fichier
        lab_nom_du_fichier.rowconfigure(1, weight=1)
        lab_nom_du_fichier.rowconfigure(2, weight=1)
        lab_nom_du_fichier.rowconfigure(3, pad=40, weight=0)
        lab_nom_du_fichier.rowconfigure(4, weight=1)

        lab_nom_du_fichier.columnconfigure(1, weight=1)
        lab_nom_du_fichier.columnconfigure(2, weight=1)
        lab_nom_du_fichier.columnconfigure(3, weight=0)
        lab_nom_du_fichier.columnconfigure(4, weight=0)
        lab_nom_du_fichier.columnconfigure(5, weight=1)
        lab_nom_du_fichier.columnconfigure(6, weight=1)

###Configuration de grille de lab_spinbox
        lab_spinbox.rowconfigure(1, weight=1)
        lab_spinbox.rowconfigure(2, weight=1)
        lab_spinbox.rowconfigure(3, weight=1)
        lab_spinbox.columnconfigure(1, weight=1)

####Creation d'objet graphique####
###Creation objet graphique dans fenetre
# taille grille dans fenetre      row = 5     et      column = 3
    ############    lab_titre.grid(row=1, column=1, columnspan=2, sticky=N)
        lab_espace_vide_apres_titre.grid(row=2, column=1)
        lab_nom_du_fichier.grid(row=3, column=1)
        lab_espace_vide_horizontal_avant_scroll.grid(row=4, column=1, columnspan=2)
        lab_espace_vide_vertical_avant_scroll.grid(row=1, column=2, rowspan=3)
        scroll_horizontal.grid(row=5, column=1, columnspan=2, sticky=S + EW)
        scroll_vertical.grid(row=1, column=3, rowspan=5, sticky=NS)
    ###########    sp_nom_du_fichier.grid()

###Creation d'objet graphique dans lab_nom_fichier
# taille grelle dans lab_nom_fichier     row = 4      et column = 6
        lab_numero_atome_ligne.grid(row=1, column=2, sticky=SW)
        lab_numero_atome_colone.grid(row=2, column=1, sticky=NE)
        lab_hamilton.grid(row=2, column=2, sticky=NW)
        lab_espace_vide_avant_en.grid(row=3, column=1, columnspan=6, sticky=N)
        lab_energie.grid(row=4, column=2)
        lab_nouvelle_energie.grid(row=4, column=5)
        lab_nouveau_hamilton.grid(row=2, column=5, sticky=NE)
        lab_numero_atome_ligne_nouveau_hamilton.grid(row=1, column=5, sticky=SE)
        lab_numero_atome_colone_nouveau_hamilton.grid(row=2, column=6, sticky=NW)
        lab_spinbox.grid(row=2, column=3, columnspan=1, sticky=E)
        lab_titre_spinbox.grid(row=2, column=4, sticky=W)
        bo_lancer_calcul_en.grid(row=4, column=3, sticky=E)

# taille grille dans lab_affichage_hamilton      row = n in taille_matrix       et     column =  m in taille_matrix
# taille grille dans lab_numerotation_atome_colone       row = 1     et  column = m in taille_matrix
# taille grille dans lab_numerotation_atome_ligne    row = n in taille_matrix    et      column = 1
# taille grille dans lab_affichage_nouveau_hamilton  row = n in taille_matrix    et  column = m in taille_matrix
# taille grille dans lab_numerotation_atome_colone_nouveau_hamilton       row = m in taille_matrix     et  column = 1
# taille grille dans lab_numerotation_atome_ligne_nouveau_hamilton    row = 1    et      column = n in taille_matrix

####Creation d'objets graphiques dans lab_spinbox
# taille grille dans lab_spinbox     row = 3     et     column = 1
        sp_atome_x.grid(row=1, column=1, sticky=E)
        sp_atome_y.grid(row=2, column=1, sticky=E)
        bo_liaison_choisi.grid(row=3, column=1, sticky=E)


#Execution du gui
        def main():
            affichage_hamilton(nom_du_fichier)
            affichage_en(nom_du_fichier)

        main()
        mainloop()

affichage_noms_fichiers()
LA_fonction()
