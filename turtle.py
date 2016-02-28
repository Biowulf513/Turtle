#! /usr/bin/env python
#  -*- coding: utf-8 -*-
class Turtle:
    def __init__(self, name='~'):
        self.name = raw_input('Введите имя Черепашки \n ') or '~'
        self.mapsize = 0
        self.map = []
        self.pos = [0,0]
        self.TestOk = 0
        self.DefaultSript()

    def DefaultSript(self):
        self.MapSize()
        self.CraftMap()
        self.MyPosition()
    def MapSize(self):
        Size=int(raw_input('Какого размера Анк-Морпорк?\n1.Маленький (5х5)\n2.Средний (7х7)\n3.Большой (9х9)\n')or '1')
        while self.TestOk != 1:
            if Size not in (1,2,3):
                print 'Не верные данные размера,\nВы ввели', Size
                Size=int(raw_input('Какого размера Анк-Морпорк?\n1.Маленький (5х5)\n2.Средний (7х7)\n3.Большой (9х9)\n')or '1')
            elif Size == 1:
                self.mapsize = 5
                self.TestOk = 1
            elif Size == 2:
                self.mapsize = 7
                self.TestOk = 1
            elif Size == 3:
                self.mapsize = 9
                self.TestOk = 1
    def CraftMap(self):
        create = 0
        for a in range(self.mapsize):
            while len(self.map) < self.mapsize:
                self.map.append([])
                for b in range(self.mapsize):
                    while len(self.map[create]) < self.mapsize:
                        self.map[create].append(' _')
                create += 1
    def MyPosition(self):
        i = 0
        for newposition in self.pos:
            self.pos[i] = len(self.map)//2
            i += 1
        self.TestOk = 0
    def Printmap(self):
        for a in self.map:
                print(''.join( a ))
    def TurtleGO(self):
        posNew=[0,0]
        self.map[self.pos[0]][self.pos[1]]=' _'
        posNew[1]=int(raw_input('Как далеко черепаха идёт по оси X?\n')or 0)
        posNew[0]=int(raw_input('Как далеко черепаха идёт по оси Y?\n')or 0)

        while self.TestOk != 1:
            if self.pos[1]+posNew[1] >= len(self.map) or self.pos[1]+posNew[1] < 0:
                print 'Слишком далеко, я упаду с края Анк-Морпорка'
                posNew[1]=int(raw_input('Как далеко черепаха идёт по оси X?\n')or 0)

            elif self.pos[0]-posNew[0] >= len(self.map) or self.pos[0]-posNew[0] < 0:
                print 'Слишком далеко, я упаду с края Анк-Морпорка'
                posNew[0]=int(raw_input('Как далеко черепаха идёт по оси Y?\n')or 0)

            else:
                self.TestOk = 1

        self.TestOk = 0
#        print posNew[1], posNew[0]
        self.pos[0]-=posNew[0]
        self.pos[1]+=posNew[1]
        self.map[self.pos[0]][self.pos[1]]=' '+self.name[0]
#        print self.pos[1], self.pos[0]
        self.Printmap()
    def Stat(self): # Болше инфы, богу инфы
        print self.name, self.pos[0], self.pos[1]
        print self.map

#class Slow(Turtle):

obj1 = Turtle()
#obj1.MapSize()
#obj1.CraftMap()
#obj1.MyPosition()
#obj1.stat()
#obj1.Printmap()
obj1.TurtleGO()
#print obj1.pos
#obj1.Stat()
#print obj1.map
#print obj1.create
print '\nshe the live!!!\nthe live!!!'