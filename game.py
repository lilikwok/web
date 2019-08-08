# -*- coding: utf-8 -*-

import pygame 
from random import randint 
from math import sqrt 
from pygame.locals import *  
import time 

class Color():
     
    RED=(255,0,0)
    GREEN=(255,255,0)
    BULE=(0,0,255)
    #随机颜色
    @staticmethod
    def randintColor():
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        return r,g,b
#球类
class Ball(object):
    #初始化球类
    def __init__(self,x,y,sx,sy,radius,color=Color.RED):
        self.x=x #x
        self.y=y #y
        self.sx=sx #每次移动的x
        self.sy=sy #每次移动的y
        self.radius=radius #半径
        self.color=color #颜色
        self.alive=True  #是否存活球
        self.eat_number = 0 # 吃的数量
        
    #移动
    def move(self,screen):
            self.x += self.sx
            self.y +=self.sy
            # x轴
            if self.x - self.radius <= 0 or \
                    self.x + self.radius >= screen.get_width():
                    if self.x-self.radius<=0:
                        self.x+=self.radius-self.x+1
                    else:
                        self.x += -(self.x+self.radius-screen.get_width()+1)
                    self.sx = -self.sx
            #y轴
            if self.y - self.radius <= 0 or \
                    self.y + self.radius >= screen.get_height():
                if self.y - self.radius <= 0:
                    self.y += self.radius-self.y+1
                else:
                    self.y +=-(self.y+self.radius-screen.get_height()+1)
                self.sy = -self.sy
 
 
 
    #吃掉
    def eat(self,screen,other):
        if self.alive and other.alive and self!=other:
            dx,dy = self.x-other.x,self.y-other.y
            distance = sqrt(dx**2 + dy**2)
            if distance<self.radius+other.radius and self.radius>other.radius:
                other.alive = False  
                #self.eat_number += 1
                #print(self.eat_number)
                self.radius = self.radius + int(other.radius*0.146)
                """
                
                """
                
    #绘图
    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius,0)



def main():
    # 定义装球的容器
    Balls = []
    eat_number = 0 
    #初始化导入 pygame模块
    pygame.init()
    #初始化窗口大小
    screen = pygame.display.set_mode((1024,768))
 
    #窗口标题
    pygame.display.set_caption("Lili's first DIY game")
    running = True
    #开启事件循环
    while running:
        #从消息队列中 获取消息并处理
        for e in pygame.event.get():
            if e.type ==pygame.QUIT:
                running = False
            if e.type==pygame.MOUSEBUTTONDOWN and e.button==1:
                # 获取鼠标点击的位置
                x,y = e.pos
                radius = randint(1,100)#随机大小
                sx,sy = randint(-10,10),randint(-10,10) #随机移动位置
                color = Color.randintColor()           
                ball = Ball(x,y,sx,sy,radius,color)

                #将球添加到容器
                Balls.append(ball)
        screen.fill((255,255,255))
        #取出容器的球
        for b in Balls:
            if b.alive:
                b.draw(screen)
            else:  
                Balls.remove(b)
                eat_number += 1
                print(eat_number) 
                show_text(screen,eat_number,2, 'Hey!')
                show_text(screen,eat_number,4, 'Stupid')
                show_text(screen,eat_number,7, 'Baby')
                show_text(screen,eat_number,13, u'七')
                show_text(screen,eat_number,19, u"夕")
                show_text(screen,eat_number,21, u"快")
                show_text(screen,eat_number,27, u"乐")
                show_text(screen,eat_number,32, u"纪念郭猪猪和肖胖胖")
                show_text(screen,eat_number,33,u"两周年半快乐")
                if eat_number == 34:
                    pygame.quit()
                    exit()         
        pygame.display.flip()
        pygame.time.delay(30) #每隔50毫秒刷新窗口的位置
        for b in Balls:
            b.move(screen)
            #检测有没有吃到其他球
            for b1 in Balls:
                b.eat(screen,b1)

                
def show_text(screen,eat_number,num, word):  
    if eat_number == num: 
        font = pygame.font.SysFont('microsoftyaheimicrosoftyaheiuibold',90)
        textSurface = font.render(word, True, (0,0,0))
        TextRect = textSurface.get_rect()
        TextRect.center = ((1024/2),(768/2))
        screen.blit(textSurface, TextRect)
                                
        pygame.display.update()
        time.sleep(1) 
        
 
if __name__ == '__main__':
   main()
