import random as rd
import pygame
from playsound import playsound
import time

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_BACKSPACE,
    K_RETURN,
    KEYDOWN,
    QUIT,
)

SPEED = 30
lives = 5
points = 0

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BOTTOM_LIMIT = SCREEN_HEIGHT - 150

maxPointsFile = open('maxpoints.txt','r')
maxP = int(maxPointsFile.readline())
maxPointsFile.close()

pygame.init()

class CenteredText(pygame.sprite.Sprite):
    def __init__(self, text, size, color, width, height):
        # Call the parent class (Sprite) constructor  
        pygame.sprite.Sprite.__init__(self)
    
        self.font = pygame.font.SysFont("Arial", size)
        self.textSurf = self.font.render(text, 1, color)
        self.image = pygame.Surface((width, height))
        self.color = color
        self.width = self.textSurf.get_width()
        self.height = self.textSurf.get_height()
        self.centered = centered
        #self.image.blit(self.textSurf, [width/2 - self.width/2, height/2 - self.height/2])
        #self.image.blit(self.textSurf, [0, 0])
    
    def setText(self, text):
        self.textSurf = self.font.render(text, 1, self.color)
        textLen = len(text)
        print('textLen:' + str(textLen) + '<' + text + '>' + str(self.centered))
        #self.image.blit(self.textSurf, [10, 10])
        #screen.blit(mainText.textSurf, (0, 0))
        screen.blit(self.textSurf, (30, 10))

class Text(pygame.sprite.Sprite):
    def __init__(self, text, size, color, width, height, centered=False):
        # Call the parent class (Sprite) constructor  
        pygame.sprite.Sprite.__init__(self)
    
        self.font = pygame.font.SysFont("Arial", size)
        self.textSurf = self.font.render(text, 1, color)
        self.image = pygame.Surface((width, height))
        self.color = color
        self.width = self.textSurf.get_width()
        self.height = self.textSurf.get_height()
        self.centered = centered
        #self.image.blit(self.textSurf, [width/2 - self.width/2, height/2 - self.height/2])
        #self.image.blit(self.textSurf, [0, 0])
    
    def setText(self, text):
        self.textSurf = self.font.render(text, 1, self.color)
        textLen = len(text)
        print('textLen:' + str(textLen) + '<' + text + '>' + str(self.centered))
        #self.image.blit(self.textSurf, [10, 10])
        #screen.blit(mainText.textSurf, (0, 0))
        screen.blit(self.textSurf, (30, 10))

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

'''
textPos = 50

livesText  = Text('Lives :' + str(lives), 48, (20, 70, 120), 100, 100)
#mainText   = Text('Get Ready ! ', 100, ( 20, 70, 120), SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
mainTextSize = 100
mainText   = Text('Get Ready ! ', mainTextSize, ( 20, 70, 120), 0, 0, True)
pointsText = Text('0/' + str(maxP),      48, (120, 70, 120), SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

base_font = pygame.font.Font(None, 32)
user_text = ''

answerInputRect = pygame.Rect(200, BOTTOM_LIMIT + 5, 140, 32)
answerNumber = 0
i = 0
a = 0 
b = 0

def resetQuestion():
    a = int(rd.random() * 13)
    b = int(rd.random() * 13)
    return str(a) + ' x ' + str(b)

running = True
'''
intro = True

xfont = pygame.font.SysFont("Arial", 10)
xtextSurf = xfont.render('abc', 1, (20, 70, 120))

while intro:

    for event in pygame.event.get():   
        if event.type == pygame.QUIT or event.type == KEYDOWN:
            intro = False

    screen.fill((255, 255, 255))
      
    # render at position stated in arguments
    #screen.blit(text_surface, (answerInputRect.x+5, answerInputRect.y+5))
      
    # set width of textfield so that text cannot get
    # outside of user's text input
    # answerInputRect.w = max(100, text_surface.get_width()+10)
          
    screen.blit(xtextSurf, (20, 20))
    #screen.blit(livesText.textSurf, (20, 20))
    #screen.blit(mainText.textSurf, (SCREEN_WIDTH/2, textPos))
    #screen.blit(mainText.textSurf, (0, 0))
    #screen.blit(pointsText.textSurf, (SCREEN_WIDTH - 150, 20))
    pygame.display.flip()

'''
while running:

    if lives == 0:
        mainText.setText(' GAME OVER !!!')
        screen.blit(mainText.textSurf, (300, textPos))
        pygame.display.flip()
        time.sleep(3)

        print(' GAME OVER !!!')
        print(' Your final score was %s points.' % points)
        if points > maxP:
            print(' Congratulations, This is a NEW RECORD!!!!')
            maxPointsFile = open('maxpoints.txt', 'w')
            maxPointsFile.write(str(points))
        #playsound('Dead.wav')
        running = False
        pygame.quit()

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == KEYDOWN:
            # Check for backspace
            if event.key == K_BACKSPACE:
                user_text = user_text[:-1]
            elif event.key == K_RETURN and user_text != '':
                
                c = int(user_text)

                if c == (a * b):            
                    points += 1
                    pointsText.setText(str(points) + '/' +str(maxP))
                else:
                    print('Gotcha!. The answer was ' + str(a * b))
                    lives -= 1
                    livesText.setText('Lives: ' + str(lives))
                    playsound('resources/sounds/lose_a_live.wav')                
                user_text = ''
                mainText.setText(resetQuestion())
                textPos = 50
            elif event.unicode.isnumeric():
                user_text += event.unicode

    # Fill the background with white
    screen.fill((255, 255, 255))

    text_surface = base_font.render(user_text, True, (0, 0, 0))
      
    # render at position stated in arguments
    screen.blit(text_surface, (answerInputRect.x+5, answerInputRect.y+5))
      
    # set width of textfield so that text cannot get
    # outside of user's text input
    answerInputRect.w = max(100, text_surface.get_width()+10)
      

    i += 1
    if i % 100 == 0:
        textPos += SPEED
        if textPos > BOTTOM_LIMIT - mainText.height:
            mainText.setText(resetQuestion())
            textPos = 50
            print('Gotcha!. The answer was ' + str(a * b))
            lives -= 1
            livesText.setText('Lives: ' + str(lives))
    
    screen.blit(livesText.textSurf, (20, 20))
    #screen.blit(mainText.textSurf, (300, textPos))
    #screen.blit(mainText.textSurf, (SCREEN_WIDTH/2 - mainTextSize, textPos))
    screen.blit(pointsText.textSurf, (SCREEN_WIDTH - 150, 20))
    pygame.display.flip()
'''

pygame.quit()