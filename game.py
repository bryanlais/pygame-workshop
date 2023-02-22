import pygame
import sys
 
pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Trace")
clock = pygame.time.Clock()
 
loop = True
press = False
color = [(255,61,61),(17,64,20),(255,255,255),(252, 191, 91),(255, 255, 179),(194, 255, 191),(184, 240, 255),(175, 150, 235)]
#red, green, white, orange, yellow, light green, light blue, light purple
colornum = 0
while loop:
    try:
        #pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                  screen.fill(pygame.Color(0, 0, 0))
                if event.key == pygame.K_g:
                  colornum += 1
                  print(colornum)

        px, py = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1,0,0):
            pygame.draw.rect(screen, color[colornum%8], (px,py,10,10))
        if pygame.mouse.get_pressed() == (0,0,1):
            pygame.draw.rect(screen, (0,0,0), (px,py,10,10))
 
        if event.type == pygame.MOUSEBUTTONUP:
            press == False
        pygame.display.update()
    except:
        print("Something wrong happened!")