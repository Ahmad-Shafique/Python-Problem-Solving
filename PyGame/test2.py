
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
            text = font.render(string, 1, (10, 10, 10))
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
                    print("Go to level one ")
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

LevelOne()
if GlobalVariables.success == True:
    print('Go to question')
    GlobalVariables.success = False
if GlobalVariables.success == True:
    LevelTwo = None
    GlobalVariables.success = False
if GlobalVariables.success == True:
    LevelThree = None
    GlobalVariables.success = False




pygame.display.update()


