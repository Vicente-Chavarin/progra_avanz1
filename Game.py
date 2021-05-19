import pygame 
pygame.init()
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
y_cord =  150
des_x = 0
des_y = 0
vel = 0.05

def dibujarPersonaje(x,y,color):
    pygame.draw.rect(screen, color, (x,y,w,h))

while not gameover:
    for event in pygame.event.get():
        #Cerra ventana de forma segura
        if event.type == pygame.QUIT:
            gameover = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                des_y = -vel
            elif even.ket == pygame.K_DOWN:
                 des_y = vel
            elif even.ket == pygame.K_LEFT:
                des_y = -vel
            elif even.ket == pygame.K_RIGHT:
                des_y = vel

        #elif event.type == py.KEYUP:


#Acciones del juego
    dibujarPersonaje(x_cord, y_cord, green, width, height)
    screen.fill(white) #color de la pantalla 
    pygame.display.flip()

py.quit()