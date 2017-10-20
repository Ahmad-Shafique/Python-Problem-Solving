import os
import sys
import math
import pygame


red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)




class GlobalVariables:
    current_level = 1
    total_levels = 1
    screen_size = (800,600)
    caption = 'A mad race'


def WriteOnScreen(string,coords=None):
    try:
        if GlobalVariables.main_screen is None: print('Main screen not found')
        elif not pygame.font: print('Warning! Font not available!!!')
        else:
            font = pygame.font.Font(None, 36)
            text = font.render(string, 1, (10, 10, 10))
            if coords is None:
                coords = text.get_rect(centerx=GlobalVariables.main_screen.get_width()/2)
            GlobalVariables.main_screen.blit(text, coords)
            pygame.display.update()
    except:
        print('Unable to print out the text for some reason ...')


os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
main_screen = pygame.display.set_mode(GlobalVariables.screen_size)
pygame.display.set_caption(GlobalVariables.caption)
main_screen.fill(white)
GlobalVariables.main_screen = main_screen


WriteOnScreen('Hello World!!!',(25,100))
stackList = []
stackPosList =[]
testCPos = (50,200)
stackList.append(pygame.draw.circle(main_screen,red,testCPos,10))
pygame.display.update()
print(stackList)
testPos = [100,250]
while True:
    ttP = tuple(testPos)
    stackList.append(pygame.draw.circle(main_screen,blue,ttP,10))
    stackPosList.append(ttP)
    pygame.display.update()
    print(stackList)
    print(stackPosList)
    main_screen.fill(white)
    print('Filled screen with white color')
    for shape in stackList:
        #tp = shape.get_rect()
        testC = stackPosList[stackList.index(shape)]
        nMS = pygame.Surface(testC)
        stackList.append(nMS)
        stackPosList.append(testC)
        main_screen.blit(nMS,shape)
        print('printed this ... ')
        print(shape)
    pygame.display.update()
    testPos[0]+=20
    testPos[1]+=20
    stackList.pop()
    stackPosList.pop()
    input()
    
pygame.display.update()

