# TODO sistemare check collisioni
from pipes import stepkinds
from random import random, randrange

import pygame
import numpy as np
import collections
import time

pygame.font.init()
pygame.mixer.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
win_surface = myfont.render('YOU WON', False, (255, 255, 255))
lose_surface = myfont.render('YOU LOST', False, (255, 255, 255))

RATE_TH = 5
WIDTH, HEIGHT = 640, 320
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")
FPS = 60


class frogger_game:
    def __init__(self):
        self.state_matrix = np.asarray([

            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

        ])
        self.frog_pos = (7, 13) 
        self.statemap = {}
        self.path = None
        #salva nel dizionario la matrice di partenza in funzione della posizione di partenza
        self.statemap [self.frog_pos] = self.state_matrix  

    # 0-Nothing, 1-left, 2-up, 3-right, 4-down
    def step(self, action):
        lose = False
        win = False
        r1 = collections.deque(self.state_matrix[1])
        r2 = collections.deque(self.state_matrix[2])
        r3 = collections.deque(self.state_matrix[3])
        r4 = collections.deque(self.state_matrix[4])
        r5 = collections.deque(self.state_matrix[5])
        r6 = collections.deque(self.state_matrix[6])
        r1.rotate(1)
        r2.rotate(1)
        r3.rotate(-1)
        r4.rotate(-1)
        r5.rotate(1)
        r6.rotate(1)
        
        r1 = list(r1)
        r2 = list(r2)
        r3 = list(r3)
        r4 = list(r4)
        r5 = list(r5)
        r6 = list(r6)
        self.state_matrix = np.asarray([self.state_matrix[0], r1, r2, r3, r4, r5, r6, self.state_matrix[7]])

        if (action == 1):
            self.frog_pos = (self.frog_pos[0], max(0, self.frog_pos[1] - 2))
        elif (action == 2):
            self.frog_pos = (max(0, self.frog_pos[0] - 1), self.frog_pos[1])
        elif (action == 3):
            self.frog_pos = (self.frog_pos[0], min(15, self.frog_pos[1] + 2))
        elif (action == 4):
            self.frog_pos = (min(7, self.frog_pos[0] + 1), self.frog_pos[1])

        if (self.state_matrix[self.frog_pos[0]][self.frog_pos[1]] != 0):
            lose = True
        if (action == 1):
            if (self.state_matrix[self.frog_pos[0]][self.frog_pos[1]+1] != 0):
                lose = True
        if (action == 3):
            if (self.state_matrix[self.frog_pos[0]][self.frog_pos[1]-1] != 0):
                lose = True
        if (self.frog_pos[0] == 0):
            win = True
        # print(action)
        return lose, win

    def simple_reactive(self):
        action = 0
        if (self.frog_pos[0] >= 4 and self.frog_pos[0] <= 5):
            if (self.state_matrix[self.frog_pos[0] - 1][self.frog_pos[1] + 1] == 0):
                action = 2
        else:
            if (self.state_matrix[self.frog_pos[0] - 1][self.frog_pos[1] - 1] == 0):
                action = 2

        return action


    
    def get_neighbors(self, v):
        #save state
        saved_state = (self.frog_pos, self.state_matrix)                
        adjac_lis = []                                                  
        for action in range (0, 5):                                     
            self.state_matrix = self.statemap[v]                       
            self.frog_pos = v                                           
            lose, win = self.step(action)                               
            if not lose:                                                
                adjac_lis.append((self.frog_pos, 1))                    
                if(self.frog_pos not in self.statemap):                 
                    self.mapAState(self.frog_pos, self.state_matrix)    
        # restore state
        self.frog_pos, self.state_matrix = saved_state                 
        return adjac_lis

    def h(self, v): #H
        distanceFromEndLane = v[0]-1
        return distanceFromEndLane

    def mapAState(self, position, matrix):
        self.statemap[position] = matrix

    def a_star_path_to_actions(self):
        if not self.path:
            self.path = self.A_star_agent()
            self.path.pop(0)

        if len(self.path) > 0:
            next_pose = self.path.pop(0)
            difference = np.array(next_pose) - np.array(self.frog_pos)

            if difference[0] < 0:
                return 2                # 2-up
            elif difference[0] > 0:
                return 4                # 4-down
            elif difference[1] > 0:
                return 3                #3-right
            elif difference[1] < 0:
                 return 1                # 1-left
        return 0               # 0-Nothing

    def A_star_agent(self):
        start = self.frog_pos                                    
        open_list = [start]                                      
        close_list = []                                          
        g = {}                                                       
        parents = {}                                             

        g[start] = 0                                             
        parents[start] = start                                   

        # finchè la lista open non è vuota

        while(len(open_list) > 0):                               
            n = None                                             
            # ricerca del nodo n in open con f = g + h minore
            for v in open_list:                          
                if( (n == None) or (g[v] + self.h(v) < g[n] + self.h(n)) ):
                    n = v
                        
            open_list.remove(n)                                            
            close_list.append(n)                                 


            # se n = None -> non è stato trovato un percorso
            if n == None:                                        
                print("Il path non esiste")
                return None
            

             # se n[0]=0 significa che il nodo si trova nella riga di goal (ovvero il lato opposto della strada) -> vittoria
            if(n[0] == 0):                                       
                path = []                                        
                #ricostruzione del path attraverso la lista parent
                while parents[n] != n:                           
                    path.append(n)                               
                    n = parents[n]                               

                path.append(start)                               
                path.reverse()                                   
                self.frog_pos = start
                print("Path trovato: ", path)
                return path



            for (m, weigth) in self.get_neighbors(n):            
                if m in close_list:                              
                    continue                                     
                g[m] = g[n] + weigth                             
                parents[m] = n                                   
                br = False                                        
                if m in open_list:                               
                    for node in open_list:                       
                        if g[m] > g[node]:                       
                            br = True                            
                if br == False:                                  
                    open_list.append(m)                          

        print("Il path non esiste")
        return None

def draw_window(game):
    WIN.fill((0, 0, 0))

    for r in range(len(game.state_matrix)):
        for c in range(len(game.state_matrix[r])):
            if (game.state_matrix[r][c] == 1):
                pygame.draw.rect(surface=WIN, color=(155, 155, 155), rect=(c * 40, r * 40, 40, 40), border_radius=3)
    pygame.draw.circle(surface=WIN, color=(0, 255, 0),
                       center=((game.frog_pos[1] * 40) + 16, (game.frog_pos[0] * 40) + 16), radius=16)
    pygame.display.update()


def draw_win():
    # WIN.fill((0, 0, 0))
    WIN.blit(win_surface, (220, 140))
    pygame.display.update()


def draw_lost():
    # WIN.fill((0, 0, 0))
    WIN.blit(lose_surface, (220, 140))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    game = frogger_game()
    rate = 0
    lost = False
    win = False
    while run:
        clock.tick(FPS)
        if ((not lost) and (not win)):
            draw_window(game)
        elif (lost):
            draw_window(game)
            draw_lost()

        else:
            draw_window(game)
            draw_win()

        if ((not lost) and (not win)):
            action = 0
#            action = game.simple_reactive()
            action = game.a_star_path_to_actions()
            '''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_LEFT):
                        action = 1
                    elif (event.key == pygame.K_UP):
                        action = 2
                    elif (event.key == pygame.K_RIGHT):
                        action = 3
                    elif (event.key == pygame.K_DOWN):
                        action = 4
                    elif (event.key == pygame.K_w):
                        action = 0
            '''
            lost, win = game.step(action)
            time.sleep(1)


main()
