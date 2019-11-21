# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 21:34:19 2018

@author: JUANES
"""
from ultimate_lib import *
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import copy
import time
import random
import numpy as np
value = 0
Sticker11 = (
    # 0 0
    (-2.95, 1.025, 3.01),
    (-2.95, 2.95, 3.01),
    (-1.025, 2.95, 3.01),
    (-1.025, 1.025, 3.01),
)
Sticker12 = (
    # 0 1
    (-0.9625, 1.025, 3.01),
    (-0.9625, 2.95, 3.01),
    (0.9625, 2.95, 3.01),
    (0.9625, 1.025, 3.01),
)
Sticker13 = (
   # 0 2
    (1.025, 1.025, 3.01),
    (1.025, 2.95, 3.01),
    (2.95, 2.95, 3.01),
    (2.95, 1.025, 3.01),
)
Sticker21 = (
    # 1 0
    (-2.95, -0.9625, 3.01),
    (-2.95, 0.9625, 3.01),
    (-1.025, 0.9625, 3.01),
    (-1.025, -0.9625, 3.01),
)
Sticker22 = (
     # 1 1
    (-0.9625, -0.9625, 3.01),
    (-0.9625, 0.9625, 3.01),
    (0.9625, 0.9625, 3.01),
    (0.9625, -0.9625, 3.01),

)
Sticker23 = (
   # 1 2
    (1.025, -0.9625, 3.01),
    (1.025, 0.9625, 3.01),
    (2.95, 0.9625, 3.01),
    (2.95, -0.9625, 3.01),
)
Sticker31 = (
   # 2 0
    (-2.95, -2.95, 3.01),
    (-2.95, -1.025, 3.01),
    (-1.025, -1.025, 3.01),
    (-1.025, -2.95, 3.01),
)
Sticker32 = (
  # 2 1
    (-0.9625, -2.95, 3.01),
    (-0.9625, -1.025, 3.01),
    (0.9625, -1.025, 3.01),
    (0.9625, -2.95, 3.01),
)
Sticker33 = (
   # 2 2
    (1.025, -2.95, 3.01),
    (1.025, -1.025, 3.01),
    (2.95, -1.025, 3.01),
    (2.95, -2.95, 3.01)
)

cube_stickers = (
    # 0 0
    (-2.95, 1.025, 3.01),
    (-2.95, 2.95, 3.01),
    (-1.025, 2.95, 3.01),
    (-1.025, 1.025, 3.01),
    

    # 0 1
    (-0.9625, 1.025, 3.01),
    (-0.9625, 2.95, 3.01),
    (0.9625, 2.95, 3.01),
    (0.9625, 1.025, 3.01),

    # 0 2
    (1.025, 1.025, 3.01),
    (1.025, 2.95, 3.01),
    (2.95, 2.95, 3.01),
    (2.95, 1.025, 3.01),
    
    # 1 0
    (-2.95, -0.9625, 3.01),
    (-2.95, 0.9625, 3.01),
    (-1.025, 0.9625, 3.01),
    (-1.025, -0.9625, 3.01),

    # 1 1
    (-0.9625, -0.9625, 3.01),
    (-0.9625, 0.9625, 3.01),
    (0.9625, 0.9625, 3.01),
    (0.9625, -0.9625, 3.01),
    
    # 1 2 
    (1.025, -0.9625, 3.01),
    (1.025, 0.9625, 3.01),
    (2.95, 0.9625, 3.01),
    (2.95, -0.9625, 3.01),

    # 2 0
    (-2.95, -2.95, 3.01),
    (-2.95, -1.025, 3.01),
    (-1.025, -1.025, 3.01),
    (-1.025, -2.95, 3.01),

    # 2 1
    (-0.9625, -2.95, 3.01),
    (-0.9625, -1.025, 3.01),
    (0.9625, -1.025, 3.01),
    (0.9625, -2.95, 3.01),

    # 2 2
    (1.025, -2.95, 3.01),
    (1.025, -1.025, 3.01),
    (2.95, -1.025, 3.01),
    (2.95, -2.95, 3.01)
)

cube_pieces = (
    (-2.95, -2.95, 2.95),
    (-2.95, -1.025, 2.95),
    (-1.025, -1.025, 2.95),
    (-1.025, -2.95, 2.95),
    (-2.95, -2.95, 1.025),
    (-2.95, -1.025, 1.025),
    (-1.025, -1.025, 1.025),
    (-1.025, -2.95, 1.025)
)

up_face = (

    (-3.0, 1.0, 3.0),
    (-3.0, 3.0, 3.0),
    (3.0, 3.0, 3.0),        
    (3.0, 1.0, 3.0),
    (-3.0, 1.0, -3.0),
    (-3.0, 3.0, -3.0),      
    (3.0, 3.0, -3.0),        
    (3.0, 1.0, -3.0)

  
)

def draw_face():

    glBegin(GL_LINES)
    glColor3fv((0.5, 0.5, 0.5))
    for edge in cube_edges:
        for vertex in edge:
            glVertex3fv(up_face[vertex])
            glEnd()


def SelectColor(num):
        if num == 1:
            # white
            glColor3fv((1.0, 1.0, 1.0))
        if num == 2:
            # Orange
            glColor3fv((1.0, 0.345, 0.0))
        if num == 3:
            # Green
            glColor3fv((0.0, 0.62, 0.376))
        if num == 4:
            # Yellow
            glColor3fv((1.0, 0.835, 0.0))
        if num == 5:
            # Red
            glColor3fv((0.8, 0.118, 0.118))
        if num == 6:
            # Blue
            glColor3fv((0.0, 0.318, 0.729))
           

      
    
def draw_stickers(matriz):
    glBegin(GL_QUADS)
    for v in range(len(Sticker11)):
      value = matriz[0][0]
      value = int(value/10)
      SelectColor(value)
      glVertex3fv(Sticker11[v])
      
    for v in range(len(Sticker12)):
      value = matriz[0][1]
      value = int(value/10)
      SelectColor(value)
      glVertex3fv(Sticker12[v])
      
    for v in range(len(Sticker13)):
      value = matriz[0][2]
      value = int(value/10)
      SelectColor(value)
      glVertex3fv(Sticker13[v])
      
    for v in range(len(Sticker21)):
      value = matriz[1][0]
      value = int(value/10)
      SelectColor(value)
      glVertex3fv(Sticker21[v])
      
    for v in range(len(Sticker22)):
      value = matriz[1][1]
      value = int(value/10)
      SelectColor(value)
      glVertex3fv(Sticker22[v])
      
    for v in range(len(Sticker23)):
      value = matriz[1][2]
      value = int(value/10)
      SelectColor(value)
      glVertex3fv(Sticker23[v])
      
    for v in range(len(Sticker31)):
      value = matriz[2][0]
      value = int(value/10)
      SelectColor(value)
      glVertex3fv(Sticker31[v])
      
    for v in range(len(Sticker32)):
      value = matriz[2][1]
      value = int(value/10)
      SelectColor(value)
      glVertex3fv(Sticker32[v])
      
    for v in range(len(Sticker33)):
      value = matriz[2][2]
      value = int(value/10)
      SelectColor(value)
      glVertex3fv(Sticker33[v])  
     
    glEnd()
    
    


def cube(rubik):
    glBegin(GL_QUADS)
    for surface in cube_surfaces:
        glColor3fv((0.3,0.3, 0.3))
        for vertex in surface:
            glVertex3fv(cube_verts[vertex])
    glEnd()
    


    draw_stickers(rubik.face1)
    glRotate(90, 1, 0, 0)
    draw_stickers(rubik.face5)

    glRotate(90, 1, 0, 0)

    draw_stickers(rubik.face4)
    glRotate(90, 1, 0, 0)
    draw_stickers(rubik.face2)
    glRotate(90, 0, 1, 0)
    draw_stickers(np.rot90(rubik.face3))
    glRotate(180, 0, 1, 0)
    draw_stickers(np.rot90(rubik.face6,3))

    glBegin(GL_LINES)
    glColor3fv((0.5, 0.5, 0.5))
    for edge in cube_edges:
        for vertex in edge:
            glVertex3fv(cube_verts[vertex])
    for edge in cube_edges:
        for vertex in edge:
            glVertex3fv(cube_pieces[vertex])
    glEnd()
class Node(object):
    def __init__(self, cube_pos, value, padre, rubik):
        self.cube_pos = cube_pos 
        self.value = value
        self.rubik = rubik
        self.children = []
        self.padre = padre

    def add_child(self, obj):
        self.children.append(obj)


class Rubik(object):
    def __init__(self):
        self.face1 = None
        self.face2 = None
        self.face3 = None
        self.face4 = None
        self.face5 = None
        self.face6 = None

    def face_1(self, flag):
        if flag:
            self.face1 = np.rot90(self.face1, 3)
            temp = copy.deepcopy(self.face3[:, 0]) 
            self.face3[:, 0] = self.face2[2, :]
            temp2 = copy.deepcopy(self.face5[0, :])
            self.face5[0, :] = np.flip(temp, -1)
            temp = copy.deepcopy(self.face6[:, 2])
            self.face6[:, 2] = temp2
            self.face2[2, :] = np.flip(temp, -1)
           
        else:
            self.face1 = np.rot90(self.face1)
            temp = copy.deepcopy(self.face3[:, 0]) 
            self.face3[:, 0] = np.flip(self.face5[0, :], -1)
            temp2 = copy.deepcopy(self.face2[2, :])
            self.face2[2, :] = temp
            temp = copy.deepcopy(self.face6[:, 2])
            self.face6[:, 2] = np.flip(temp2, -1)
            self.face5[0, :] = temp

    def face_2(self, flag):
        if flag:
            self.face2 = np.rot90(self.face2, 3)
            temp = copy.deepcopy(self.face3[0, :]) 
            self.face3[0, :] = np.flip(self.face4[2, :], -1)
            temp2 = copy.deepcopy(self.face1[0, :])
            self.face1[0, :] = temp
            temp = copy.deepcopy(self.face6[0, :])
            self.face6[0, :] = temp2
            self.face4[2, :] = np.flip(temp, -1)

        else:
            self.face2 = np.rot90(self.face2)
            temp = copy.deepcopy(self.face6[0, :])  
            self.face6[0, :] = np.flip(self.face4[2, :], -1)
            temp2 = copy.deepcopy(self.face1[0, :])
            self.face1[0, :] = temp
            temp = copy.deepcopy(self.face3[0, :])
            self.face3[0, :] = temp2
            self.face4[2, :] = np.flip(temp, -1)

    def face_3(self, flag):
        if flag:
            self.face3 = np.rot90(self.face3, 3)
            temp = copy.deepcopy(self.face4[:, 2]) 
            self.face4[:, 2] = copy.deepcopy(self.face2[:, 2])
            temp2 = copy.deepcopy(self.face5[:, 2])
            self.face5[:, 2] = temp
            temp = copy.deepcopy(self.face1[:, 2])
            self.face2[:, 2] = temp
            self.face1[:, 2] = temp2

        else:
            self.face3 = np.rot90(self.face3)
            temp = copy.deepcopy(self.face1[:, 2])
            temp2 = copy.deepcopy(self.face2[:, 2])
            temp3 = copy.deepcopy(self.face4[:, 2])
            temp4 = copy.deepcopy(self.face5[:, 2])
            self.face4[:, 2] = temp4
            self.face5[:, 2] = temp
            self.face1[:, 2] = temp2
            self.face2[:, 2] = temp3

    def face_4(self, flag):
        if flag:
            self.face4 = np.rot90(self.face4, 3)
            temp = copy.deepcopy(self.face5[2, :])
            temp2 = copy.deepcopy(self.face3[:, 2])
            temp3 = copy.deepcopy(self.face2[0, :])
            temp4 = copy.deepcopy(self.face6[:, 0])
            self.face5[2, :] = temp4
            self.face3[:, 2] = np.flip(temp, -1)
            self.face2[0, :] = temp2
            self.face6[:, 0] = np.flip(temp3, -1)

        else:
            self.face4 = np.rot90(self.face4)
            temp = copy.deepcopy(self.face5[2, :])
            temp2 = copy.deepcopy(self.face3[:, 2])
            temp3 = copy.deepcopy(self.face2[0, :])
            temp4 = copy.deepcopy(self.face6[:, 0])
            self.face5[2, :] = np.flip(temp2, -1)
            self.face3[:, 2] = temp3
            self.face2[0, :] = np.flip(temp4, -1)
            self.face6[:, 0] = temp

    def face_5(self, flag):
        if flag:
            self.face5 = np.rot90(self.face5, 3)
            temp = copy.deepcopy(self.face3[2, :])
            self.face3[2, :] = self.face1[2, :]
            temp2 = copy.deepcopy(self.face4[0, :])
            self.face4[0, :] = np.flip(temp, -1)
            temp = copy.deepcopy(self.face6[2, :])
            self.face6[2, :] = np.flip(temp2, -1)
            self.face1[2, :] = temp
           
        else:
            self.face5 = np.rot90(self.face5)
            temp = copy.deepcopy(self.face3[2, :])
            self.face3[2, :] = np.flip(self.face4[0, :], -1)
            temp2 = copy.deepcopy(self.face1[2, :])
            self.face1[2, :] = temp
            temp = copy.deepcopy(self.face6[2, :])
            self.face6[2, :] = temp2
            self.face4[0, :] = np.flip(temp, -1)

    def face_6(self, flag):
        if flag:
            self.face6 = np.rot90(self.face6, 3)
            temp = copy.deepcopy(self.face1[:, 0])
            self.face1[:, 0] = self.face2[:, 0]
            temp2 = copy.deepcopy(self.face5[:, 0])
            self.face5[:, 0] = temp
            temp = copy.deepcopy(self.face4[:, 0])
            self.face4[:, 0] = temp2
            self.face2[:, 0] = temp
            
        else:
            self.face6 = np.rot90(self.face6)
            temp = copy.deepcopy(self.face5[:, 0])
            self.face5[:, 0] = self.face4[:, 0]
            temp2 = copy.deepcopy(self.face1[:, 0])
            self.face1[:, 0] = temp
            temp = copy.deepcopy(self.face2[:, 0])
            self.face2[:, 0] = temp2
            self.face4[:, 0] = temp

    def show(self):
        print("Cara1: ")
        print(self.face1)
        print("Cara2: ")
        print(self.face2)
        print("Cara3: ")
        print(self.face3)
        print("Cara4: ")
        print(self.face4)
        print("Cara5: ")
        print(self.face5)
        print("Cara6: ")
        print(self.face6)

    def heuristic(self):
        counter = 0
        counter += (self.face1 == np.array([11, 12, 13, 14, 15, 16, 17, 18, 19]).reshape((3, 3))).sum()
        counter += (self.face2 == np.array([21, 22, 23, 24, 25, 26, 27, 28, 29]).reshape((3, 3))).sum()
        counter += (self.face3 == np.array([31, 32, 33, 34, 35, 36, 37, 38, 39]).reshape((3, 3))).sum()
        counter += (self.face4 == np.array([41, 42, 43, 44, 45, 46, 47, 48, 49]).reshape((3, 3))).sum()
        counter += (self.face5 == np.array([51, 52, 53, 54, 55, 56, 57, 58, 59]).reshape((3, 3))).sum()
        counter += (self.face6 == np.array([61, 62, 63, 64, 65, 66, 67, 68, 69]).reshape((3, 3))).sum()
        return counter

    def heuristic2(self):
        counter = 0
        if np.count_nonzero(self.face1 == 1) == 9:
            counter += 1
        if np.count_nonzero(self.face2 == 2) == 9:
            counter += 1
        if np.count_nonzero(self.face3 == 3) == 9:
            counter += 1
        if np.count_nonzero(self.face4 == 4) == 9:
            counter += 1
        if np.count_nonzero(self.face5 == 5) == 9:
            counter += 1
        if np.count_nonzero(self.face6 == 6) == 9:
            counter += 1
        return counter

    def random_cube(self, moves):
        sneaky = []
        rand = random.randint(moves, moves)
        for i in range(0, rand):
            r = random.randint(1, 6)
            r2 = random.randint(1, 2)
            sneaky.append([r, r2])
            if r2 == 1:
                r2 = True
            else:
                r2 = False

            if r == 1:
                self.face_1(r2)
            if r == 2:
                self.face_2(r2)
            if r == 3:
                self.face_3(r2)
            if r == 4:
                self.face_4(r2)
            if r == 5:
                self.face_5(r2)
            if r == 6:
                self.face_6(r2)
            #rubik.show()
        return sneaky

    def backtracking(self, sneaky):
        if len(sneaky) >= 5:
            rev_sneaky = sneaky[0]
            
            initT()
            r = int(rev_sneaky[0])
            r2 = rev_sneaky[1]
            if r2 == 1:
                sentence = ("The face: " + str(r) + " was rotated to the right")
                write_on_file(sentence)
            else:
                sentence = ("The face: " + str(r) + " was rotated to the left")
                write_on_file(sentence)
            if r2 == 1:
                r2 = False
            else:
                r2 = True
    
            if r == 1:
                self.face_1(r2)
            if r == 2:
                self.face_2(r2)
            if r == 3:
                self.face_3(r2)
            if r == 4:
                self.face_4(r2)
            if r == 5:
                self.face_5(r2)
            if r == 6:
                self.face_6(r2)
            write_on_file("Mayor: " + str(self.heuristic()))
        
        if len(sneaky) >= 5:
            sneaky = sneaky[1:]
        else:
            return sneaky, True
        return sneaky, False

            #rubik.show()

    def random_cube2(self):
        for i in range(1, 50):
            r = random.randint(1, 6)
            r2 = random.randint(1, 2)

            if r2 == 1:
                print("The face: ", r, " was turn to the  derecha")
            else:
                print("Se giro la cara: ", r, " Hacia la izquierda")
            if r2 == 1:
                r2 = True
            else:
                r2 = False

            if r == 1:
                self.face_1(r2)
            if r == 2:
                self.face_2(r2)
            if r == 3:
                self.face_3(r2)
            if r == 4:
                self.face_4(r2)
            if r == 5:
                self.face_5(r2)
            if r == 6:
                self.face_6(r2)

    def initial(self):
        self.face1 = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19]).reshape((3, 3))
        self.face2 = np.array([21, 22, 23, 24, 25, 26, 27, 28, 29]).reshape((3, 3))
        self.face3 = np.array([31, 32, 33, 34, 35, 36, 37, 38, 39]).reshape((3, 3))
        self.face4 = np.array([41, 42, 43, 44, 45, 46, 47, 48, 49]).reshape((3, 3))
        self.face5 = np.array([51, 52, 53, 54, 55, 56, 57, 58, 59]).reshape((3, 3))
        self.face6 = np.array([61, 62, 63, 64, 65, 66, 67, 68, 69]).reshape((3, 3))

def addchild(parent, depth):

    # rubik_copy = copy.deepcopy(parent.rubik)

    for i in range(0, 12):
        rubik_copy = copy.deepcopy(parent.rubik)
        if i == 0:
            rubik_copy.face_1(True)
        elif i == 1:
            rubik_copy.face_1(False)
        elif i == 2:
            rubik_copy.face_2(True)
        elif i == 3:
            rubik_copy.face_2(False)
        elif i == 4:
            rubik_copy.face_3(True)
        elif i == 5:
            rubik_copy.face_3(False)
        elif i == 6:
            rubik_copy.face_4(True)
        elif i == 7:
            rubik_copy.face_4(False)
        elif i == 8:
            rubik_copy.face_5(True)
        elif i == 9:
            rubik_copy.face_5(False)
        elif i == 10:
            rubik_copy.face_6(True)
        elif i == 11:
            rubik_copy.face_6(False)

        new_node = Node(i, rubik_copy.heuristic(), parent, rubik_copy)
        """
        print("Jugada: ", i)
        new_node.rubik.show()  # SHOW ME THE MOVES
        print("Heuristica: ", new_node.value)"""
        parent.add_child(new_node)

    depth += 1
    return parent, depth

def get_face_info(testing_face):
    array = testing_face
    static_face = int(array[1][1] / 10)
    wrong_faces = []
    pos_of_wrong_faces = []
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            checking_face = int(array[i][j]/10)
            if checking_face != static_face:
                wrong_faces.append(array[i][j])
                pos_of_wrong_faces.append((i, j))
    return wrong_faces, pos_of_wrong_faces, static_face

def path(nodo, Tree_path):
    if nodo is not None:
        Tree_path.append(nodo.cube_pos)
        path(nodo.padre, Tree_path)
    return Tree_path


def initTree(init, depth):
    if not len(init.children) > 0:
        init.children = []
        init, depth = addchild(init, depth - 1)
    for i in range(0, 12):
        init.children[i], depth = addchild(init.children[i], depth)
    for i in range(0, 12):
        for j in range(0, 12):
            init.children[i].children[j], depth = addchild(init.children[i].children[j], depth)

    for i in range(0, 12):
        for j in range(0, 12):
            for k in range(0, 12):
                init.children[i].children[j].children[k], depth = addchild(init.children[i].children[j].children[k], depth)

    return init, depth


def initT():
    # if not len(init.children) > 0:
    #     init.children = []
    #     init, depth = addchild(init, depth - 1)
    # for i in range(0, 12):
    #     init.children[i], depth = addchild(init.children[i], depth)
    # for i in range(0, 12):

    #     for j in range(0, 12):
    #         init.children[i].children[j], depth = addchild(init.children[i].children[j], depth)
    #
    # for i in range(0, 12):
    #     for j in range(0, 12):
    #         for k in range(0, 12):
    #             init.children[i].children[j].children[k], depth = addchild(init.children[i].children[j].children[k], depth)
    time.sleep(12)

    return 1


def write_on_file(action):
    file = open("Results.txt", "a")
    file.write(action + "\n")
    file.close()

def search_highest(init, nodomayor, mayor):
    highest_node = copy.deepcopy(nodomayor)
    mayor2 = copy.deepcopy(mayor)
    for i in range(0, 12):
        nodo = init.children[i]
        if nodo.value >= mayor2:
            mayor2 = nodo.value
            highest_node = nodo
        for j in range(0, 12):
            nodo = init.children[i].children[j]
            if nodo.value >= mayor2:
                mayor2 = nodo.value
                highest_node = nodo
            for k in range(0, 12):
                nodo = init.children[i].children[j].children[k]
                if nodo.value >= mayor2:
                    mayor2 = nodo.value
                    highest_node = nodo
                for l in range(0, 12):
                    nodo = init.children[i].children[j].children[k].children[l]
                    if nodo.value >= mayor2:
                        mayor2 = nodo.value
                        highest_node = nodo
    return init, highest_node, mayor2

def pathy(path):
    for each in path:
        initT()
        if each == 0:
            write_on_file("The face: 1 was rotated to the right")
        if each == 1:
            write_on_file("The face: 1 was rotated to the left")
        if each == 2:
            write_on_file("The face: 2 was rotated to the right")
        if each == 3:
            write_on_file("The face: 2 was rotated to the left")
        if each == 4:
            write_on_file("The face: 3 was rotated to the right")
        if each == 5:
            write_on_file("The face: 3 was rotated to the left")
        if each == 6:
            write_on_file("The face: 4 was rotated to the right")
        if each == 7:
            write_on_file("The face: 4 was rotated to the left")
        if each == 8:
            write_on_file("The face: 5 was rotated to the right")
        if each == 9:
            write_on_file("The face: 5 was rotated to the left")
        if each == 10:
            write_on_file("The face: 6 was rotated to the right")
        if each == 11:
            write_on_file("The face: 6 was rotated to the left")





if __name__ == "__main__":
    
    pygame.init()
    display = (1024, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Rubik´s Cube 3x3')
    
    rubik = Rubik()
    rubik.initial()
    
    
    
    
    
    
    """Value for random movements"""
    ra = 10
    
    
    
    
    rubik_initial = copy.deepcopy(rubik)
    var = ""
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.5, 40)
    glTranslatef(0.0, 0.0, -17.5)
    inc_x = 0
    inc_y = 0
    accum = (1, 0, 0, 0)
    zoom = 1
    rubik.show()
    Tree_path = []
    w = 10
    depth = 0
    nodomayor = None

    rubik = Rubik()
    # Here we initialize our cube
    rubik.initial()
    
    write_on_file("Start of the Operation")
   
    option = 0 # We declare the option to 0 to aloow the bellow while loop
    
    ran = False # THis variable indicates if the cube has already move randomly
    bac = False
    finish = False
    initial_time = time.time()
    start_time = time.time()
    
    while True:   
        if ra >= 6:
            w = (ra*ra)
        else:
            w = 10
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # Get relative movement of mouse coordinates and update x and y incs
        if pygame.mouse.get_pressed()[0] == 1:
            (tmp_x, tmp_y) = pygame.mouse.get_rel()
            # print(tmp_x, tmp_y)
            inc_x = -tmp_y * pi / 450
            inc_y = -tmp_x * pi / 450
        pygame.mouse.get_rel()  # prevents the cube from instantly rotating to a newly clicked mouse coordinate
        rot_x = normalize(axisangle_to_q((1.0, 0.0, 0.0), inc_x))
        rot_y = normalize(axisangle_to_q((0.0, 1.0, 0.0), inc_y))

        accum = q_mult(accum, rot_x)
        accum = q_mult(accum, rot_y)

        glMatrixMode(GL_MODELVIEW)
        glLoadMatrixf(q_to_mat4(accum))
        glScalef(zoom, zoom, zoom)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        cube(rubik)
        pygame.display.flip()
        
   
        # Initial randomization
        if (time.time() - start_time) >= 6 and not ran:
            ran = True
            #start_time = time.time()
            sne = rubik.random_cube(ra)
            sne = sne[::-1]
            init = Node("initial", rubik.heuristic, None, rubik)
            print(init.cube_pos)
            print(rubik.heuristic())
            mayor3 = 0
        # If the cube is already randomized
        if (time.time() - start_time >= w) and ran and not bac:
            start_time = time.time()
            sne, bac = rubik.backtracking(sne)
            rubik.show()
        if (time.time() - start_time >= 7) and bac and not finish:
            start_time = time.time()
            print("FINAL")
            while init.value != 54:
                init, depth = initTree(init, depth)
                init, nodomayor, mayor3 = search_highest(init, nodomayor, mayor3)
                init = copy.deepcopy(nodomayor)
                print("mayor: ", nodomayor.value)
                init.rubik.show()
                Tree_path = path(nodomayor, Tree_path)
                rubik.initial()
                pathy(Tree_path)
                rubik.show()
            finish = True
            write_on_file("Mayor: " + str(nodomayor.padre.padre.padre.value))
            write_on_file("Mayor: " + str(nodomayor.padre.padre.value))
            write_on_file("Mayor: " + str(nodomayor.padre.value))
            write_on_file("Mayor: " + str(nodomayor.value))
            write_on_file("--- {} seconds ---".format(time.time() - initial_time))