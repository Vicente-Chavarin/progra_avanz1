import pygame as py
#Pantalla 
title = "Mi primer juego"
size = [400,300]
screen = py.display.set_mode(size)
py.display.set_caption(title)

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

def dibujarPersonaje(x,y,color,w,h):
    py.draw.rect(screen, color, (x,y,w,h))

while not gameover:
    for event in py.event.get():
        #Cerra ventana de forma segura
        if event.type == py.QUIT:
            gameover = True
        elif event.type == py.KEYDOWN:
            if event.key == py.K_UP:
                des_y = -vel
            elif even.ket == py.K_DOWN:
                 des_y = vel
            elif even.ket == py.K_LEFT:
                des_y = -vel
            elif even.ket == py.K_RIGHT:
                des_y = vel

        #elif event.type == py.KEYUP:


#Acciones del juego
    dibujarPersonaje(x_cord, y_cord, green, width, height)
    screen.fill(white) #color de la pantalla 
    py.display.flip()

py.quit()