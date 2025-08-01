import pygame
import constantes
from personaje import Personaje

jugador  = Personaje(50,50)

pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)) #Inicia ventana

#nombre de la ventana
pygame.display.set_caption("Juego")

run = True

while run:
    jugador.dibujar(ventana)
    #recorre los posibles distintos eventos que se ejecuten 
    for event in pygame.event.get(): #event.get entrega la lista de todos los eventos que pueden ocurrir
        if event.type == pygame.QUIT: 
            #event.type muestra que tipo de evento es 
            #pygame.QUIT accion de cerrar ventana (ej. click en la cruz)
            run = False
    pygame.display.update() #refleja cambios

pygame.quit()