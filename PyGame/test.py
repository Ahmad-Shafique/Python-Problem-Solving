
import os
import sys
import math
import pygame
import time


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
    funcList = []
    paramsList = []
    characterPosition=[0,200]
    characterSelected = 1
    success =True

def ConvertYCoordinate(y):
    return GlobalVariables.screen_size[1]-y

def ImageBlitFunction(imagePath,coordinates=(0,ConvertYCoordinate(100))):
    image = pygame.image.load(imagePath).convert()
    GlobalVariables.main_screen.blit(image,coordinates)


def StoreFunctionAndDraw(function,*params):
    GlobalVariables.funcList.append(function)
    GlobalVariables.paramsList.append(list(params))
    function(*params)
    pygame.display.update()

def DrawEntireStack():
    functionList=GlobalVariables.funcList
    paramsList = GlobalVariables.paramsList
    for function in functionList:
        index = functionList.index(function)
        function(*paramsList[index])
    pygame.display.update()

def WriteOnScreen(string,coords=None):
    try:
        if GlobalVariables.main_screen is None: print('Main screen not found')
        elif not pygame.font: print('Warning! Font not available!!!')
        else:
            font = pygame.font.Font(None, 36)
            text = font.render(string, 1, red)
            if coords is None:
                coords = text.get_rect(centerx=GlobalVariables.main_screen.get_width()/2)
            GlobalVariables.main_screen.blit(text, coords)
            pygame.display.update()
    except:
        print('Unable to print out the text for some reason ...')

def DrawBackground():
    pygame.draw.rect(main_screen,black,(0,ConvertYCoordinate(100),800,ConvertYCoordinate(0)))
    pygame.draw.rect(main_screen,blue,(600,ConvertYCoordinate(100),200,ConvertYCoordinate(50)))
    pygame.display.update()

def ChangeCharacter():
    GlobalVariables.characterSelected = -GlobalVariables.characterSelected

def DrawLevelOne():
    GlobalVariables.main_screen.fill(white)
    DrawBackground()
    if GlobalVariables.characterSelected == 1:
        ImageBlitFunction('m1.png',(GlobalVariables.characterPosition[0],ConvertYCoordinate(GlobalVariables.characterPosition[1])))
    else:
        ImageBlitFunction('m2.png',(GlobalVariables.characterPosition[0],ConvertYCoordinate(GlobalVariables.characterPosition[1])))
    pygame.display.update()

def LevelOneIntro():
    DrawLevelOne()
    WriteOnScreen('You are Nathan the Ninja',(200,100))
    time.sleep(3)
    DrawLevelOne()
    WriteOnScreen('You are on your path on discovery of secrets of the universe today...',(0,100))
    time.sleep(3)
    DrawLevelOne()
    WriteOnScreen('Well, to your brain capacity anyway...',(100,100))
    time.sleep(3)
    return

def LevelOneEnding():
    DrawLevelOne()
    WriteOnScreen('Nathan needs to cross the water body',(200,100))
    time.sleep(3)
    DrawLevelOne()
    WriteOnScreen('He just realised that for every move',(100,100))
    WriteOnScreen('He had to calculate amount of energy and vector  needed',(0,150))
    WriteOnScreen('And apply as much',(200,200))
    time.sleep(3)
    return

def LevelOne():
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: return
            elif event.type == pygame.KEYDOWN and (event.key == ord('a') or event.key == ord('A') or event.key == pygame.K_LEFT):
                if GlobalVariables.characterPosition[0] >= 2:
                    GlobalVariables.characterPosition[0] -= 20
                    ChangeCharacter()
            elif event.type == pygame.KEYDOWN and (event.key == ord('d') or event.key == ord('D') or event.key == pygame.K_RIGHT):
                if GlobalVariables.characterPosition[0] >=550:
                    GlobalVariables.success = True
                    GlobalVariables.current_level = 2
                    return
                else:
                    GlobalVariables.characterPosition[0] += 20
                    ChangeCharacter()
            
        DrawLevelOne()
    






os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
main_screen = pygame.display.set_mode(GlobalVariables.screen_size)
pygame.display.set_caption(GlobalVariables.caption)
main_screen.fill(white)
GlobalVariables.main_screen = main_screen
clock = pygame.time.Clock()


#WriteOnScreen('Hello World!!!',(25,100))

#pygame.draw.circle(main_screen,red,(50,200),10)
#ImageBlitFunction('main.jpg')
print(ConvertYCoordinate(0))

while GlobalVariables.success == True:
    if GlobalVariables.current_level == 1:
        LevelOneIntro()
        LevelOne()
        LevelOneEnding()
        GlobalVariables.success = False
    elif GlobalVariables.current_level == 2:
        LevelTwo = None
        GlobalVariables.success = False
    elif GlobalVariables.current_level == 3:
        LevelThree = None
        GlobalVariables.success = False

pygame.display.update()


