import pygame 
#Pantalla 
title = "Mi primer juego"
size = [400,300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption(title)

#Paleta de colores del juego
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

#Game loop
gameover = False

#coordenadas de inicio
w = 10
h = 10
x_cord =  200
y_cord =  120
des_x = 0
des_y = 0

#general
vel = 2

#oponente
x_opo = 0
y_opo = 120
des_opo_y = 0


def dibujarPersonaje(x,y,color,scree,width,hight):
    pygame.draw.rect(screen, color, (x,y,w*6,h))

while not gameover:
    for event in pygame.event.get():
        #Cerra ventana de forma segura
        if event.type == pygame.QUIT:
            gameover = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                des_y = -vel
            elif event.key == pygame.K_DOWN:
                 des_y = vel
            #elif event.key == pygame.K_LEFT:
                #des_x = -vel
            #elif event.key == pygame.K_RIGHT:
                #des_x = vel

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                des_y = 0
            elif event.key == pygame.K_DOWN:
                 des_y = 0
           #elif event.key == pygame.K_LEFT:
                #des_x = 0
            #elif event.key == pygame.K_RIGHT:
                #des_x = 0


#Acciones del juego
    y_cord = y_cord + des_y
    y_opo = y_opo + des_opo_y 
    dibujarPersonaje(x_cord, y_cord, black, screen, w,h)
    dibujarPersonaje(x_opo, y_opo, black, screen, w,h)

    screen.fill(white) #color de la pantalla 
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()