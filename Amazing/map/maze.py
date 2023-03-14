from random import *
import pygame

from Amazing.map.cells import Cells
from Amazing.map.GameZone import Zone
import Amazing.Const



jeu = Zone(400, 400).game_surface

class Maze:

    def __init__(self, surface, taille, side, fill):

        self.surface = Zone(side, side)
        self.laby = Cells(surface, taille)
        self.fill = fill
        self.taille = taille

        if self.fill:
            self.laby.fill()

    def gen_exploration(self):
        # Initialisation
        visited = list()
        depart = (randint(0, self.taille - 1), randint(0, self.taille - 1))
        pile = [depart]
        visited.append(depart)
        # Tant que la pile n'est pas vide
        while pile:
            continuer = True
            # La position devient la dernière cellule de la pile et la supprime de la pile
            position = pile.pop()
            voisins = list(self.laby.get_contiguous_cells(position))
            shuffle(voisins)
            i = 0
            while i < len(voisins) and continuer == True:
                # Vérifie si cette cellule a des voisins non visités
                if voisins[i] not in visited:
                    # On ajout le position à la pile
                    pile.append(position)
                    # On casse le mur
                    print(voisins)
                    self.laby.remove_wall(position, voisins[i])
                    # On ajoute la cellule à la pile et aux cellules visités
                    visited.append(voisins[i])
                    pile.append(voisins[i])
                    continuer = False
                i += 1
        return self.laby


    def afficher(self):

        for i in self.laby.cells.keys():
            s = pygame.Surface((self.surface.get_height()//self.taille, self.surface.get_width()//self.taille))
            s.fill(Amazing.Const.NONE)
            print(i[0])
            self.surface.game_surface.blit(s,
                ((i[0]*self.surface.get_height()//self.taille,
                  i[1]*self.surface.get_height()//self.taille)))
