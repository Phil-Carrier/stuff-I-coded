import pygame, sys, random, time
from pygame.locals import *
pygame.init()

screen_wdt = 1000
screen_hgt = 650
screen = pygame.display.set_mode((screen_wdt, screen_hgt))
centerX = 400
centerY = 100
clicked_value = 0
ComputerMoveImg = 0
result = "no one"

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

rockImg = pygame.image.load("rock.png")
rockImg = pygame.transform.scale_by(rockImg, 0.5)
rockX, rockY = 100, 50
paperImg = pygame.image.load("paper.png")
paperImg = pygame.transform.scale_by(paperImg, 0.333)
paperX, paperY = 125, 250
scissorsImg = pygame.image.load("scissors.png")
scissorsImg = pygame.transform.scale_by(scissorsImg, 0.5)
scissorsX, scissorsY = 100, 450

#defining
def ComputerMove(clickedImg):
   screen.fill (BLACK)
   screen.blit (clickedImg, (300, 150))
   ComputerMoveImg = random.randint (1,3)
   if ComputerMoveImg == 1:
       screen.blit (rockImg, (600, 150))
   elif ComputerMoveImg == 2:
       screen.blit (paperImg, (600,150))
   elif ComputerMoveImg == 3:
       screen.blit (scissorsImg, (600,150))
   time.sleep (0.1)
   pygame.display.update()
   if clickedImg == rockImg:
       if ComputerMoveImg == 1:
           result = "Tie: No one"
       elif ComputerMoveImg == 2: 
           result = "Paper beats Rock: The computer"
       elif ComputerMoveImg == 3:
           result = "Rock beats Scissors: You" 
   elif clickedImg == paperImg:
       if ComputerMoveImg == 1:
           result == "Paper beats Rock: You"
       elif ComputerMoveImg == 2: 
           result = "Tie: No one"
       elif ComputerMoveImg == 3:
           result = "Scissors beat Paper: The computer" 
   elif clickedImg == scissorsImg:
       if ComputerMoveImg == 1:
           result = "Rock beats Scissors: The computer"
       elif ComputerMoveImg == 2: 
           result = "Scissors beat Paper: You"
       elif ComputerMoveImg == 3:
           result = "Tie: No one" 
   fontObj = pygame.font.Font("Spoon SemiBold.ttf", 50)
   textSurfaceObj = fontObj.render(result + " won", True, GREEN, BLUE)
   textRectObj = textSurfaceObj.get_rect()
   textRectObj.center = (500, 150)
   screen.fill (BLACK)
   screen.blit(textSurfaceObj, textRectObj)
   time.sleep (1)
   pygame.display.update()
   time.sleep (1)
   pygame.display.quit()
   pygame.quit()
   sys.exit()
   
screen.fill(BLACK)
fontObj = pygame.font.Font("Spoon SemiBold.ttf", 50)
textSurfaceObj = fontObj.render("Let's play rock, paper, scissors!", True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (400, 150)
screen.blit(textSurfaceObj, textRectObj)
fontObj = pygame.font.Font("Spoon SemiBold.ttf", 20)
textSurfaceObj = fontObj.render("Click the rectangles to log your move in", True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (400, 350)
screen.blit(textSurfaceObj, textRectObj)
pygame.display.update()
time.sleep(2)

# Draw images and clickable rectangles
screen.fill(BLACK)
pygame.draw.rect(screen, RED, (rockX, rockY, 100, 100))  # Fix rectangle dimensions
screen.blit(rockImg, (rockX, rockY))
pygame.draw.rect(screen, BLUE, (paperX, paperY, 100, 100))
screen.blit(paperImg, (paperX, paperY))
pygame.draw.rect(screen, GREEN, (scissorsX, scissorsY, 100, 100))
screen.blit(scissorsImg, (scissorsX, scissorsY))
pygame.display.update()

# Main loop
while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            # Check if click is inside the rock rectangle
            if rockX <= mouseX <= rockX + 100 and rockY <= mouseY <= rockY + 100:
                clicked_value = 1
                print("You clicked Rock!")
                ComputerMove(rockImg)
            # Check if click is inside the paper rectangle
            elif paperX <= mouseX <= paperX + 100 and paperY <= mouseY <= paperY + 100:
                clicked_value = 2
                print("You clicked Paper!")
                ComputerMove (paperImg)
            # Check if click is inside the scissors rectangle
            elif scissorsX <= mouseX <= scissorsX + 100 and scissorsY <= mouseY <= scissorsY + 100:
                clicked_value = 3
                print("You clicked Scissors!")
                ComputerMove(scissorsImg)