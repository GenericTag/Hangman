import pygame
import  os
import  math
import random
#Display
pygame.init()
WIDTH,HEIGHT = 800,500
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Stefan's Hangman!")

#Button var
RADIUS = 20 
GAP = 15
letters = [] 
startx = round((WIDTH-(RADIUS*2+GAP)*13)/2)#MAFS
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP)*(i % 13))# wtf this was complicated jesus 
    y = starty +((i // 13) * (GAP + RADIUS * 2))
    letters.append([x,y,chr(A + i),True])
#Fonts
LETTER_FONT = pygame.font.SysFont('comicsans',40)
WORD_FONT = pygame.font.SysFont('comicsans',60)
TITLE_FONT = pygame.font.SysFont('comicsans',70)
#Images
images = []
for i in range(7):
    image = pygame.image.load(os.path.join("images","hangman" + str(i) + ".png"))
    images.append(image)

#Variables
hangman_status = 0
words = ["DEVELOPER","PYGAME","POKEMON","BATMAN","AWESOME","PROGRAMMER","GAMERS","ACADEMY"]
word = random.choice(words)
guessed = []

#Color
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,128,0)
RED = (255,0,0)
PURPLE = (148,0,211)

#Game loop
FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
    win.fill(WHITE)
    
    # draw title
    text = TITLE_FONT.render("STEF'S HANGMAN",1,PURPLE)
    win.blit(text,(WIDTH/2 -text.get_width()/2,20))
    
    #draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word,1,BLACK)
    win.blit(text,(400,200))


    # draw buttons
    for letter in letters:
        x,y,ltr,visible = letter
        if visible:
            pygame.draw.circle(win,BLACK,(x,y),RADIUS,3)
            text = LETTER_FONT.render(ltr,1,BLACK)
            win.blit(text,(x-text.get_width()/2,y - text.get_height()/2))# MAFS

    win.blit(images[hangman_status],(150,100))
    pygame.display.update()  

def display_message (message,color):  
        pygame.time.delay(1000) 
        win.fill(WHITE)
        text = WORD_FONT.render(message,1,color)
        win.blit(text,(WIDTH/2 - text.get_width()/2,HEIGHT/2-text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(4000)
       

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            m_x,m_y = pygame.mouse.get_pos()
            for  letter in letters:
                x,y,ltr,visible = letter
                if visible:
                    dis = math.sqrt((x-m_x)**2 + (y-m_y)**2)#Pythogorus motherfucker
                    if dis < RADIUS:
                     letter[3]= False
                     guessed.append(ltr)
                     if ltr not in word:
                         hangman_status += 1
    draw()                       
    won = True                     
    for letter in word:
        if letter not in guessed:
            won = False
            break
    if won:
        display_message("WINNER!",GREEN)
        break
    
    if hangman_status == 6:
        display_message("YOU SUCK!",RED)
        break
pygame.quit()
