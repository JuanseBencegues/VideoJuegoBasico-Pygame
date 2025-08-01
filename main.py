import pygame
import constantes
from personaje import Personaje

jugador  = Personaje(50,50)

pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)) #Inicia ventana
run = True

#nombre de la ventana
pygame.display.set_caption("Juego")

#definir variables de movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda = False

#Controlar frame-rate
reloj = pygame.time.Clock()



while run:
    #determinar fps
    reloj.tick(constantes.FPS)


    ventana.fill(constantes.COLOR_FONDO)

    #Calcular movimiento jugador
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD
    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD

    #mover al jugador
    jugador.movimiento(delta_x, delta_y)

    jugador.dibujar(ventana)
    #recorre los posibles distintos eventos que se ejecuten 
    for event in pygame.event.get(): #event.get entrega la lista de todos los eventos que pueden ocurrir
        if event.type == pygame.QUIT: 
            #event.type muestra que tipo de evento es 
            #pygame.QUIT accion de cerrar ventana (ej. click en la cruz)
            run = False
        #Cuando se precione una tecla
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_a: #Se presionó 'a'
                mover_izquierda = True
            if event.key == pygame.K_d: #Se presionó 'd'
                mover_derecha = True
            if event.key == pygame.K_w: #Se presionó 'w'
                mover_arriba = True
            if event.key == pygame.K_s: #Se presionó 's'
                mover_abajo = True
        #Cuando se suelte una tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a: 
                mover_izquierda = False
            if event.key == pygame.K_d: 
                mover_derecha = False
            if event.key == pygame.K_w: 
                mover_arriba = False
            if event.key == pygame.K_s: 
                mover_abajo = False


    pygame.display.update() #refleja cambios

pygame.quit()