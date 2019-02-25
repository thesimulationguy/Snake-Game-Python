#This won't work in Jupyter Notebook as Pygame is included.

import pygame
import random

pygame.init()
clock=pygame.time.Clock()
display=pygame.display.set_mode((500,500))
apple_pos=[random.randint(1,50)*10,random.randint(1,50)*10]
snake_pos=[[250,250],[240,250],[230,250]]
snake_head=[250,250]
score=0

def coll_with_apple(score):
    apple_pos=[random.randint(1,50)*10,random.randint(1,50)*10] #We want to display random location
    score+=1
    return apple_pos,score

def coll_with_bound(snake_head):
    if snake_head[0]>=500 or snake_head[0]<0 or snake_head[1]>=500 or snake_head[1]<0:
        return 1
    else:
        return 0

def coll_with_self(snake_pos):
    for i in snake_pos[1:]:
        if snake_pos[0]==i:
            return 1

def death(snake_pos):
    if coll_with_bound(snake_pos[0])==1 or coll_with_self(snake_pos)==1:
        return 1
    else:
        return 0

def generate(snake_head,snake_pos,apple_pos,but_dir,score):
    if but_dir==1:
        snake_head[0]+=10
    elif but_dir==0:
        snake_head[0]-=10
    elif but_dir==2:
        snake_head[1]+=10
    elif but_dir==3:
        snake_head[1]-=10
    else:
        pass

    if snake_head==apple_pos:
        apple_pos,score=coll_with_apple(score)
        snake_pos.insert(0,list(snake_head))
    else:
        snake_pos.insert(0,list(snake_head))
        snake_pos.pop()

    return snake_pos,apple_pos,score

def display_snake_apple(display,snake_pos,apple_pos):
    for i in snake_pos:
        pygame.draw.rect(display,(255,255,255),pygame.Rect(i[0],i[1],10,10))

    pygame.draw.rect(display,(255,0,0),pygame.Rect(apple_pos[0],apple_pos[1],10,10))

import sys
def play_game(snake_head,snake_pos,apple_pos,but_dir,score):
    crashed=False
    prev_but_dir=1

    while crashed is not True:
        for event in pygame.event.get():
            keys=pygame.key.get_pressed()
            if event.type==pygame.QUIT:
                sys.exit(0)

            if keys[pygame.K_LEFT] and prev_but_dir !=1:
                but_dir=0
            elif keys[pygame.K_RIGHT] and prev_but_dir !=0:
                but_dir=1
            elif keys[pygame.K_UP] and prev_but_dir !=2:
                but_dir=3
            elif keys[pygame.K_DOWN] and prev_but_dir !=3:
                but_dir=2
            else:
                but_dir=but_dir

        display.fill((0,0,0))
        display_snake_apple(display,snake_pos,apple_pos)

        snake_pos,apple_pos,score=generate(snake_head,snake_pos,apple_pos,but_dir,score)
        pygame.display.set_caption("SCORE:"+str(score))
        pygame.display.update()
        prev_but_dir=but_dir
        if death(snake_pos)==1:
            crashed=True
        clock.tick(20)
        pygame.display.update()
    return score

final_score=play_game(snake_head,snake_pos,apple_pos,1,score)

